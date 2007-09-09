from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class PpmTransform(PILTransform):
    """A transform which converts images to ppm files."""

    name = u'plone.transforms.image.ppm.PpmTransform'
    title = _(u'title_pil_ppm_transform',
              default=u'A PIL transform which converts to PPM.')

    output = 'image/x-portable-pixmap'
    format = 'ppm'
