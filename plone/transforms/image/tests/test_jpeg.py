# -*- coding: UTF-8 -*-
"""
    PIL Jpeg transform tests.
"""

import unittest

from os.path import abspath, dirname, join

from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.utils import configurationSetUp

PREFIX = abspath(dirname(__file__))

def input_file_path(name):
    return join(PREFIX, 'input', name)


def testJpegTransform():
    """
    Create a new transform:

      >>> from zope.component import queryUtility
      >>> from plone.transforms.interfaces import IPILTransform

      >>> transform = queryUtility(IPILTransform,
      ...     name='plone.transforms.image.jpeg.JpegTransform')
      >>> transform
      <plone.transforms.image.jpeg.JpegTransform object at ...>

    Set up some test data:

      >>> filename = input_file_path('logo.gif')
      >>> data = file(filename, 'rb')

    Try to transform the data:

      >>> result = transform.transform(data)
      >>> data.close()

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.errors is None
      True

      >>> result.data
      <cStringIO.StringO object at ...>

      >>> ''.join(result.data)[0:10]
      '\\xff\\xd8\\xff\\xe0\\x00\\x10JFIF'

    Set up some more test data:

      >>> filename = input_file_path('logo.png')
      >>> data = file(filename, 'rb')

    Try to transform the data:

      >>> result = transform.transform(data)
      >>> data.close()

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.errors is None
      True

      >>> ''.join(result.data)[0:10]
      '\\xff\\xd8\\xff\\xe0\\x00\\x10JFIF'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
