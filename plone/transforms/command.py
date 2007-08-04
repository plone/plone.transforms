import os
import shutil
import tempfile

from zope.interface import implements

from plone.transforms.interfaces import ICommandTransform

from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import TransformResult

from plone.transforms.message import PloneMessageFactory as _


class CommandTransform(PersistentTransform):
    """A persistent transform which runs a transform based on a command line
    tool.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICommandTransform, CommandTransform)
      True
    """

    implements(ICommandTransform)

    inputs = (None, )
    output = None

    name = u'plone.transforms.transform.CommandTransform'
    title = _(u'title_skeleton_command_transform',
              default=u'A skeleton command transform.')
    description = None

    command = None
    args = None

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
        return the path of the tmp file.
        """
        fd, tmpfilepath = tempfile.mkstemp(text=False)
        # write data to tmp using a file descriptor
        self.write(fd, data)
        # close it so the other process can read it
        os.close(fd)
        return tmpfilepath

    def prepare_transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        """
        tmpfilepath = self.initialize_tmpfile(data)
        tmpdirpath = tempfile.mkdtemp()

        commandline = 'cd "%s" && %s %s' % (
            tmpfilepath, self.command, self.args)

        commandline = commandline % { 'infile' : tmpfilepath }
        if os.name=='posix':
            commandline = commandline + ' 2>error_log 1>/dev/null'

        os.system(commandline)

        subobjects = {}
        for tmpfile in os.listdir(tmpdirpath):
            tmp = os.path.join(tmpfilepath, tmpfilepath)
            subobjects[tmpfile] = file(tmp, 'rb').read()
            os.unlink(tmp)

        result = TransformResult(None)
        result.subobject = subobjects

        os.unlink(tmpfilepath)
        shutil.rmtree(tmpdirpath)

        return result

    def transform(self, data):
        """Prepare the transform result and hand back everything as subobjects.
        You can then pick the default content from the result object and put
        it into the default data.
        """
        result = self.prepare_transform(data)
        return result
