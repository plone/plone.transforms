from zope.component import queryUtility
from zope.interface import implements

from plone.transforms.interfaces.chain import ITransformChain
from plone.transforms.message import PloneMessageFactory as _


class TransformChain(list):
    """A transform chain is an utility with optional configuration information.
    
    It stores a list of (interface, name) tuples which identify transforms.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformChain, TransformChain)
      True
    """

    implements(ITransformChain)

    name = u'plone.transforms.chain.TransformChain'
    title = _(u'title_skeleton_transform_chain',
              default=u'A skeleton transform chain.')
    description = None

    @property
    def inputs(self):
        """
        The accepted inputs of a transform chain are the inputs of the first
        transform in the chain or empty if no transform is yet registered.
        """
        if len(self) == 0:
            # If the chain is empty, we don't know our input formats.
            return None
        interface, name = self[0]
        first = queryUtility(interface, name=name)
        return first.inputs

    @property
    def output(self):
        """
        The output format of a transform chain is the output of the last
        transform in the chain or empty if no transform is yet registered.
        """
        if len(self) == 0:
            # If the chain is empty, we don't know our output format.
            return None
        interface, name = self[-1]
        last = queryUtility(interface, name=name)
        return last.output

    def convert(self, data):
        """
        The convert method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """
        for transform_spec in self:
            transform = queryUtility(transform_spec[0], name=transform_spec[1])
            data = transform.convert(data)
        return data
