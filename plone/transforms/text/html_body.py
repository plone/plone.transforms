"""
HTML body extractor transform
"""
from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.stringiter import StringIter
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult
from plone.transforms.utils import html_bodyfinder


class HtmlBodyTransform(Transform):
    """A transform which extracts the body of a HTML text."""

    implements(ITransform)

    name = u'plone.transforms.text.html_body.HtmlBodyTransform'

    title = _(u'title_html_body_transform',
        default=u'HTML body extractor')

    description = _(u'description_html_body_transform',
        default=u"A transform which extracts the body of a HTML text.")

    inputs  = ("text/html",)
    output = "text/html"

    def transform(self, data, options=None):
        """Returns the transform result."""
        if self._validate(data) is None:
            return None

        data = u''.join(data)
        return TransformResult(StringIter(html_bodyfinder(data)))
