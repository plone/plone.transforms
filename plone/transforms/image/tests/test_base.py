# -*- coding: UTF-8 -*-
"""
    Basic PIL transform tests.
"""

import unittest

from zope.testing.doctestunit import DocTestSuite

from plone.transforms.image.bmp import BmpTransform
from plone.transforms.image.gif import GifTransform
from plone.transforms.image.jpeg import JpegTransform
from plone.transforms.image.pcx import PcxTransform
from plone.transforms.image.png import PngTransform
from plone.transforms.image.ppm import PpmTransform
from plone.transforms.image.tiff import TiffTransform

from plone.transforms.image.tests.base import input_file_path
from plone.transforms.image.tests.base import PILTransformTestCase

MODULES = [
    'plone.transforms.image.bmp',
    'plone.transforms.image.gif',
    'plone.transforms.image.jpeg',
    'plone.transforms.image.pcx',
    'plone.transforms.image.pil',
    'plone.transforms.image.png',
    'plone.transforms.image.ppm',
    'plone.transforms.image.tiff',
]

TRANSFORMS = [
    dict(name='plone.transforms.image.bmp.BmpTransform',
         class_=BmpTransform,
         output='BM'
        ),
    dict(name='plone.transforms.image.gif.GifTransform',
         class_=GifTransform,
         output='GIF87a\x18'
        ),
    dict(name='plone.transforms.image.jpeg.JpegTransform',
         class_=JpegTransform,
         output='\xff\xd8\xff\xe0\x00\x10JFIF'
        ),
    dict(name='plone.transforms.image.pcx.PcxTransform',
         class_=PcxTransform,
         output='\n\x05\x01\x08\x00\x00\x00\x00\x17\x00'
        ),
    dict(name='plone.transforms.image.png.PngTransform',
         class_=PngTransform,
         output='\x89PNG\r\n\x1a\n\x00\x00'
        ),
    dict(name='plone.transforms.image.ppm.PpmTransform',
         class_=PpmTransform,
         output='P6\n24 23\n2'
        ),
    dict(name='plone.transforms.image.tiff.TiffTransform',
         class_=TiffTransform,
         output='II*\x00\x08\x00\x00\x00\t\x00'
        ),
]

tests = []
for transform in TRANSFORMS:

    class PILTransformTest(PILTransformTestCase):

        name = transform['name']
        class_ = transform['class_']
        inputfiles = [input_file_path('logo.' + e) for e in
                      'bmp', 'gif', 'jpg', 'pcx', 'png', 'ppm', 'tiff']
        output = transform['output']

    tests.append(PILTransformTest)


def test_suite():
    suite = unittest.TestSuite()
    for module in MODULES:
        suite.addTest(DocTestSuite(module=module))
    for test in tests:
        suite.addTest(unittest.makeSuite(test))
    return suite
