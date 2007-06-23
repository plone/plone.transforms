# -*- coding: UTF-8 -*-
"""
    Tests for the markdown transform.
"""

import unittest

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.interfaces import ITransform
from plone.transforms.text.markdown_html import HAS_MARKDOWN


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.transforms)()

def testMarkdownTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.markdown_html.MarkdownTransform')
      >>> util
      <plone.transforms.text.markdown_html.MarkdownTransform object at ...>

    Set up some test text:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Now transform the data:

      >>> result = util.transform(data)

    And check the result:

      >>> result
      <generator object at ...>

      >>> u''.join(result)
      u'\\n<p>Some simple test text.\\n</p>\\n\\n\\n'
    """


def test_suite():
    suite = unittest.TestSuite((
        DocTestSuite('plone.transforms.text.markdown_html'),
        ))
    if HAS_MARKDOWN:
        suite.addTest(
            DocTestSuite(setUp=configurationSetUp,
                         tearDown=tearDown,
                         optionflags=doctest.ELLIPSIS | 
                            doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
