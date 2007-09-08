from plone.transforms.interfaces.transform import ITransform


class ITransformChain(ITransform):
    """
    A transformation chain utility, which implements Python's list protocol.
    
    It stores a list of (interface_name, name) tuples which identify transforms.
    The interface_name must be the full dotted path to an actual interface.
    
    The input formats are defined as the input formats of the first transform
    in the chain. The output format is the output format of the last transform.
    """

    def transform(data, options=None):
        """
        The transform method takes some data in one of the input formats.
        It returns either an ITransformResult in the output format or None
        if an error occurred.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        
        The method might raise a ValueError if one of the registered transforms
        is not available or invalid.

        The optional options dictonary can be used to provide additional
        arguments to influence the result of the transform, like image sizes
        or quality settings.
        """
