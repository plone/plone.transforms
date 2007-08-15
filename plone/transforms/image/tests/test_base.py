# -*- coding: UTF-8 -*-
"""
    Basic PIL transform tests.
"""

import unittest

from zope.testing.doctestunit import DocTestSuite

modules = [
    'plone.transforms.image.bmp',
    'plone.transforms.image.gif',
    'plone.transforms.image.jpeg',
    'plone.transforms.image.pcx',
    'plone.transforms.image.png',
    'plone.transforms.image.ppm',
    'plone.transforms.image.tiff',
]

def test_suite():
    return unittest.TestSuite(
        [DocTestSuite(module=module) for module in modules]
        )
