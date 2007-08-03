from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class ICommandTransform(ITransform):
    """A transformation utility using a command line tool.
    """

    command = Attribute("The name of the command line tool.")

    args = Attribute("The arguments for the command line tool.")

    def extractOutput(stdout):
        """Allow to extract only a part of the stdout and return it.
        For example we only might be interested in the body of a HTML file.
        """

    def initialize_tmpfile(data):
        """Create a temporary directory, copy input in a file there
        return the filehandle to the file.
        """
