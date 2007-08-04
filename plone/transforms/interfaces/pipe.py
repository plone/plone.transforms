from zope.interface import Attribute

from plone.transforms.interfaces import ICommandTransform


class IPipeTransform(ICommandTransform):
    """A transformation utility using a command line tool, through input
    and output pipes.
    """

    command = Attribute("The name of the command line tool.")

    args = Attribute("The arguments for the command line tool.")

    use_stdin = Attribute("Boolean indicating if the input should be written"
                          "to a temporary file or directly passed into stdin.")
