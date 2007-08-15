# -*- coding: UTF-8 -*-
"""
    Tests for the HTML body extractor.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.stringiter import StringIter
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.html_body import HtmlBodyTransform


class HtmlBodyTransformTest(TransformTestCase):

    name = 'plone.transforms.text.html_body.HtmlBodyTransform'
    class_ = HtmlBodyTransform
    interface = ITransform
    input_ = StringIter(u"<html><head><title>Stupid title</title></head>"
                         "<body><p>Some simple test text.\n</p>"
                         "</body></html>")
    output = u'<p>Some simple test text.\n</p>'


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(HtmlBodyTransformTest))
    return suite
