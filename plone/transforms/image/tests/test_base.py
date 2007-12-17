# -*- coding: UTF-8 -*-
"""
    Basic PIL transform tests.
"""

import unittest

from plone.transforms.image.pil import HAS_PIL

from plone.transforms.image.bmp import BmpTransform
from plone.transforms.image.gif import GifTransform
from plone.transforms.image.jpeg import JpegTransform
from plone.transforms.image.pcx import PcxTransform
from plone.transforms.image.png import PngTransform
from plone.transforms.image.ppm import PpmTransform
from plone.transforms.image.tiff import TiffTransform

from plone.transforms.image.tests.base import input_file_path
from plone.transforms.image.tests.base import PILTransformTestCase

from plone.transforms.interfaces import IPILTransform


TRANSFORMS = [
    dict(name='plone.transforms.image.bmp.BmpTransform',
         class_=BmpTransform,
         output='BMP',
        ),
    dict(name='plone.transforms.image.gif.GifTransform',
         class_=GifTransform,
         output='GIF',
        ),
    dict(name='plone.transforms.image.jpeg.JpegTransform',
         class_=JpegTransform,
         output='JPEG',
        ),
    dict(name='plone.transforms.image.pcx.PcxTransform',
         class_=PcxTransform,
         output='PCX',
        ),
    dict(name='plone.transforms.image.png.PngTransform',
         class_=PngTransform,
         output='PNG',
        ),
    dict(name='plone.transforms.image.ppm.PpmTransform',
         class_=PpmTransform,
         output='PPM',
        ),
    dict(name='plone.transforms.image.tiff.TiffTransform',
         class_=TiffTransform,
         output='TIFF',
        ),
]

if not HAS_PIL:
    TRANSFORMS = []

tests = []
for transform in TRANSFORMS:

    class PILTransformTest(PILTransformTestCase):

        name = transform['name']
        class_ = transform['class_']
        interface = IPILTransform
        inputfiles = [input_file_path('logo.' + e) for e in
                      'bmp', 'gif', 'jpg', 'pcx', 'png', 'ppm', 'tiff']
        output = transform['output']

    tests.append(PILTransformTest)

    class PILSizedTransformTest(PILTransformTestCase):

        name = transform['name']
        class_ = transform['class_']
        interface = IPILTransform
        inputfiles = [input_file_path('logo.' + e) for e in
                      'bmp', 'gif', 'jpg', 'pcx', 'png', 'ppm', 'tiff']
        output = transform['output']
        options = dict(width=10, height=9)

    tests.append(PILSizedTransformTest)


def test_suite():
    suite = unittest.TestSuite()
    if HAS_PIL:
        for test in tests:
            suite.addTest(unittest.makeSuite(test))
    return suite
