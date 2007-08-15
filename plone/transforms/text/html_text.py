"""
HTML to text transform
"""
from logging import DEBUG
import re

from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.log import log
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
    """A transform which transforms HTML into Text.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, HtmlToTextTransform)
      True
    """

    implements(ITransform)

    name = u'plone.transforms.text.html_text.HtmlToTextTransform'

    title = _(u'title_html_to_text_transform',
        default=u'HTML to Text transform')

    description = _(u'description_html_to_text_transform',
        default=u"A transform which transforms HTML into Text.")

    inputs  = ("text/html",)
    output = "text/plain"

    available = True

    def transform(self, data):
        if not self.available:
            return None
        # Invalid input
        if data is None or isinstance(data, basestring):
            log(DEBUG, "Invalid input while transforming an Image in %s." %
                        self.name)
            return None

        # TODO convert entites with htmlentitydefs.name2codepoint ?
        data = u''.join(data)
        for regex in FILTERS:
            data = regex.sub(u' ', data)
        return TransformResult(StringIter(data))
