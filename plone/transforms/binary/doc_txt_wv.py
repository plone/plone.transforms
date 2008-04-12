from plone.transforms.command import CommandTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter


class DocTxtWvCommandTransform(CommandTransform):
    """A transform which transforms doc into Text."""

    title = _(u'title_doc_txt_wv_transform',
        default=u'DOC to Text transform.')

    inputs = ("application/msword", )
    output = "text/plain"

    command = 'wvText'
    args = "%(infile)s %(infile)s.text "

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        arguments = { 'infile_data_suffix' : '.text' }

        result = self.prepare_transform(data, arguments=arguments)
        text = u''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result
