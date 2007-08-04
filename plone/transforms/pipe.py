import os
import tempfile

from zope.interface import implements

from plone.transforms.interfaces import IPipeTransform

from plone.transforms.command import CommandTransform
from plone.transforms.transform import TransformResult

from plone.transforms.message import PloneMessageFactory as _


class PipeTransform(CommandTransform):
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

    def extractOutput(self, stdout):
        return stdout.read()

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        """
        if self.command is None:
            return None

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
