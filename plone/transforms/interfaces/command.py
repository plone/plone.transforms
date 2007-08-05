from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class ICommandTransform(ITransform):
    """A transformation utility using a command line tool.
    """

    command = Attribute("The name of the command line tool.")

    args = Attribute("The arguments for the command line tool.")

    command_available = Attribute("A boolean indicating if the command is "
                                  "available and accessible.")

    def initialize_tmpfile(data):
        """Create a temporary directory, copy input in a file there
        return the filehandle to the file.
        """
