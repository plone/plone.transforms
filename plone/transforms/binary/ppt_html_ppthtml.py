from plone.transforms.command import CommandTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.utils import html_bodyfinder


class PptHtmlPpthtmlCommandTransform(CommandTransform):
    """A transform which transforms ppt into HTML including the images
    as subobjects.
    """

    title = _(u'title_ppt_html_ppthtml_transform',
        default=u'PPT to HTML transform.')

    inputs = ("application/powerpoint", "application/vnd.ms-powerpoint", )
    output = "text/html"

    command = 'ppthtml'
    args = "%(infile)s >%(infile)s.html"

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        result = self.prepare_transform(data, infile_data_suffix='.html')
        text = ''.join(result.data).decode('utf-8', 'ignore')
        result.data = StringIter(html_bodyfinder(text))
        return result
