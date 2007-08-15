# -*- coding: UTF-8 -*-
"""
    PIL transform tests.
"""

import unittest

from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.utils import configurationSetUp


def testEmptyPILTransform():
    """
    Create a new command transform:

      >>> from plone.transforms.image.pil import PILTransform
      >>> transform = PILTransform()

    Set up some test data:

      >>> from plone.transforms.stringiter import StringIter
      >>> data = StringIter("I'm not an image.")

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
