from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class TiffTransform(PILTransform):
    """A transform which converts images to tiff files."""

    name = u'plone.transforms.image.tiff.TiffTransform'
    title = _(u'title_pil_tiff_transform',
              default=u'A PIL transform which converts to TIFF.')

    output = 'image/tiff'
    format = 'tiff'
