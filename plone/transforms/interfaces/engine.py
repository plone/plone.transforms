from zope.interface import Attribute
from zope.interface import Interface


class ITransformEngine(Interface):
    """
    A transformation engine, which provides helper methods to transform data.
    
    It looks up ITransform utilities for a given input and output mimetype
    combination and provides a method to transform the data into the desired
    outpyt format.
    """

    def unavailable_transforms():
        """
        Returns a list of all registered but unavailable transforms. The list
        entries are triples of (input mimetype, output mimetype, transform).
        """

    def available_transforms():
        """
        Returns a list of all available transforms. The list entries are
        triples of (input mimetype, output mimetype, transform).
        """

    def find_transform(input_mimetype, output_mimetype):
        """
        The find_transform method returns the transform which is going to
        be used for a particular input / output mimetype combination.
        """

    def transform(data, input_mimetype, output_mimetype, options=None):
        """
        The transform method takes some data in one of the input formats.
        It returns either an ITransformResult including data the output format
        or None if an error occurred.

        The optional options dictonary can be used to provide additional
        arguments to influence the result of the transform, like image sizes
        or quality settings.
        
        Per default it will contain both the input_mimetype and output_mimetype
        values provided to this method.
        """


class IConfigurableTransformEngine(ITransformEngine):
    """
    A transformation engine, which provides helper methods to transform data.
    
    It bases its transform finding algorithm on the explicitely set
    configuration information stored in itself.
    """
