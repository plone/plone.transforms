"""
HTML to Text
"""
from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import Transform
from plone.transforms.transform import TransformResult

import re

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

    def transform(self, data):
        # TODO convert entites with htmlentitydefs.name2codepoint ?
        for convertion_chain in ( 
                       '<script [^>]>.*</script>(?im)',
                       '<style [^>]>.*</style>(?im)',
                       '<head [^>]>.*</head>(?im)',
                       '(?im)</?(font|em|i|strong|b)(?=\W)[^>]*>',
                       '<[^>]*>(?i)(?m)',
                       ) :
            r = re.compile( convertion_chain )
            data = r.sub(u' ', u''.join(data))
        return TransformResult(iter(data))
