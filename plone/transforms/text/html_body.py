"""
HTML body extractor transform
"""
from zope.interface import implements
from StringIO import StringIO

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult
from plone.transforms.utils import html_bodyfinder


class HtmlBodyTransform(Transform):
    """A transform which extracts the body of a HTML text.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, HtmlBodyTransform)
      True
    """

    implements(ITransform)

    name = u'plone.transforms.text.html_body.HtmlBodyTransform'

    title = _(u'title_html_body_transform',
        default=u'HTML body extractor')

    description = _(u'description_html_body_transform',
        default=u"A transform which extracts the body of a HTML text.")

    inputs  = ("text/html",)
    output = "text/html"

    def transform(self, data):
        data = u''.join(data)
        return TransformResult(StringIO(html_bodyfinder(data)))
