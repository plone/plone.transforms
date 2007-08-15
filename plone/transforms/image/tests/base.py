from os.path import abspath, dirname, join
from unittest import TestCase

from zope.component import queryUtility

from plone.transforms.image.tests.layer import PILLayer
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult

PREFIX = abspath(dirname(__file__))

def input_file_path(name, prefix=PREFIX):
    return join(PREFIX, 'input', name)


class PILTransformTestCase(TestCase):

    layer = PILLayer

    name = None
    class_ = None
    inputfiles = None
    output = None

    def test_registration(self):
        util = queryUtility(ITransform, name=self.name)
        self.failIf(util is None)
        self.failUnless(isinstance(util, self.class_))

    def test_invalid_transform(self):
        util = queryUtility(ITransform, name=self.name)
        result = util.transform(None)
        self.failUnless(result is None)

        result = util.transform(u'foo')
        self.failUnless(result is None)

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
