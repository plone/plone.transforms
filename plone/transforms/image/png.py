from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class PngTransform(PILTransform):
    """A transform which converts images to png files."""

    name = u'plone.transforms.image.png.PngTransform'
    title = _(u'title_pil_png_transform',
              default=u'A PIL transform which converts to PNG.')

    output = 'image/png'
    format = 'png'
