from zope.interface import implements

from plone.transforms.interfaces.transform import ITransform


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

    title = None
    description = None

    def __init__(self, inputs=(), output=(), title=None, description=None):
        self.inputs = inputs
        self.output = output
        self.title = title
        self.description = description

    def convert(self, data, **kwargs):
        """
        The convert method takes some data in one of the input formats and
        returns it in the output format.
        """
        return data
