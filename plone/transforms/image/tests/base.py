from zope.component import queryUtility

from plone.transforms.image.tests.layer import PILLayer
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.tests.base import input_file_path as ifp

def input_file_path(name):
    return ifp(__file__, name)


class PILTransformTestCase(TransformTestCase):

    layer = PILLayer

    name = None
    class_ = None
    interface = None
    inputfiles = None
    output = None

    def test_transform(self):
        util = queryUtility(ITransform, name=self.name)

        for inputfile in self.inputfiles:
            try:
                data = file(inputfile, 'rb')
                result = util.transform(data)
            finally:
                data.close()

            # Make sure we got back a proper result
            self.failUnless(ITransformResult.providedBy(result))
            self.failUnless(result.errors is None)

            # Did we get an iterator as the primary result data?
            self.failUnless(getattr(result.data, 'next', None) is not None)

            # Check the beginning of the file only
            result_string = ''.join(result.data)
            self.failUnless(result_string.startswith(self.output))
