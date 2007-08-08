# -*- coding: UTF-8 -*-
"""
    Tests for the markdown transform.
"""

import unittest

from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.utils import configurationSetUp


def testMarkdownTransform():
    """
    First we get the transform utility.

      >>> from zope.component import queryUtility
      >>> from plone.transforms.interfaces import ITransform

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.markdown_html.MarkdownTransform')
      >>> util
      <plone.transforms.text.markdown_html.MarkdownTransform object at ...>

    Set up some test text:

      >>> data = iter(u"Some simple test text.")

    Now transform the data:

      >>> result = util.transform(data)

    And check the result:

      >>> util.available
      True

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> u''.join(result.data)
      u'\\n<p>Some simple test text.\\n</p>\\n\\n\\n'
    """


def test_suite():
    suite = unittest.TestSuite((
        DocTestSuite('plone.transforms.text.markdown_html'),
        ))
    suite.addTest(
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                        doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
