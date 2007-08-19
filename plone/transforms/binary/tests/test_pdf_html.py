# -*- coding: UTF-8 -*-
"""
    Tests for the pdf to html transform.
"""

import unittest

from plone.transforms.binary.pdf_html import PDFCommandTransform
from plone.transforms.binary.pdf_html import PDFPipeTransform
from plone.transforms.binary.pdf_html import PDFTextTransform

from plone.transforms.binary.tests.base import input_file_path
from plone.transforms.binary.tests.base import BinaryTransformTestCase

from plone.transforms.interfaces import ITransform


TRANSFORMS = [
    dict(name='plone.transforms.binary.pdf_html.PDFCommandTransform',
         class_=PDFCommandTransform,
         inputfile='test_pdf_html_complex.pdf',
         output=u"""
<!-- Page 1 -->\n<a name="1"></a>
<DIV style="position:relative;width:1200;height:900;">
<STYLE type="text/css">\n<!--\n-->\n</STYLE>
"""
        ),
    dict(name='plone.transforms.binary.pdf_html.PDFPipeTransform',
         class_=PDFPipeTransform,
         inputfile='test_pdf_html.pdf',
         output=u"""\n<A name=1></a>test_pdf_html.py<br>\n2007-08-03<br>
# -*- coding: UTF-8 -*-<br>&quot;&quot;&quot;<br>    Tests for the pdf to html transform.<br>&quot;&quot;&quot;<br>
"""
        ),
    dict(name='plone.transforms.binary.pdf_html.PDFTextTransform',
         class_=PDFTextTransform,
         inputfile='test_pdf_html.pdf',
         output=u"""
  test_pdf_html.py \n2007-08-03 
# -*- coding: UTF-8 -*- &quot;&quot;&quot;     Tests for the pdf to html transform. &quot;&quot;&quot;"""
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
