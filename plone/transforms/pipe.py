import os
from cStringIO import StringIO

from zope.interface import implements

from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import IPipeTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import TransformResult


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

    title = _(u'title_skeleton_pipe_transform',
              default=u'A skeleton pipe transform.')
    description = None

    available = False

    command = None
    args = None
    use_stdin = False

    def __init__(self):
        super(PipeTransform, self).__init__()

    def extract_output(self, stdout):
        out = StringIO()
        out.writelines(stdout)
        out.seek(0)
        return out

    def transform(self, data, options=None):
        """Returns the transform result."""
        if self._validate(data) is None:
            return None

        commandline = "%s %s" % (self.command, self.args)
        if not self.use_stdin:
            tmpname = self.initialize_tmpfile(data)
            commandline = commandline % { 'infile' : tmpname }

        child_stdin, child_stdout, child_stderr = os.popen3(commandline, 'b')

        if self.use_stdin:
            self.write(child_stdin, data)

        status = child_stdin.close()
        out = self.extract_output(child_stdout)
        child_stdout.close()

        if not self.use_stdin:
            os.unlink(tmpname)

        # Add the errors to the transform result
        result = TransformResult(out)
        result.errors = child_stderr.read()
        child_stderr.close()
        return result
