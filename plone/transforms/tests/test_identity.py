# -*- coding: UTF-8 -*-
"""
    Tests for the identity transform.
"""

import unittest

from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.utils import configurationSetUp


def testIdentityTransform():
    """
    Let's make sure that this implementation actually fulfills the API.

      >>> from plone.transforms.interfaces import ITransform
      >>> from plone.transforms.identity import IdentityTransform

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, IdentityTransform)
      True

    First we get the transform utility.

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.identity.IdentityTransform')
      >>> util
      <plone.transforms.identity.IdentityTransform object at ...>

    Set up some test text and turn it into a iterator which fullfils the
    iterator protocol:

      >>> data = iter(u'Some simple test text.')

    Now transform the data:

      >>> result = util.transform(data)
      >>> result = result.data

    Check that we get back an object implementing the iterator protocol:

      >>> hasattr(result, 'next')
      True

      >>> hasattr(result, '__iter__')
      True

    In this case we got a iterator:

      >>> result
      <iterator object at ...>

    And make sure we got back the identical text:

      >>> u''.join(result)
      u'Some simple test text.'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
