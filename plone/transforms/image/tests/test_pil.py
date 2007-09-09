# -*- coding: UTF-8 -*-
"""
    PIL transform tests.
"""

import unittest

from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.image.pil import HAS_PIL
from plone.transforms.tests.utils import configurationSetUp


def testPILTransform():
    """
    Let's make sure that this implementation actually fulfills the API.

      >>> from plone.transforms.interfaces import IPILTransform
      >>> from plone.transforms.image.pil import PILTransform

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPILTransform, PILTransform)
      True

    Create a new command transform:

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
    if HAS_PIL:
        return unittest.TestSuite((
            DocTestSuite(setUp=configurationSetUp,
                         tearDown=tearDown,
                         optionflags=doctest.ELLIPSIS | 
                                     doctest.NORMALIZE_WHITESPACE),
            ))
    else:
        return unittest.TestSuite()
