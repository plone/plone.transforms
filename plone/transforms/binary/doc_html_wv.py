from zope.interface import implements

from plone.transforms.command import CommandTransform
from plone.transforms.interfaces import ICommandTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.utils import html_bodyfinder


class DocHtmlWvCommandTransform(CommandTransform):
    """A transform which transforms doc into HTML including the images
    as subobjects.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICommandTransform, DocHtmlWvCommandTransform)
      True
    """

    implements(ICommandTransform)

    name = u'plone.transforms.binary.doc_html_wv.DocHtmlWvCommandTransform'

    title = _(u'title_doc_html_wv_transform',
        default=u'DOC to HTML transform including images.')

    description = _(u'description_doc_html_wv_transform',
        default=u"A transform which transforms a DOC into HTML and "
                 "provides the images as subobjects.")

    inputs  = ("application/msword",)
    output = "text/html"

    command = 'wvHtml'
    args = "%(infile)s %(infile)s.html --charset=utf-8"

    def transform(self, data):
        """Returns the transform result.
        """
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.html')
        text = ''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(html_bodyfinder(text))
        return result
