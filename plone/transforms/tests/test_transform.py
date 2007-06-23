# -*- coding: UTF-8 -*-
"""
    Transform tests.
"""

import unittest

import zope.component
from zope.component import getGlobalSiteManager
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.interfaces import IMultipleOutputTransform
from plone.transforms.transform import MultipleOutputTransform


class TestTransform(MultipleOutputTransform):

    name = u"TestTransform"
    title = u"Test transform."


class SplitTransform(MultipleOutputTransform):

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
        return {'default' : first, 'second' : second}


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.transforms)()


def testEmptyTransform():
    """
    First we create and register a new transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(TestTransform(),
      ...     IMultipleOutputTransform,
      ...     name='TestTransform')

      >>> util = queryUtility(IMultipleOutputTransform,
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
      {'default': <generator object at ...}

      >>> default = result.get('default')
      >>> u''.join(default) == text
      True
    """


def testSplitTransform():
    """
    First we load a new transform:

      >>> XMLConfig('configure.zcml', plone.transforms.tests)()

      >>> util = queryUtility(IMultipleOutputTransform,
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
      {'default': <generator object at ...>, 'second': <generator object at ...}

      >>> default = result.get('default')
      >>> u''.join(default)
      u'ACEGI'

      >>> second = result.get('second')
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
