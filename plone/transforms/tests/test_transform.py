# -*- coding: UTF-8 -*-
"""
    Transform tests.
"""

import unittest

from zope.testing.doctestunit import DocTestSuite

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.transforms.transform'),
        ))
