# -*- coding: UTF-8 -*-
"""
    Tests for the Python HTML transform.
"""

from unittest import TestSuite, makeSuite

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.tests.base import input_file_path
from plone.transforms.text.python_html import PythonHtmlTransform

try:
    test = file(input_file_path(__file__, 'test_python_html.py'))
    TEST_TEXT = unicode(test.read(), 'ascii', 'ignore')
finally:
    test.close()


class PythonHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.python_html.PythonHtmlTransform'
    class_ = PythonHtmlTransform
    interface = ITransform
    input_ = iter(TEST_TEXT)
    output = u'''<pre><tt><span style="font-style: italic"><span style="color: #9A1900"># -*- coding: UTF-8 -*-</span></span>

<span style="font-weight: bold"><span style="color: #000080">from</span></span> plone<span style="color: #990000">.</span>transforms<span style="color: #990000">.</span>interfaces <span style="font-weight: bold"><span style="color: #000080">import</span></span> <span style="color: #009900">ITransform</span>
'''


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(PythonHtmlTransformTest))
    return suite
