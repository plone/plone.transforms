# -*- coding: UTF-8 -*-
"""
    Tests for the doc transforms.
"""

import unittest

from plone.transforms.binary.doc_html_wv import DocHtmlWvCommandTransform
from plone.transforms.binary.doc_txt_wv import DocTxtWvCommandTransform

from plone.transforms.binary.tests.base import input_file_path
from plone.transforms.binary.tests.base import BinaryTransformTestCase

from plone.transforms.interfaces import ITransform


TRANSFORMS = [
    dict(name='plone.transforms.binary.doc_html_wv.DocHtmlWvCommandTransform',
         class_=DocHtmlWvCommandTransform,
         inputfile='test.doc',
         output=u""""""
        ),
    dict(name='plone.transforms.binary.doc_txt_wv.DocTxtWvCommandTransform',
         class_=DocTxtWvCommandTransform,
         inputfile='test.doc',
         output=u""""""
        ),
]

tests = []
for transform in TRANSFORMS:

    class BinaryTransformTest(BinaryTransformTestCase):

        name = transform['name']
        class_ = transform['class_']
        interface = ITransform
        inputfile = input_file_path(transform['inputfile'])
        output = transform['output']

    tests.append(BinaryTransformTest)


def test_suite():
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTest(unittest.makeSuite(test))
    return suite
