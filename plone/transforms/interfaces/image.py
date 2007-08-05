from zope.interface import Attribute

from plone.transforms.interfaces import ITransform


class IPILTransform(ITransform):
    """A transform which runs a transform based on the Python Imaging library.
    """

    format = Attribute("The desired output format in a format supported by PIL.")

    width = Attribute("The new width of the image, None if no rescaling "
                      "should take place.")

    height = Attribute("The new height of the image, None if no rescaling "
                       "should take place.")
