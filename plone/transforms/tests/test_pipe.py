# -*- coding: UTF-8 -*-
"""
    Pipe transform tests.
"""

import unittest

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.pipe import PipeTransform
from plone.transforms.interfaces import IPipeTransform

from plone.transforms.tests.utils import configurationSetUp


def testPipeTransform():
    """
    Create a new pipe transform:

      >>> transform = PipeTransform()

    Set up some test text and turn it into a iterator:

      >>> data = iter(u"Some simple test text.")

    Try to transform the data:

      >>> result = transform.transform(data)
      >>> result is None
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.pipe'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
