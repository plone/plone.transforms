from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.image.pil import PILTransform


class JpegTransform(PILTransform):
    """A transform which converts images to jpeg files based on the Python
    Imaging library.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPILTransform, JpegTransform)
      True
    """

    implements(IPILTransform)

    name = u'plone.transforms.image.jpeg.JpegTransform'
    title = _(u'title_pil_jpeg_transform',
              default=u'A PIL transform which converts to JPEG.')
    description = None

    # We don't specify inputs, but take them from the base class
    output = 'image/jpeg'
    format = 'jpeg'
