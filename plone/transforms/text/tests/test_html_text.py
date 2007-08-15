# -*- coding: UTF-8 -*-
"""
    Tests for the HTML to text transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.stringiter import StringIter
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.html_text import HtmlToTextTransform


class HtmlToTextTransformTest(TransformTestCase):

    name = 'plone.transforms.text.html_text.HtmlToTextTransform'
    class_ = HtmlToTextTransform
    interface = ITransform
    input_ = StringIter(unicode("\n<html><head><title>Stupid title</title>"
                                "</head><body><p>Some simple test text héhé.\n"
                                "</p>\n\n\n</body></html>", 'utf-8'))
    output = u'\n   Stupid title    Some simple test text h\xe9h\xe9.'


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(HtmlToTextTransformTest))
    return suite
