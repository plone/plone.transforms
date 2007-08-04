import os
import tempfile

from zope.interface import implements

from plone.transforms.interfaces import ICommandTransform

from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import TransformResult

from plone.transforms.message import PloneMessageFactory as _


class PipeTransform(PersistentTransform):
    """A persistent transform which runs a transform based on a command line
    tool and handles input and output through pipes.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICommandTransform, PipeTransform)
      True
    """

    implements(ICommandTransform)

    inputs = (None, )
    output = None

    name = u'plone.transforms.transform.PipeTransform'
    title = _(u'title_skeleton_pipe_transform',
              default=u'A skeleton pipe transform.')
    description = None

    command = None
    args = None

    def writeBinary(self, fd, firstchunk, data):
        os.write(fd, firstchunk)
        for chunk in data:
            os.write(fd, chunk)

    def writeText(self, fd, firstchunk, data):
        os.write(fd, firstchunk.encode('utf-8'))
        for chunk in data:
            os.write(fd, chunk.encode('utf-8')) 

    def initialize_tmpfile(self, data):
        """Create a temporary directory, copy input in a file there
        return the path of the tmp dir and of the input file.
        """
        filehandle, tmpname = tempfile.mkstemp(text=False)
        # write data to tmp using a file descriptor
        firstchunk = data.next()
        if isinstance(firstchunk, unicode):
            self.writeText(filehandle, firstchunk, data)
        else:
            self.writeBinary(filehandle, firstchunk, data)
        # close it so the other process can read it
        os.close(filehandle)
        return tmpname

    def extractOutput(self, stdout):
        return stdout.read()

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        """
        tmpname = self.initialize_tmpfile(data)
        # do some stuff
        commandline = "%s %s" % (self.command, self.args)
        commandline = commandline % { 'infile' : tmpname }

        child_stdin, child_stdout = os.popen4(commandline, 'b')

        status = child_stdin.close()
        out = self.extractOutput(child_stdout)
        child_stdout.close()

        os.unlink(tmpname)

        return TransformResult(iter(out))
