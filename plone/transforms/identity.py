from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import Transform


class IdentityTransform(Transform):
    """A transform which transforms any input into the identical output.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, IdentityTransform)
      True
    """

    implements(ITransform)

    name = u'plone.transforms.identity.IdentityTransform'
    title = _(u'title_identity_transform',
              default=u'An identity transform.')
    description = _(u'description_identity_transform',
                    default=u"A transform which transforms any input into "
                             "the identical output.")
