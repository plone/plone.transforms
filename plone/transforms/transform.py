from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import IMultipleOutputTransform

from plone.transforms.message import PloneMessageFactory as _


class Transform(object):
    """A transform is an utility with optional configuration information.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, Transform)
      True
    """

    implements(ITransform)

    inputs = ()
    output = ()

    name = u'plone.transforms.transform.Transform'
    title = _(u'title_skeleton_transform',
              default=u'A skeleton transform.')
    description = None

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """
        return data


class MultipleOutputTransform(object):
    """A transform which has multiple output streams.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMultipleOutputTransform, MultipleOutputTransform)
      True
    """

    implements(IMultipleOutputTransform)

    inputs = ()
    output = ()

    name = u'plone.transforms.transform.MultipleOutputTransform'
    title = _(u'title_skeleton_multiple_output_transform',
              default=u'A skeleton multiple output transform.')
    description = None

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats.
        
        It returns a dict of named output streams, with a default output stream
        named 'default'.
        """
        return {'default' : data}
