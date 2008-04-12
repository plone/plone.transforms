from plone.transforms.command import CommandTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.utils import html_bodyfinder


class DocHtmlWvCommandTransform(CommandTransform):
    """A transform which transforms doc into HTML including the images
    as subobjects.
    """

    title = _(u'title_doc_html_wv_transform',
        default=u'DOC to HTML transform including images.')

    inputs = ("application/msword", )
    output = "text/html"

    command = 'wvHtml'
    args = "%(infile)s %(infile)s.html --charset=utf-8"

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        arguments = { 'infile_data_suffix' : '.html' }

        result = self.prepare_transform(data, arguments=arguments)
        text = ''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(html_bodyfinder(text))
        return result
