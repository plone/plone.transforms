from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class IPILTransform(ITransform):
    """A transform which runs a transform based on the Python Imaging library.
    """
