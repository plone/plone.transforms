# -*- coding: UTF-8 -*-
"""
    Tests for the structured text transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.st_html import StructuredTextHtmlTransform, HAS_ST


class StructuredTextHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.st_html.StructuredTextHtmlTransform'
    class_ = StructuredTextHtmlTransform
    interface = ITransform
    input_ = iter(u'*hello world*')
    output = u'<p><em>hello world</em></p>'


def test_suite():
    suite = TestSuite()
    if HAS_ST:
        suite.addTest(makeSuite(StructuredTextHtmlTransformTest))
    return suite
