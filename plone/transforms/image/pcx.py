from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class PcxTransform(PILTransform):
    """A transform which converts images to pcx files."""

    name = u'plone.transforms.image.pcx.PcxTransform'
    title = _(u'title_pil_pcx_transform',
              default=u'A PIL transform which converts to PCX.')

    output = 'image/pcx'
    format = 'pcx'
