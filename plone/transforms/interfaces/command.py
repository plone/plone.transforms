from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class ICommandTransform(ITransform):
    """A transformation utility using a command line tool.
    """

    command = Attribute("The name of the command line tool.")

    args = Attribute("The arguments for the command line tool.")

    def initialize_tmpfile(data, directory=None):
        """Create a temporary file and copy input into it.
        Returns the path of the tmp file.

        The temporary directory in which the file is being created can
        optionally be specified via the directory argument.
        """

    def prepare_transform(data, arguments=None):
        """The method takes some data in one of the input formats and returns
        a TransformResult with data in the output format.

        You can pass an additional dictonary of arguments which will be
        replaced in the actual command line call.
        """
