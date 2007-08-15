from zope.component.testing import tearDown
from plone.transforms.tests.utils import configurationSetUp


class PILLayer:

    @classmethod
    def setUp(cls):
        configurationSetUp()

    @classmethod
    def tearDown(cls):
        tearDown()
