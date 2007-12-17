from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

HAS_ST = True
try:
    from StructuredText.StructuredText import HTML
except ImportError:
    HAS_ST = False


class StructuredTextHtmlTransform(Transform):
    """A transform which transforms structured text into HTML."""

    title = _(u'title_st_html_transform',
        default=u'Structured text to HTML transform')

    inputs = ("text/structured", )
    output = "text/html"

    available = False

    level = 2

    def __init__(self):
        super(StructuredTextHtmlTransform, self).__init__()
        if HAS_ST:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        level = self.level
        if options:
            level = options.get('level', level)

        html = HTML(u''.join(data).encode('utf-8'),
                    level=level,
                    header=0)

        return TransformResult(StringIter(unicode(html, 'utf-8')))
