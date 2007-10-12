from os.path import abspath, dirname, join
from unittest import TestCase

from zope.component import queryUtility
from zope.interface.verify import verifyClass

from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult
from plone.transforms.tests.layer import TransformLayer


def input_file_path(file_, name):
    return join(abspath(dirname(file_)), 'input', name)


class TransformTestCase(TestCase):

    layer = TransformLayer

    name = None
    class_ = None
    interface = None
    input_ = None
    output = None

    def test_interface(self):
        verifyClass(self.interface, self.class_)

    def test_registration(self):
        util = queryUtility(ITransform, name=self.name)
        self.failIf(util is None)
        self.failUnless(isinstance(util, self.class_))

    def test_invalid_transform(self):
        util = queryUtility(ITransform, name=self.name)
        try:
            result = util.transform(None)
        except ValueError, e:
            if e.args[0].endswith('The transform is unavailable.'):
                return
            raise
        self.failUnless(result is None)

        result = util.transform(u'foo')
        self.failUnless(result is None)

    def test_transform(self):
        util = queryUtility(ITransform, name=self.name)

        if not util.available:
            return

        result = util.transform(self.input_)

        # Make sure we got back a proper result
        self.failUnless(ITransformResult.providedBy(result))
        self.failUnless(not result.errors)

        # Did we get an iterator as the primary result data?
        self.failUnless(getattr(result.data, 'next', None) is not None)

        # Check the beginning of the output only
        result_string = ''.join(result.data)
        self.failUnless(result_string.startswith(self.output))
