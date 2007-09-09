import zope.app.publisher.browser
import zope.component
from zope.component.testing import setUp
from zope.component.testing import tearDown

from zope.configuration.xmlconfig import XMLConfig

import plone.transforms


class TransformLayer:

    @classmethod
    def setUp(cls):
        setUp()
        XMLConfig('meta.zcml', zope.component)()
        XMLConfig('meta.zcml', zope.app.publisher.browser)()
        XMLConfig('meta.zcml', plone.transforms)()
        XMLConfig('configure.zcml', plone.transforms)()

    @classmethod
    def tearDown(cls):
        tearDown()
