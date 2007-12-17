from cgi import escape

from zope.interface import implements

from plone.transforms.interfaces import IRankedTransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult


class TextHtmlTransform(Transform):
    """A transform which transforms plain text into HTML."""

    implements(IRankedTransform)

    title = _(u'title_text_html_transform',
        default=u'Plain text to HTML transform')

    inputs = ("text/plain", )
    output = "text/html"

    rank = 50

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = escape(u''.join(data).strip(), 1)
        html = '<p>%s</p>' % html.replace('\n', '<br />')
        return TransformResult(StringIter(html))


class TextPreHtmlTransform(Transform):
    """A transform which transforms plain text into HTML."""

    implements(IRankedTransform)

    title = _(u'title_text_pre_html_transform',
        default=u'Plain text to HTML transform using the pre tag')

    inputs = ("text/plain", )
    output = "text/html"

    rank = 100

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = '<pre class="data">%s</pre>' % escape(u''.join(data), 1)
        return TransformResult(StringIter(html))
