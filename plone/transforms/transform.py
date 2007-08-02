from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformResult

from plone.transforms.message import PloneMessageFactory as _


class TransformResult(object):
    """Data stream, is the result of a transform.
    
    The data argument takes an object providing Python's iterator protocol.
    In case of textual data, the data has to be Unicode. The same applies
    to the data return value and the values in the subobjects

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformResult, TransformResult)
      True
    """

    implements(ITransformResult)

    data = None
    metadata = {}
    subobjects = {}

    def __init__(self, data, metadata=None, subobjects=None):
        self.data = data
        if subobjects is not None:
            self.subobjects = subobjects
        if metadata is not None:
            self.metadata = metadata


class Transform(object):
    """A transform is an utility with optional configuration information.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransform, Transform)
      True
    """

    implements(ITransform)

    inputs = (None, )
    output = None

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
        return TransformResult(data)
