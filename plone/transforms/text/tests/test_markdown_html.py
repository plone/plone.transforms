# -*- coding: UTF-8 -*-
"""
    Tests for the markdown transform.
"""

from unittest import TestSuite, makeSuite

from zope.testing.doctestunit import DocTestSuite

from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.markdown_html import MarkdownTransform


class MarkdownTransformTest(TransformTestCase):

    name = 'plone.transforms.text.markdown_html.MarkdownTransform'
    class_ = MarkdownTransform
    input_ = iter(u"Some simple test text.")
    output = u'\n<p>Some simple test text.\n</p>'


def test_suite():
    suite = TestSuite()
    suite.addTest(DocTestSuite('plone.transforms.text.markdown_html'))
    suite.addTest(makeSuite(MarkdownTransformTest))
    return suite
