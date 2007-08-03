# -*- coding: UTF-8 -*-
"""
    Tests for the pdf to html transform.
"""

import unittest

from os.path import join, abspath, dirname

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.interfaces import ITransform

from plone.transforms.tests.utils import configurationSetUp


PREFIX = abspath(dirname(__file__))

def input_file_path(name):
    return join(PREFIX, 'input', name)


def testPDFTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.pdf_html.PDFTransform')
      >>> util
      <plone.transforms.binary.pdf_html.PDFTransform object at ...>

    Set up some test text:

      >>> filename = input_file_path('test_pdf_html.pdf')
      >>> handle = file(filename, 'rb')
      >>> text = (c for c in handle.read())
      >>> handle.close()

    Now transform the data:

      >>> result = util.transform(text)

    And check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <generator object at ...>

      >>> beginning = "<A name=1></a>test_pdf_html.py<br>\\n2007-08-03<br>\\n# -*- coding: UTF-8"
      >>> beginning in ''.join(result.data)
      True
    """


def test_suite():
    suite = unittest.TestSuite((
        DocTestSuite('plone.transforms.binary.pdf_html'),
        ))
    suite.addTest(
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                        doctest.NORMALIZE_WHITESPACE))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
