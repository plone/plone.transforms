from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import TransformResult

HAS_PIL = True
try:
    from PIL import Image
except ImportError:
    HAS_PIL = False


class PILTransform(PersistentTransform):
    """A persistent transform which runs a transform based on the Python
    Imaging library.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPILTransform, PILTransform)
      True
    """

    implements(IPILTransform)

    name = u'plone.transforms.image.pil.PILTransform'
    title = _(u'title_skeleton_pil_transform',
              default=u'A skeleton PIL transform.')
    description = None

    inputs = (None, )
    output = None

    available = False

    def __init__(self):
        super(PILTransform, self).__init__()
        if HAS_PIL:
            self.available = True

    def transform(self, data):
        if not self.available:
            return None
        return TransformResult(None)
