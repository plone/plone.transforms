from zope.interface import Attribute, Interface


class ITransform(Interface):
    """A transformation utility.
    """

    inputs = Attribute("List of mimetypes this transform accepts as inputs. "
                       "Mimetypes syntax follows rfc2045 / rfc4288.")

    output = Attribute("Mimetype this transform outputs. Mimetypes syntax "
                       "follows rfc2045 / rfc4288.")

    name = Attribute("A unique name for the transform.")

    title = Attribute("The title of the transform.")

    description = Attribute("A description of the transform.")

    def transform(data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """


class IMultipleOutputTransform(Interface):
    """A transformation utility which may return multiple output streams.
    """

    inputs = Attribute("List of mimetypes this transform accepts as inputs. "
                       "Mimetypes syntax follows rfc2045 / rfc4288.")

    output = Attribute("Mimetype of the default output of this transform. "
                       "Mimetypes syntax follows rfc2045 / rfc4288.")

    name = Attribute("A unique name for the transform.")

    title = Attribute("The title of the transform.")

    description = Attribute("A description of the transform.")

    def transform(data):
        """
        The transform method takes some data in one of the input formats.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.

        It returns a dict of named output streams, with a default output stream
        named 'default'.
        """
