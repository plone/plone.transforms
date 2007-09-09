from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class JpegTransform(PILTransform):
    """A transform which converts images to jpeg files."""

    name = u'plone.transforms.image.jpeg.JpegTransform'
    title = _(u'title_pil_jpeg_transform',
              default=u'A PIL transform which converts to JPEG.')

    output = 'image/jpeg'
    format = 'jpeg'
