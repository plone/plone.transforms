from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

HAS_REST = True
try:
    from reStructuredText import HTML
except ImportError:
    HAS_REST = False


class RestHtmlTransform(Transform):
    """A transform which transforms restructured text into HTML."""

    title = _(u'title_rest_html_transform',
        default=u'REST to HTML transform')

    inputs = ("text/x-rst", "text/restructured", )
    output = "text/html"

    available = False

    header_level = 2
    report_level = 2
    language = 'en'
    warnings = None

    def __init__(self):
        super(RestHtmlTransform, self).__init__()
        if HAS_REST:
            self.available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        header_level = self.header_level
        report_level = self.report_level
        language = self.language
        warnings = self.warnings
        if options:
            header_level = options.get('header_level', header_level)
            report_level = options.get('report_level', report_level)
            language = options.get('language', language)
            warnings = options.get('warnings', warnings)

        html = HTML(u''.join(data).encode('utf-8'),
                    input_encoding='utf-8',
                    output_encoding='utf-8',
                    language_code=language,
                    initial_header_level=header_level,
                    report_level=report_level,
                    warnings=warnings,
                    settings=dict(documentclass='', traceback=1))

        html = html.replace(' class="document"', '', 1)
        return TransformResult(StringIter(unicode(html, 'utf-8')))
