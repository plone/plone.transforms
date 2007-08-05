# -*- coding: UTF-8 -*-
"""
    Tests for the HTML to text transform.
"""

import unittest
from StringIO import StringIO

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.interfaces import ITransform

from plone.transforms.tests.utils import configurationSetUp


def testHtmlTextTransform():
    r"""
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.html_text.HtmlToTextTransform')
      >>> util
      <plone.transforms.text.html_text.HtmlToTextTransform object at ...>

    Set up some test text:

      >>> text = unicode("\n<html><head><title>Stupid title</title></head><body>"
      ... "<p>Some simple test text héhé.\n</p>\n\n\n</body></html>", 'utf-8')
      >>> data = StringIO(text)

    Now transform the data:

      >>> result = util.transform(data)

    And check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <StringIO.StringIO instance at ...>

      >>> text = u''.join(result.data)
      >>> text.strip()
      u'Stupid title   Some simple test text h\xe9h\xe9.'
    """


def test_suite():
    suite = unittest.TestSuite((
        DocTestSuite('plone.transforms.text.html_text'),
        ))
    suite.addTest(
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                        doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
