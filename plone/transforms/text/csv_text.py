"""
CSV to text transform
"""
import re

from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

COMMA_RE = re.compile(',')
QUOTES_RE = re.compile('"')

FILTERS = frozenset((COMMA_RE, QUOTES_RE))

class CsvTextTransform(Transform):
    """A transform which transforms CSV into Text."""

    title = _(u'title_csv_to_text_transform',
        default=u'CSV to Text transform')

    inputs = ("text/comma-separated-values", )
    output = "text/plain"

    available = True

    def transform(self, data, options=None):
        if self._validate(data) is None:
            return None

        data = u''.join(data)
        for regex in FILTERS:
            data = regex.sub(u' ', data)
        return TransformResult(StringIter(data))
