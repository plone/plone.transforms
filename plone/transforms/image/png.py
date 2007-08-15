from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class PngTransform(PILTransform):
    """A transform which converts images to png files."""

    implements(IPILTransform)

    name = u'plone.transforms.image.png.PngTransform'
    title = _(u'title_pil_png_transform',
              default=u'A PIL transform which converts to PNG.')

    # We don't specify inputs, but take them from the base class
    output = 'image/png'
    format = 'png'
