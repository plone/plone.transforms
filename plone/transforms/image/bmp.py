from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class BmpTransform(PILTransform):
    """A transform which converts images to bmp files."""

    title = _(u'title_pil_bmp_transform',
              default=u'A PIL transform which converts to BMP.')

    output = 'image/x-ms-bmp'
    format = 'bmp'
