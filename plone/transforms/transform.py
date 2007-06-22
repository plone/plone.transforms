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

    def convert(self, data):
        """
        The convert method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """
        pass
