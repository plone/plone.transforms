from zope.interface import Attribute

from plone.transforms.interfaces import ICommandTransform


class IPipeTransform(ICommandTransform):
    """A transformation utility using a command line tool, through input
    and output pipes.
    """

    use_stdin = Attribute("Boolean indicating if the input should be written"
                          "to a temporary file or directly passed into stdin.")

    def extract_output(stdout):
        """Allow to extract only a part of the stdout and return it.
        For example we only might be interested in the body of a HTML file.
        """
