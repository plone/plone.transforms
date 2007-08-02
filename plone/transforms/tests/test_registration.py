# -*- coding: UTF-8 -*-
"""
    Transform registration tests.
"""

import unittest

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

import plone.transforms
from plone.transforms.interfaces import ILocalEngineRegistration


def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.transforms)()


def testLocalEngineRegistration():
    """
    Make a new local engine registration:

      >>> from plone.transforms.registration import LocalEngineRegistration

      >>> interface_name = 'plone.transforms.interfaces.ILocalEngineRegistration'

      >>> registration = LocalEngineRegistration(interface_name)

      >>> registration
      <plone.transforms.registration.LocalEngineRegistration object at ...>

      >>> registration.interface_name is interface_name
      True
    """


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.registration'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | 
                                 doctest.NORMALIZE_WHITESPACE),
        ))
