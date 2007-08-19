from zope.component import queryUtility

from plone.transforms.binary.tests.layer import BinaryLayer
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.tests.base import input_file_path as ifp

def input_file_path(name):
    return ifp(__file__, name)


class BinaryTransformTestCase(TransformTestCase):

    layer = BinaryLayer

    name = None
    class_ = None
    interface = None
    inputfile = None
    output = None

    def test_transform(self):
        util = queryUtility(ITransform, name=self.name)
        result = None

        if not util.available:
            return

        try:
            data = file(self.inputfile, 'rb')
            result = util.transform(data)
        finally:
            data.close()

        # Make sure we got back a proper result
        self.failUnless(ITransformResult.providedBy(result))
        self.failUnless(not result.errors)

        # Did we get an iterator as the primary result data?
        self.failUnless(getattr(result.data, 'next', None) is not None)

        # Check the beginning of the file only
        result_string = ''.join(result.data)
        self.failUnless(result_string.startswith(self.output))