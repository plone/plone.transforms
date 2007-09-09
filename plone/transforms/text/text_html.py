from zope.interface import implements

from plone.transforms.interfaces import IRankedTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

HAS_TEXT = True
try:
    # TODO Use a different quoting method, to avoid a dependency here
    from DocumentTemplate.DT_Util import html_quote
except ImportError:
    HAS_TEXT = False


class TextHtmlTransform(Transform):
    """A transform which transforms plain text into HTML."""

    implements(IRankedTransform)

    title = _(u'title_text_html_transform',
        default=u'Plain text to HTML transform')

    inputs = ("text/plain", )
    output = "text/html"

    available = False

    rank = 50

    def __init__(self):
        super(TextHtmlTransform, self).__init__()
        if HAS_TEXT:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = html_quote(u''.join(data).strip())
        html = '<p>%s</p>' % html.replace('\n', '<br />')
        return TransformResult(StringIter(html))


class TextPreHtmlTransform(Transform):
    """A transform which transforms plain text into HTML."""

    implements(IRankedTransform)

    title = _(u'title_text_pre_html_transform',
        default=u'Plain text to HTML transform using the pre tag')

    inputs = ("text/plain", )
    output = "text/html"

    available = False

    rank = 100

    def __init__(self):
        super(TextPreHtmlTransform, self).__init__()
        if HAS_TEXT:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = '<pre class="data">%s</pre>' % html_quote(u''.join(data))
        return TransformResult(StringIter(html))
