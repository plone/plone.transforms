"""
HTML to text transform
"""
import re

from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

SCRIPT_RE = re.compile('<script [^>]>.*</script>(?im)')
STYLE_RE = re.compile('<style [^>]>.*</style>(?im)')
HEAD_RE = re.compile('<head [^>]>.*</head>(?im)')
TEXTFORMAT_RE = re.compile('(?im)</?(font|em|i|strong|b)(?=\W)[^>]*>')
TAG_RE = re.compile('<[^>]*>(?i)(?m)')

FILTERS = frozenset((SCRIPT_RE, STYLE_RE, HEAD_RE, TEXTFORMAT_RE, TAG_RE))


class HtmlToTextTransform(Transform):
    """A transform which transforms HTML into Text."""

    title = _(u'title_html_to_text_transform',
        default=u'HTML to Text transform')

    inputs = ("text/html", )
    output = "text/plain"

    available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        # TODO convert entites with htmlentitydefs.name2codepoint ?
        data = u''.join(data)
        for regex in FILTERS:
            data = regex.sub(u' ', data)
        return TransformResult(StringIter(data))
