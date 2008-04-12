import re

from zope.interface import implements

from plone.transforms.chain import PersistentTransformChain
from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import IRankedTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.stringiter import StringIter
from plone.transforms.utils import html_bodyfinder

REGEXES = (
    (re.compile('((left|top|right|bottom)[ \t]*:[ \t]*[0-9]+)[ \t]*([;"])'),
     r"\1px\3"
    ),
)


class PDFCommandTransform(CommandTransform):
    """A transform which transforms pdf into HTML including the images
    as subobjects."""

    implements(IRankedTransform)

    title = _(u'title_pdf_html_transform',
        default=u'PDF to HTML transform including images.')

    inputs = ("application/pdf", )
    output = "text/html"

    command = 'pdftohtml'
    args = "%(infile)s -q -c -noframes -enc UTF-8 %(dev)s"
    dev = 'png16m'

    rank = 50

    def fixBrokenStyles(self, html):
        for rex, subtxt in REGEXES:
            html = rex.sub(subtxt, html)
        return html

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        dev = self.dev
        if options is not None:
            dev = options.get('output_image_format', self.dev)

        arguments = {
            'infile_data_suffix' : '.html',
            'dev' : '-dev %s' % dev
            }

        result = self.prepare_transform(data, arguments=arguments)
        if result.data is None:
            return None

        text = ''.join(result.data).decode('utf-8', 'ignore')
        # workaround because of bug in pdftohtml
        text = self.fixBrokenStyles(text)
        result.data = StringIter(html_bodyfinder(text))
        return result


class PDFPipeTransform(PipeTransform):
    """A transform which transforms pdf into HTML."""

    implements(IRankedTransform)

    title = _(u'title_pdf_html_transform',
        default=u'PDF to HTML only transform')

    inputs = ("application/pdf", )
    output = "text/html"

    command = 'pdftohtml'
    args = "%(infile)s -q -noframes -stdout -enc UTF-8"
    use_stdin = False

    rank = 100

    def extract_output(self, stdout):
        return StringIter(html_bodyfinder(stdout.read()).decode('utf-8', 'ignore'))


class PDFTextTransform(PersistentTransformChain):
    """A transform chain which transforms pdf into text."""

    title = _(u'title_pdf_text_transform',
        default=u'PDF to Text only transform')

    def __init__(self):
        super(PDFTextTransform, self).__init__()
        self.append(('plone.transforms.interfaces.IPipeTransform',
                     u'plone.transforms.binary.pdf_html.PDFPipeTransform'))
        self.append(('plone.transforms.interfaces.ITransform',
                     u'plone.transforms.text.html_text.HtmlToTextTransform'))
