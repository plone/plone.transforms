import os
import tempfile

from zope.interface import implements

from plone.transforms.interfaces import IPipeTransform

from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import TransformResult

from plone.transforms.message import PloneMessageFactory as _


class PipeTransform(PersistentTransform):
    """A persistent transform which runs a transform based on a command line
    tool and handles input and output through pipes.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPipeTransform, PipeTransform)
      True
    """

    implements(IPipeTransform)

    inputs = (None, )
    output = None

    name = u'plone.transforms.transform.PipeTransform'
    title = _(u'title_skeleton_pipe_transform',
              default=u'A skeleton pipe transform.')
    description = None

    command = None
    args = None
    use_stdin = False

    def write(self, fd, data):
        # write data to tmp using a file descriptor
        firstchunk = data.next()
        if isinstance(firstchunk, unicode):
            self.writeText(fd, firstchunk, data)
        else:
            self.writeBinary(fd, firstchunk, data)

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
        fd, tmpname = tempfile.mkstemp(text=False)
        # write data to tmp using a file descriptor
        self.write(fd, data)
        # close it so the other process can read it
        os.close(fd)
        return tmpname

    def extractOutput(self, stdout):
        return stdout.read()

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        """
        if not self.use_stdin:
            tmpname = self.initialize_tmpfile(data)
            commandline = "%s %s" % (self.command, self.args)
            commandline = commandline % { 'infile' : tmpname }

        child_stdin, child_stdout = os.popen4(commandline, 'b')

        if self.use_stdin:
            self.write(child_stdin, data)

        status = child_stdin.close()
        out = self.extractOutput(child_stdout)
        child_stdout.close()

        if not self.use_stdin:
            os.unlink(tmpname)

        return TransformResult(iter(out))
