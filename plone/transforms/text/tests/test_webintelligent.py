# -*- coding: UTF-8 -*-
"""
    Tests for the web-intelligent transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.web_intelligent import HtmlWebIntelligentTransform
from plone.transforms.text.web_intelligent import WebIntelligentHtmlTransform
from plone.transforms.text.web_intelligent import HAS_WEB_INTELLIGENTTEXT


class HtmlWebIntelligentTransformTest(TransformTestCase):

    name = 'plone.transforms.text.web_intelligent.HtmlWebIntelligentTransform'
    class_ = HtmlWebIntelligentTransform
    interface = ITransform
    input_ = iter(u"<b>Some simple & test text.</b>")
    output = u'Some simple & test text.'


class WebIntelligentHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.web_intelligent.WebIntelligentHtmlTransform'
    class_ = WebIntelligentHtmlTransform
    interface = ITransform
    input_ = iter(u"Some simple & test text.")
    output = u'Some simple &amp; test text.'


def test_suite():
    suite = TestSuite()
    if HAS_WEB_INTELLIGENTTEXT:
        suite.addTest(makeSuite(HtmlWebIntelligentTransformTest))
        suite.addTest(makeSuite(WebIntelligentHtmlTransformTest))
    return suite
