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

    def initialize_tmpfile(self, data):
        """Create a temporary directory, copy input in a file there
        return the path of the tmp dir and of the input file.
        """
        filehandle = tempfile.NamedTemporaryFile()
        filehandle.writelines(data)
        return filehandle

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        """
        try:
            filehandle = self.initialize_tmpfile(data)
            # do some stuff
            return TransformResult(iter(filehandle))
        finally:
            filehandle.close()
