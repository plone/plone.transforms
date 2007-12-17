from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

HAS_WEB_INTELLIGENTTEXT = True
try:
    from plone.intelligenttext.transforms import (
        convertWebIntelligentPlainTextToHtml,
        convertHtmlToWebIntelligentPlainText)
except ImportError:
    HAS_WEB_INTELLIGENTTEXT = False


class WebIntelligentHtmlTransform(Transform):
    """A transform which transforms web intelligent text into HTML."""

    title = _(u'title_web_intelligent_html_transform',
        default=u'Web Intelligent Text to HTML transform')

    inputs = ("text/x-web-intelligent", )
    output = "text/html"

    available = False

    def __init__(self):
        super(WebIntelligentHtmlTransform, self).__init__()
        if HAS_WEB_INTELLIGENTTEXT:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = convertWebIntelligentPlainTextToHtml(u''.join(data))
        return TransformResult(StringIter(unicode(html, 'utf-8')))


class HtmlWebIntelligentTransform(Transform):
    """A transform which transforms HTML into web intelligent text."""

    title = _(u'title_html_web_intelligent_transform',
        default=u'HTML to Web Intelligent Text transform')

    inputs = ("text/html",)
    output = "text/x-web-intelligent"

    available = False

    def __init__(self):
        super(HtmlWebIntelligentTransform, self).__init__()
        if HAS_WEB_INTELLIGENTTEXT:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        html = u''.join(data).encode('utf-8')
        html = convertHtmlToWebIntelligentPlainText(html)
        return TransformResult(StringIter(unicode(html, 'utf-8')))
