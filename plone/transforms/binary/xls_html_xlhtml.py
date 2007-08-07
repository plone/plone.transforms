from StringIO import StringIO

from zope.interface import implements

from plone.transforms.interfaces import IPipeTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform


class XlsHtmlXlhtmlCommandTransform(PipeTransform):
    """A transform which transforms xls into HTML.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IPipeTransform, XlsHtmlXlhtmlCommandTransform)
      True
    """

    implements(IPipeTransform)

    name = u'plone.transforms.binary.xls_html_xlhtml.XlsHtmlXlhtmlCommandTransform'

    title = _(u'title_xls_html_xlhtml_transform',
        default=u'Xls to HTML transform.')

    description = _(u'description_xls_html_xlhtml_transform',
        default=u"A transform which transforms a Xls into HTML.")

    inputs  = ("application/vnd.ms-excel","application/msexcel",)
    output = "text/html"

    command = 'xlhtml'
    args = "-nh %(infile)s > %(infile)s.html "

    def transform(self, data):
        """Returns the transform result.
        """
        result = self.prepare_transform(data, infile_data_suffix='.html')
        text = ''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIO(text)
        return result
