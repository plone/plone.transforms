from cStringIO import StringIO

from zope.interface import implements

from plone.transforms.interfaces import IPILTransform
from plone.transforms.log import log_debug
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
    """

    implements(IPILTransform)

    name = u'plone.transforms.image.pil.PILTransform'
    title = _(u'title_skeleton_pil_transform',
              default=u'A skeleton PIL transform.')

    inputs = ('image/x-ms-bmp', 'image/gif', 'image/jpeg', 'image/pcx',
              'image/png', 'image/x-portable-pixmap', 'image/tiff')
    output = None

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

        width = self.width
        height = self.height

        # Allow to override the size settings via the options dict
        if options is not None:
            width = options.get('width', width)
            height = options.get('height', height)

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
                log_debug("Error %s while transforming an Image in %s." %
                          (str(e), self.name))
                return result

            transparency = pil_image.info.get("transparency", False)

            if self.format in ['jpeg', 'ppm']:
                pil_image.draft("RGB", pil_image.size)
                pil_image = pil_image.convert("RGB")

            if width is None:
                width = pil_image.size[0]
            if height is None:
                height = pil_image.size[1]

            if width and height:
                pil_image.thumbnail((width, height), Image.ANTIALIAS)

            transformed = StringIO()

            # Only use transparency in the supported modes
            if self.format == 'png' and pil_image.mode not in ('P', 'L'):
                pil_image.save(transformed, self.format)
            else:
                pil_image.save(transformed,
                               self.format,
                               transparency=transparency)

            transformed.seek(0)

        finally:
            orig.close()

        result.data = transformed
        return result
