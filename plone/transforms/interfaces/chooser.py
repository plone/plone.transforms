from zope.interface import Attribute, Interface


class ITransformChooser(Interface):
    """
    A transformation chooser is responsible for choosing an appropriate
    transformation engine for a certain transformation.
    
    Transformation engines can be spread among different servers and can be
    called asynchronously.
    """

    engines = Attribute("A list of ITransformEngineRegistration entries.")

    def transform(data, input_mimetype, output_mimetype):
        """
        The transform method takes some data in the input format and returns
        it in the output format.
        """
