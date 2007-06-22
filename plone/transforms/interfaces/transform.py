from zope.interface import Attribute, Interface


class ITransform(Interface):
    """A transformation utility.
    """

    inputs = Attribute("List of mimetypes this transform accepts as inputs. "
                       "Mimetypes syntax follows rfc2045 / rfc4288.")

    output = Attribute("Mimetype this transform outputs. Mimetypes syntax "
                       "follows rfc2045 / rfc4288.")

    title = Attribute("The title of the transform.")

    description = Attribute("A description of the transform.")

    def convert(data):
        """
        The convert method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """
