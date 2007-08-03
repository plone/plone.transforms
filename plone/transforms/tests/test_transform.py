# -*- coding: UTF-8 -*-
"""
    Transform tests.
"""

import unittest

import zope.app.publisher.browser
import zope.component
from zope.component import getGlobalSiteManager
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.interfaces import ITransform
from plone.transforms.transform import PersistentTransform
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult


class TestTransform(Transform):

    name = u"TestTransform"
    title = u"Test transform."


class TestPersistentTransform(PersistentTransform):

    name = u"TestPersistentTransform"
    title = u"Persistent test transform."


class SplitTransform(Transform):

    name = u"plone.transforms.test_transform.SplitTransform"
    title = u"Splitting transform."

    def transform(self, data):
        first = []
        second = []
        while data:
            try:
                first.append(data.next())
                second.append(data.next())
            except StopIteration:
                break
        first = (f for f in first)
        second = (s for s in second)
        result = TransformResult(first)
        result.subobjects['second'] = second
        return result


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.app.publisher.browser)()
    XMLConfig('configure.zcml', plone.transforms)()


def testEmptyTransform():
    """
    First we create and register a new transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(TestTransform(),
      ...     ITransform,
      ...     name='TestTransform')

      >>> util = queryUtility(ITransform,
      ...            name='TestTransform')
      >>> util
      <plone.transforms.tests.test_transform.TestTransform object at ...>

    Set up some test text and turn it into a generator:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Now transform the data:

      >>> result = util.transform(data)

    Check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <generator object at ...>

      >>> u''.join(result.data) == text
      True
    """


def testEmptyPersistentTransform():
    """
    First we create and register a new transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(TestPersistentTransform(),
      ...     ITransform,
      ...     name='TestPersistentTransform')

      >>> util = queryUtility(ITransform,
      ...            name='TestPersistentTransform')
      >>> util
      <plone.transforms.tests.test_transform.TestPersistentTransform object at ...>

    Set up some test text and turn it into a generator:

      >>> text = u"Some simple test text."
      >>> data = (chr for chr in text)

    Now transform the data:

      >>> result = util.transform(data)

    Check the result:

      >>> result
      <plone.transforms.transform.TransformResult object at ...>

      >>> result.data
      <generator object at ...>

      >>> u''.join(result.data) == text
      True
    """


def testSplitTransform():
    """
    First we load a new transform:

      >>> XMLConfig('configure.zcml', plone.transforms.tests)()

      >>> util = queryUtility(ITransform,
      ...            name='plone.transforms.test_transform.SplitTransform')
      >>> util
      <plone.transforms.tests.test_transform.SplitTransform object at ...>

    Set up some test text and turn it into a generator:

      >>> text = u"ABCDEFGHI"
      >>> data = (chr for chr in text)

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
        DocTestSuite('plone.transforms.transform'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
