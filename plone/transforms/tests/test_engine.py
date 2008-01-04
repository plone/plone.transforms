# -*- coding: UTF-8 -*-
"""
    Transform engine tests.
"""

import unittest

from zope.component import getGlobalSiteManager
from zope.component import queryUtility
from zope.component.testing import tearDown
from zope.interface import implements
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

from plone.transforms.engine import ConfigurableTransformEngine
from plone.transforms.interfaces import IRankedTransform
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformEngine
from plone.transforms.transform import Transform

from plone.transforms.tests.utils import configurationSetUp


class IAmFirstTransform(Transform):

    implements(IRankedTransform)

    name = u'IAmFirstTransform'
    rank = -10

    inputs = ('foo', )
    output = 'bar'


class IAmSecondTransform(Transform):

    implements(IRankedTransform)

    name = u'IAmSecondTransform'
    rank = 10

    inputs = ('foo', )
    output = 'bar'


class OptionsTransform(Transform):

    name = u'OptionsTransform'

    inputs = ('spam', )
    output = 'spam/options'

    def transform(self, data, options=None):
        result = super(OptionsTransform, self).transform(data, options=options)
        if options is not None:
            data = u''.join(result.data)
            data += u', '.join(['[%s : %s]' % (k,v) for k,v in options.items()])
            result.data = iter(data)
        return result


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

    Now try with a configurable engine:

      >>> engine = ConfigurableTransformEngine()
      >>> engine
      <ConfigurableTransformEngine object at ...>

    Try to transform the data:

      >>> result = engine.transform(data, None, None)
      >>> result is None
      True
    """


def testAvailableTransforms():
    """
    Get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

      >>> avail = engine.available_transforms()
      >>> unavail = engine.unavailable_transforms()

      >>> len(avail) + len(unavail) >= 60
      True

    Now try with a configurable engine:

      >>> engine = ConfigurableTransformEngine()
      >>> engine
      <ConfigurableTransformEngine object at ...>

      >>> avail = engine.available_transforms()
      >>> unavail = engine.unavailable_transforms()

      >>> len(avail) + len(unavail)
      0
    """


def testTransformPaths():
    """
    Get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

      >>> engine.find_transform(None, None)
      <plone.transforms.identity.IdentityTransform object at ...>

      >>> engine.find_transform('text/html', 'text/plain')
      <plone.transforms.text.html_text.HtmlToTextTransform object at ...>

    Now try with a configurable engine:

      >>> engine = ConfigurableTransformEngine()
      >>> engine
      <ConfigurableTransformEngine object at ...>

      >>> engine.find_transform(None, None) is None
      True

      >>> engine.find_transform('application/pdf', 'text/html') is None
      True
    """

def testConfigurableTransformEngine():
    """
    Create a configurable engine:

      >>> engine = ConfigurableTransformEngine()
      >>> engine
      <ConfigurableTransformEngine object at ...>

      >>> engine.available_transforms()
      []

      >>> engine.append(('plone.transforms.interfaces.ITransform',
      ...                'plone.transforms.identity.IdentityTransform'))

      >>> engine.available_transforms()
      [(None, None, <plone.transforms.identity.IdentityTransform object at ...>)]

      >>> engine.find_transform(None, None)
      <plone.transforms.identity.IdentityTransform object at ...>

      >>> engine.pop()
      ('...ITransform', 'plone.transforms.identity.IdentityTransform')

      >>> engine.available_transforms()
      []
    """

def testTransformOrder():
    """
    Get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

    Register our two new test transforms:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(IAmFirstTransform(),
      ...     ITransform,
      ...     name='IAmFirstTransform')

      >>> gsm.registerUtility(IAmSecondTransform(),
      ...     ITransform,
      ...     name='IAmSecondTransform')

    Check the rank of the two transforms:

      >>> first = queryUtility(ITransform,
      ...                      name='IAmFirstTransform')
      >>> first.rank
      -10

      >>> second = queryUtility(ITransform,
      ...                       name='IAmSecondTransform')
      >>> second.rank
      10

    Check that the first transform is found first:

      >>> engine.find_transform('foo', 'bar')
      <plone.transforms.tests.test_engine.IAmFirstTransform object at ...>

    Change the first transforms rank and see if the second is found now:

      >>> first.rank = 20

      >>> engine.find_transform('foo', 'bar')
      <plone.transforms.tests.test_engine.IAmSecondTransform object at ...>

    Restore the rank:

      >>> first.rank = -10

    Create a configurable engine:

      >>> engine = ConfigurableTransformEngine()
      >>> engine
      <ConfigurableTransformEngine object at ...>

    Check that we don't find any transform at first:

      >>> engine.find_transform('foo', 'bar') is None
      True

    Put in the two test transforms:

      >>> engine.append(('plone.transforms.interfaces.ITransform',
      ...                'IAmFirstTransform'))
      >>> engine.append(('plone.transforms.interfaces.ITransform',
      ...                'IAmSecondTransform'))

    Check that we get the first transform:

      >>> engine.find_transform('foo', 'bar')
      <plone.transforms.tests.test_engine.IAmFirstTransform object at ...>

    Change the first transform's rank and make sure that this doesn't change
    anything:

      >>> first.rank = 20

      >>> engine.find_transform('foo', 'bar')
      <plone.transforms.tests.test_engine.IAmFirstTransform object at ...>

    Restore the first rank and reverse the transforms in the engine:

      >>> first.rank = -10
      >>> engine.reverse()

    Now the second transform should be found:

      >>> engine[0]
      ('plone.transforms.interfaces.ITransform', 'IAmSecondTransform')

      >>> engine.find_transform('foo', 'bar')
      <plone.transforms.tests.test_engine.IAmSecondTransform object at ...>
    """

def testTransformOptions():
    """
    Get the global transform engine:

      >>> engine = queryUtility(ITransformEngine)
      >>> engine
      <plone.transforms.engine.TransformEngine object at ...>

    Register our new test transform:

      >>> gsm = getGlobalSiteManager()
      >>> gsm.registerUtility(OptionsTransform(),
      ...     ITransform,
      ...     name='OptionsTransform')

      >>> engine.find_transform('spam', 'spam/options')
      <plone.transforms.tests.test_engine.OptionsTransform object at ...>

      >>> result = engine.transform(iter(u'origtext'), 'spam', 'spam/options',
      ...                           options=dict(foo='bar'))

    Our transform should have preserved the original data:

      >>> data = u''.join(result.data)
      >>> data.startswith(u'origtext')
      True

    And it should also have put all passed in options at the end:

      >>> u'[foo : bar]' in data
      True

    As well as the two default options put in by the engine itself:

      >>> u'[input_mimetype : spam]' in data
      True

      >>> u'[output_mimetype : spam/options]' in data
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.engine'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
