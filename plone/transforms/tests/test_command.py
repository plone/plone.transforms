# -*- coding: UTF-8 -*-
"""
    Command transform tests.
"""

import unittest

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import ICommandTransform

from plone.transforms.tests.utils import configurationSetUp


def testCommandTransform():
    """
    Create a new command transform:

      >>> command = CommandTransform()

    Set up some test text and turn it into a iterator:

      >>> data = iter(u"Some simple test text.")

    Try to transform the data:

      >>> result = command.transform(data)
      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

      >>> 'None: command not found' in u''.join(result.data)
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.command'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))