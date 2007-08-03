# -*- coding: UTF-8 -*-
"""
    Command transform tests.
"""

import unittest

import zope.app.publisher.browser
import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import ICommandTransform


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.app.publisher.browser)()
    XMLConfig('configure.zcml', plone.transforms)()


def testCommandTransform():
    """
    Create a new command transform:

      >>> command = CommandTransform()

    Set up some test text and turn it into a generator:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Try to transform the data:

      >>> result = command.transform(data)
      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <generator object at ...>

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
