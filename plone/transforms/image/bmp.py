from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class BmpTransform(PILTransform):
    """A transform which converts images to bmp files."""

    implements(IPILTransform)

    name = u'plone.transforms.image.bmp.BmpTransform'
    title = _(u'title_pil_bmp_transform',
              default=u'A PIL transform which converts to BMP.')

    # We don't specify inputs, but take them from the base class
    output = 'image/x-ms-bmp'
    format = 'bmp'
