# -*- coding: UTF-8 -*-
"""
    Tests for the HTML body extractor.
"""

import unittest

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.interfaces import ITransform

from plone.transforms.tests.utils import configurationSetUp


def testHtmlBodyTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.html_body.HtmlBodyTransform')
      >>> util
      <plone.transforms.text.html_body.HtmlBodyTransform object at ...>

    Set up some test text:

      >>> data = iter(u"<html><head><title>Stupid title</title></head>"
      ...              "<body><p>Some simple test text.\\n</p></body></html>")

    Now transform the data:

      >>> result = util.transform(data)

    And check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

      >>> text = u''.join(result.data)
      >>> text
      u'<p>Some simple test text.\\n</p>'
    """


def test_suite():
    suite = unittest.TestSuite((
        DocTestSuite('plone.transforms.text.html_body'),
        ))
    suite.addTest(
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                        doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
