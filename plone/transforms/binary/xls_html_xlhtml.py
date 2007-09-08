from zope.interface import implements

from plone.transforms.interfaces import IPipeTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.stringiter import StringIter


class XlsHtmlXlhtmlCommandTransform(PipeTransform):
    """A transform which transforms xls into HTML."""

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

    def transform(self, data, options=None):
        """Returns the transform result.
        """
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.html')
        text = u''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result
