# -*- coding: UTF-8 -*-
"""
    Transform engine tests.
"""

import unittest

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.interfaces import ITransformEngine

from plone.transforms.tests.utils import configurationSetUp


def testTransformEngineInstallation():
    """
    Try to get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

    Set up some test text and turn it into a iterator:

      >>> data = iter(u"Some simple test text.")

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
