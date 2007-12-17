# -*- coding: UTF-8 -*-

from plone.transforms.interfaces import ITransform
from plone.transforms.tests.base import TransformTestCase
from plone.transforms.text.python_html import PythonHtmlTransform


class PythonHtmlTransformTest(TransformTestCase):

    name = 'plone.transforms.text.python_html.PythonHtmlTransform'
    class_ = PythonHtmlTransform
    interface = ITransform
    input_ = iter('''foo''')
    output = u'bar'
