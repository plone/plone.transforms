# -*- coding: UTF-8 -*-
"""
    Tests for the text plain transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.text_html import TextHtmlTransform
from plone.transforms.text.text_html import TextPreHtmlTransform


class TextHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.text_html.TextHtmlTransform'
    class_ = TextHtmlTransform
    interface = ITransform
    input_ = iter(u'hello\nworld')
    output = u'<p>hello<br />world</p>'


class TextPreHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.text_html.TextPreHtmlTransform'
    class_ = TextPreHtmlTransform
    interface = ITransform
    input_ = iter(u'hello\nworld')
    output = u'<pre class="data">hello\nworld</pre>'


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TextHtmlTransformTest))
    suite.addTest(makeSuite(TextPreHtmlTransformTest))
    return suite
