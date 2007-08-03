# -*- coding: UTF-8 -*-
"""
    Transform engine tests.
"""

import unittest

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.interfaces import ITransformEngine


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.transforms)()


def testTransformEngineInstallation():
    """
    Try to get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

    Set up some test text and turn it into a generator:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Try to transform the data:

      >>> result = engine.transform(data, None, None)
      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> u''.join(result.data)
      u'Some simple test text.'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.engine'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
