from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class GifTransform(PILTransform):
    """A transform which converts images to gif files."""

    name = u'plone.transforms.image.gif.GifTransform'
    title = _(u'title_pil_gif_transform',
              default=u'A PIL transform which converts to GIF.')

    output = 'image/gif'
    format = 'gif'
