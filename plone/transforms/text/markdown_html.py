"""
Uses the http://www.freewisdom.org/projects/python-markdown/ module to do its
handy work

Based on work from: Tom Lazar <tom@tomster.org> at the archipelago sprint 2006.
"""
from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

HAS_MARKDOWN = True
try:
    from markdown import markdown
except ImportError:
    HAS_MARKDOWN = False


class MarkdownTransform(Transform):
    """A transform which transforms markdown text into HTML."""

    implements(ITransform)

    name = u'plone.transforms.text.markdown_html.MarkdownTransform'

    title = _(u'title_markdown_transform',
        default=u'Markdown to HTML transform')

    description = _(u'description_markdown_transform',
        default=u"A transform which transforms any markdown text into HTML.")

    inputs  = ("text/x-web-markdown",)
    output = "text/html"

    available = False

    def __init__(self):
        super(Transform, self).__init__()
        if HAS_MARKDOWN:
            self.available = True

    def transform(self, data):
        """Returns the transform result."""
        if self._validate(data) is None:
            return None

        html = markdown(u''.join(data).encode('utf-8'))
        return TransformResult(StringIter(html))
