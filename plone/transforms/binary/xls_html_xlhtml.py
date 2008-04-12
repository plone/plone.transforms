from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.pipe import PipeTransform
from plone.transforms.stringiter import StringIter


class XlsHtmlXlhtmlCommandTransform(PipeTransform):
    """A transform which transforms xls into HTML."""

    title = _(u'title_xls_html_xlhtml_transform',
        default=u'Xls to HTML transform.')

    inputs = ("application/vnd.ms-excel", "application/msexcel", )
    output = "text/html"

    command = 'xlhtml'
    args = "-nh %(infile)s > %(infile)s.html "

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        arguments = { 'infile_data_suffix' : '.html' }

        result = self.prepare_transform(data, arguments=arguments)
        text = u''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result
