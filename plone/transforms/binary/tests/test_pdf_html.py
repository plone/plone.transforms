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

def testPDFCommandTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.pdf_html.PDFCommandTransform')
      >>> util
      <plone.transforms.binary.pdf_html.PDFCommandTransform object at ...>

    Set up some test text:

      >>> filename = input_file_path('test_pdf_html_complex.pdf')
      >>> handle = file(filename, 'rb')
      >>> text = iter(handle.read())
      >>> handle.close()

    Now transform the data:

      >>> result = util.transform(text)

    And check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

      >>> 'Plone is awesome' in u''.join(result.data)
      True

    We got four subobjects:

      >>> len(result.subobjects)
      4

    Two of them are images:

      >>> images = [f for f in result.subobjects.keys() if f.endswith('png')]
      >>> len(images)
      2

      >>> image1 = result.subobjects[images[0]]
      >>> image1
      <iterator object at ...>

      >>> ''.join(image1).startswith('\x89PNG')
      True
    """


def testPDFPipeTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.text.pdf_html.PDFPipeTransform')
      >>> util
      <plone.transforms.binary.pdf_html.PDFPipeTransform object at ...>

    Set up some test text:

      >>> filename = input_file_path('test_pdf_html.pdf')
      >>> handle = file(filename, 'rb')
      >>> text = iter(handle.read())
      >>> handle.close()

    Now transform the data:

      >>> result = util.transform(text)

    And check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

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
