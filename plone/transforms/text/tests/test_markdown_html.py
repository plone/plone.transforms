# -*- coding: UTF-8 -*-
"""
    Tests for the markdown transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.markdown_html import MarkdownTransform, HAS_MARKDOWN


class MarkdownTransformTest(TransformTestCase):

    name = 'plone.transforms.text.markdown_html.MarkdownTransform'
    class_ = MarkdownTransform
    interface = ITransform
    input_ = iter(u"Some simple test text.")
    output = u'\n<p>Some simple test text.\n</p>'


def test_suite():
    suite = TestSuite()
    if HAS_MARKDOWN:
        suite.addTest(makeSuite(MarkdownTransformTest))
    return suite
