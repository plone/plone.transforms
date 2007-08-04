from zope.interface import implements

from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import ICommandTransform
from plone.transforms.interfaces import IPipeTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.transform import TransformResult
from plone.transforms.utils import html_bodyfinder


class PDFCommandTransform(CommandTransform):
    """A transform which transforms pdf into HTML including the images
    as subobjects.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICommandTransform, PDFCommandTransform)
      True
    """

    implements(ICommandTransform)

    name = u'plone.transforms.binary.pdf_html.PDFPipeTransform'

    title = _(u'title_pdf_html_transform',
        default=u'PDF to HTML transform including images.')

    description = _(u'description_pdf_html_transform',
        default=u"A transform which transforms a PDF into HTML and "
                 "provides the images as subobjects.")

    inputs  = ("application/pdf",)
    output = "text/html"

    command = 'pdftohtml'
    args = "%(infile)s -q -c -noframes -enc UTF-8"

    def transform(self, data):
        """Prepare the transform result and hand back everything as subobjects.
        You can then pick the default content from the result object and put
        it into the default data.
        """
        result = self.prepare_transform(data)
        htmls = [f for f in result.subobjects.keys() if f.endswith('html')]
        html = htmls[0]
        text = ''.join(result.subobjects[html]).decode('utf-8', 'ignore')
        del result.subobjects[html]
        result.data = iter(html_bodyfinder(text))
        return result


class PDFPipeTransform(PipeTransform):
    """A transform which transforms pdf into HTML.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPipeTransform, PDFPipeTransform)
      True
    """

    implements(IPipeTransform)

    name = u'plone.transforms.binary.pdf_html.PDFPipeTransform'

    title = _(u'title_pdf_html_transform',
        default=u'PDF to HTML only transform')

    description = _(u'description_pdf_html_transform',
        default=u"A transform which transforms a PDF into HTML.")

    inputs  = ("application/pdf",)
    output = "text/html"

    command = 'pdftohtml'
    args = "%(infile)s -q -noframes -stdout -enc UTF-8"
    use_stdin = False

    def extractOutput(self, stdout):
        return html_bodyfinder(stdout.read()).decode('utf-8', 'ignore')
