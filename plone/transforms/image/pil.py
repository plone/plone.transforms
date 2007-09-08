from cStringIO import StringIO
from logging import DEBUG

from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.log import log
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

    inputs = ('image/x-ms-bmp', 'image/gif', 'image/jpeg', 'image/pcx',
              'image/png', 'image/x-portable-pixmap', 'image/tiff')
    output = None

    available = False

    format = None
    width = None
    height = None

    def __init__(self):
        super(PILTransform, self).__init__()
        if HAS_PIL:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        if self.format is None:
            return None

        result = TransformResult(None)
        try:
            # If we already got a file-like iterator use it
            if isinstance(data, file):
                orig = data
            else:
                orig = StringIO()
                orig.writelines(data)
                orig.seek(0)

            try:
                pil_image = Image.open(orig)
            except IOError, e:
                result.errors = str(e)
                log(DEBUG, "Error %s while transforming an Image in %s." %
                            (str(e), self.name))
                return result

            if self.format in ['jpeg', 'ppm']:
                pil_image.draft("RGB", pil_image.size)
                pil_image = pil_image.convert("RGB")

            if self.width and self.height:
                pil_image.thumbnail((self.width,self.height), Image.ANTIALIAS)

            transformed = StringIO()
            pil_image.save(transformed, self.format)
            transformed.seek(0)

        finally:
            orig.close()

        result.data = transformed
        return result
