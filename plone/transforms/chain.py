from zope.component import queryUtility
from zope.dottedname.resolve import resolve
from zope.interface import implements

from plone.transforms.interfaces import ITransformChain
from plone.transforms.message import PloneMessageFactory as _


class TransformChain(list):
    """A transform chain is an utility with optional configuration information.
    
    It stores a list of (interface_name, name) tuples which identify transforms.
    The interface_name must be the full dotted path to an actual interface.

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
        interface_name, name = self[0]
        interface = resolve(interface_name)
        first = queryUtility(interface, name=name)
        if first is None:
            return None
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
        interface_name, name = self[-1]
        interface = resolve(interface_name)
        last = queryUtility(interface, name=name)
        if last is None:
            return None
        return last.output

    def transform(self, data):
        """
        The transform method takes some data in one of the input formats and
        returns it in the output format.
        
        The data argument takes an object providing Python's iterator protocol.
        In case of textual data, the data has to be Unicode. The same applies
        to the return value.
        """
        for transform_spec in self:
            interface_name, name = transform_spec
            interface = resolve(interface_name)
            transform = queryUtility(interface, name=name)
            data = transform.transform(data)
        return data