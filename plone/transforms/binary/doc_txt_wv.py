from zope.interface import implements

from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import ICommandTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter


class DocTxtWvCommandTransform(CommandTransform):
    """A transform which transforms doc into Text.
    """

    implements(ICommandTransform)

    name = u'plone.transforms.binary.doc_txt_wv.DocTxtWvCommandTransform'

    title = _(u'title_doc_txt_wv_transform',
        default=u'DOC to Text transform.')

    description = _(u'description_doc_txt_wv_transform',
        default=u"A transform which transforms a DOC into Text.")

    inputs  = ("application/msword",)
    output = "text/plain"

    command = 'wvText'
    args = "%(infile)s %(infile)s.text "

    def transform(self, data, options=None):
        """Returns the transform result."""
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.text')
        text = u''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(text)
        return result
