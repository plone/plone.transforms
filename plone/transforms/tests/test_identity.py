# -*- coding: UTF-8 -*-
"""
    Tests for the identity transform.
"""

import unittest

import plone.transforms
from plone.transforms.interfaces import ITransform

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.transforms)()

def testIdentityTransform():
    """
    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.identity.IdentityTransform')
      >>> util
      <plone.transforms.identity.IdentityTransform object at ...>

    Set up some test text and turn it into a generator which fullfils the
    iterator protocol:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Now transform the data:

      >>> result = util.transform(data)

    Check that we get back an object implementing the iterator protocol:

      >>> hasattr(result, 'next')
      True

      >>> hasattr(result, '__iter__')
      True

    In this case we got a generator:

      >>> result
      <generator object at ...>

    And make sure we got back the identical text:

      >>> u''.join(result) == text
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.identity'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
