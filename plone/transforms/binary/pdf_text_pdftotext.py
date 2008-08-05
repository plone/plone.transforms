import re

from zope.interface import implements

from plone.transforms.chain import PersistentTransformChain
from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import IRankedTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.stringiter import StringIter

class PDFTextCommandTransform(CommandTransform):
    """A transform which transforms pdf into Text."""

    implements(IRankedTransform)

    title = _(u'title_pdf_text_transform',
        default=u'PDF to TEXT transform.')

    inputs = ("application/pdf", )
    output = "text/plain"

    command = 'pdftotext'
    args = "%(infile)s -q -layout -enc UTF-8"

    rank = 50

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.txt')
        text = ''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result
