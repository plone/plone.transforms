# -*- coding: UTF-8 -*-
"""
    Tests for the textile transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.textile_html import TextileTransform, HAS_TEXTILE


class TextileTransformTest(TransformTestCase):

    name = 'plone.transforms.text.textile_html.TextileTransform'
    class_ = TextileTransform
    interface = ITransform
    input_ = iter(u"""h1. Textile test text

_This_ is quite *boring*, but it needs to be "done":http://plone.org, right?

h2. Cheeses

# Gouda
# Roquefort
# Emmentaler
""")
    output = u"""<h1>Textile test text</h1>

<p><em>This</em> is quite <strong>boring</strong>, but it needs to be <a href="http://plone.org">done</a>, right?</p>

<h2>Cheeses</h2>

<ol>
<li>Gouda</li>
<li>Roquefort</li>
<li>Emmentaler</li>
</ol>"""


def test_suite():
    suite = TestSuite()
    if HAS_TEXTILE:
        suite.addTest(makeSuite(TextileTransformTest))
    return suite
