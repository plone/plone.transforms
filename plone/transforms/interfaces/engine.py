from zope.interface import Interface


class ITransformEngine(Interface):
    """
    A transformation engine, which provides helper methods to transform data.
    
    It looks up ITransform utilities for a given input and output mimetype
    combination and provides a method to transform the data into the desired
    outpyt format.
    """

    def available_transforms():
        """
        Returns a list of all available transforms. The list entries are
        triples of (input mimetype, output mimetype, transform).
        """

    def transform(data, input_mimetype, output_mimetype):
        """
        The transform method takes some data in one of the input formats.
        It returns either an ITransformResult in the output format or None
        if an error occurred.
        """
