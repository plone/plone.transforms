# -*- coding: UTF-8 -*-
"""
    PIL transform tests.
"""

import unittest

from os.path import abspath, dirname, join
from StringIO import StringIO

from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.utils import configurationSetUp

PREFIX = abspath(dirname(__file__))

def input_file_path(name):
    return join(PREFIX, 'input', name)


def testEmptyPILTransform():
    """
    Create a new command transform:

      >>> from plone.transforms.image.pil import PILTransform
      >>> transform = PILTransform()

    Set up some test data:

      >>> data = StringIO("I'm not an image.")

    Try to transform the data:

      >>> result = transform.transform(data)
      >>> result is None
      True

    Specify an output format:

      >>> transform.format = 'bmp'

      >>> result = transform.transform(data)
      >>> result
      <plone.transforms.transform.TransformResult object at ...>

    We haven't provided a real image:

      >>> result.data is None
      True

      >>> result.errors
      'cannot identify image file'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.image.pil'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
