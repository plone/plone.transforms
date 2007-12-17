from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import Transform


class IdentityTransform(Transform):
    """A transform which transforms any input into the identical output."""

    title = _(u'title_identity_transform',
              default=u'An identity transform.')
