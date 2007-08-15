# -*- coding: UTF-8 -*-
"""
    PIL Gif transform tests.
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


def testGifTransform():
    """
    Create a new transform:

      >>> from zope.component import queryUtility
      >>> from plone.transforms.interfaces import IPILTransform

      >>> transform = queryUtility(IPILTransform,
      ...     name='plone.transforms.image.gif.GifTransform')
      >>> transform
      <plone.transforms.image.gif.GifTransform object at ...>

    Set up some test data:

      >>> filename = input_file_path('logo.jpg')
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

      >>> ''.join(result.data).startswith('GIF87a\x18\')
      True

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

      >>> ''.join(result.data).startswith('GIF87a\x18\')
      True

    Now we try it again, while only providing an iterator and not a file object:

      >>> data = file(filename, 'rb')
      >>> value = iter(''.join(data))

    Try to transform the data again:

      >>> result = transform.transform(value)
      >>> data.close()

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.errors is None
      True

      >>> result.data
      <cStringIO.StringO object at ...>

      >>> ''.join(result.data).startswith('GIF87a\x18\')
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
