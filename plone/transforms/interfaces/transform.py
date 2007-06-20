from zope.interface import Attribute, Interface


class ITransform(Interface):
    """A transformation utility.
    """

    inputs = Attribute("List of mimetypes this transform accepts "
                       "as inputs.")

    output = Attribute("Output mimetype")


    title = Attribute("The title of the transform.")

    description = Attribute("A description of the transform.")

    def convert(data, **kwargs):
        """
        The convert method takes some data in one of the input formats and
        returns it in the output format.
        """
