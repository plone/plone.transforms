from zope.interface import Attribute, Interface

from plone.transforms.interfaces.transform import ITransform


class ITransformChain(ITransform):
    """
    A transformation chain utility, which implements Python's list protocol.
    
    It stores a list of (interface, name) tuples which identify transforms.
    
    The input formats are defined as the input formats of the first transform
    in the chain. The output format is the output format of the last transform.
    """
