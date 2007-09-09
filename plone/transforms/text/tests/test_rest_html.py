# -*- coding: UTF-8 -*-
"""
    Tests for the rest transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.rest_html import RestHtmlTransform, HAS_REST


class RestHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.rest_html.RestHtmlTransform'
    class_ = RestHtmlTransform
    interface = ITransform
    input_ = iter(u'*hello world*')
    output = u'<p><em>hello world</em></p>'


def test_suite():
    suite = TestSuite()
    if HAS_REST:
        suite.addTest(makeSuite(RestHtmlTransformTest))
    return suite
