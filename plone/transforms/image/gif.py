from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class GifTransform(PILTransform):
    """A transform which converts images to gif files based on the Python
    Imaging library.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPILTransform, GifTransform)
      True
    """

    implements(IPILTransform)

    name = u'plone.transforms.image.gif.GifTransform'
    title = _(u'title_skeleton_pil_gif_transform',
              default=u'A PIL transform which converts to GIF.')
    description = None

    # We don't specify inputs, but take them from the base class
    output = 'image/gif'

    available = False

    format = 'gif'
    width = None
    height = None

    def __init__(self):
        super(GifTransform, self).__init__()
