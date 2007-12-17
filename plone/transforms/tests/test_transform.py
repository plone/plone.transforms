# -*- coding: UTF-8 -*-
"""
    Transform tests.
"""

import unittest

from zope.component import getGlobalSiteManager
from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

from plone.transforms.tests.utils import configurationSetUp


class TestTransform(Transform):

    name = u"TestTransform"
    title = u"Test transform."


class TestPersistentTransform(PersistentTransform):

    name = u"TestPersistentTransform"
    title = u"Persistent test transform."


class SplitTransform(Transform):

    title = u"Splitting transform."

    def transform(self, data, options=None):
        first = []
        second = []
        while data:
            try:
                first.append(data.next())
                second.append(data.next())
            except StopIteration:
                break
        return TransformResult(iter(first),
                               subobjects=dict(second=iter(second)))


def testTransformResult():
    """
    Let's make sure that this implementation actually fulfills the API.

      >>> from plone.transforms.interfaces import ITransformResult

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformResult, TransformResult)
      True
    """


def testEmptyTransform():
    """
    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, Transform)
      True

    First we create and register a new transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(TestTransform(),
      ...     ITransform,
      ...     name='TestTransform')

      >>> util = queryUtility(ITransform,
      ...            name='TestTransform')
      >>> util
      <plone.transforms.tests.test_transform.TestTransform object at ...>

    Set up some test text and turn it into a iterator:

      >>> data = iter(u'Some simple test text.')

    Now transform the data:

      >>> result = util.transform(data)

    Check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

      >>> u''.join(result.data)
      u'Some simple test text.'
    """


def testEmptyPersistentTransform():
    """
    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, PersistentTransform)
      True

    First we create and register a new transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(TestPersistentTransform(),
      ...     ITransform,
      ...     name='TestPersistentTransform')

      >>> util = queryUtility(ITransform,
      ...            name='TestPersistentTransform')
      >>> util
      <plone.transforms.tests.test_transform.TestPersistentTransform object at ...>

    Set up some test text and turn it into a iterator:

      >>> data = iter(u'Some simple test text.')

    Now transform the data:

      >>> result = util.transform(data)

    Check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <iterator object at ...>

      >>> u''.join(result.data)
      u'Some simple test text.'
    """


def testSplitTransform():
    """
    First we load a new transform:

      >>> from zope.configuration.xmlconfig import XMLConfig
      >>> import plone.transforms.tests
      >>> XMLConfig('configure.zcml', plone.transforms.tests)()

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.tests.test_transform.SplitTransform')
      >>> util
      <plone.transforms.tests.test_transform.SplitTransform object at ...>

    Set up some test text and turn it into a iterator:

      >>> data = iter(u"ABCDEFGHI")

    Now transform the data:

      >>> result = util.transform(data)

    Check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> u''.join(result.data)
      u'ACEGI'

      >>> second = result.subobjects['second']
      >>> u''.join(second)
      u'BDFH'
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
