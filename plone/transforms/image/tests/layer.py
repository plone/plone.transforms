import zope.component
from zope.component.testing import setUp
from zope.component.testing import tearDown

from zope.configuration.xmlconfig import XMLConfig

import plone.transforms.image


class PILLayer:

    @classmethod
    def setUp(cls):
        setUp()
        XMLConfig('meta.zcml', zope.component)()
        XMLConfig('meta.zcml', plone.transforms)()
        XMLConfig('configure.zcml', plone.transforms.image)()

    @classmethod
    def tearDown(cls):
        tearDown()
