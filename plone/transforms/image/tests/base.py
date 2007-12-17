from zope.component import queryUtility

from cStringIO import StringIO

from plone.transforms.image.tests.layer import PILLayer
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.tests.base import input_file_path as ifp

HAS_PIL = True
try:
    from PIL import Image
except ImportError:
    HAS_PIL = False

def input_file_path(name):
    return ifp(__file__, name)


class PILTransformTestCase(TransformTestCase):

    layer = PILLayer

    name = None
    class_ = None
    interface = None
    inputfiles = None
    output = None
    options = None

    def test_transform(self):
        util = queryUtility(ITransform, name=self.name)

        for inputfile in self.inputfiles:
            try:
                data = file(inputfile, 'rb')
                result = util.transform(data, options=self.options)
            finally:
                data.close()

            # Make sure we got back a proper result
            self.failUnless(ITransformResult.providedBy(result))
            self.failUnless(result.errors is None)

            # Did we get an iterator as the primary result data?
            self.failUnless(getattr(result.data, 'next', None) is not None)

            image = StringIO(''.join(result.data))
            pil_image = Image.open(image)

            self.failUnless(pil_image.format == self.output)

            # Check the size
            if self.options is not None:
                size = (self.options['width'], self.options['height'])
                self.failUnless(pil_image.size == size)
