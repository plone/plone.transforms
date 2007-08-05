from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class ICommandTransform(ITransform):
    """A transformation utility using a command line tool.
    """

    command = Attribute("The name of the command line tool.")

    args = Attribute("The arguments for the command line tool.")

    def initialize_tmpfile(data):
        """Create a temporary file and copy input into it.
        Returns the path of the tmp file.
        """
