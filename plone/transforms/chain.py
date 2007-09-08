from persistent.list import PersistentList

from zope.component import queryUtility
from zope.dottedname.resolve import resolve
from zope.interface import implements

from plone.transforms.interfaces import ITransformChain
from plone.transforms.message import PloneMessageFactory as _
from plone.transforms.transform import TransformResult


class AbstractTransformChain:
    """A transform chain is an utility with optional configuration information.
    
    It stores a list of (interface_name, name) tuples which identify transforms.
    The interface_name must be the full dotted path to an actual interface.
    """

    available = True

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

    def transform(self, data, options=None):
        """Returns the transform result."""
        metadata = None
        subobjects = None
        errors = None
        old_transform = None
        for transform_spec in self:
            interface_name, name = transform_spec
            try:
                interface = resolve(interface_name)
            except ImportError, e:
                raise ValueError("The transform chain '%s' includes a "
                                 "transform for the interface '%s' but this "
                                 "could not be imported."
                                 % (self.name, interface_name))
            interface = resolve(interface_name)
            transform = queryUtility(interface, name=name)
            if transform is None:
                raise ValueError("The transform chain '%s' includes a "
                                 "transform for the interface '%s' with the "
                                 "name '%s'. The transform could not be found."
                                 % (self.name, interface_name, name))
            if not transform.available:
                self.available = False
                raise ValueError("The transform chain '%s' includes a "
                                 "transform for the interface '%s' with the "
                                 "name '%s'. The transform is unavailable."
                                 % (self.name, interface_name, name))
            result = transform.transform(data, options=options)
            if result is None:
                return None
            # Get the data from the result
            data = result.data
            metadata = result.metadata
            subobjects = result.subobjects
            errors = result.errors
            old_transform = transform
        return TransformResult(data, metadata, subobjects, errors)


class TransformChain(list, AbstractTransformChain):
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

    available = True

    def __repr__(self):
        return '<%s object at %s>' % (str(self.name), id(self))


class PersistentTransformChain(PersistentList, AbstractTransformChain):
    """A persistent transform chain

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformChain, PersistentTransformChain)
      True
    """

    implements(ITransformChain)

    name = u'plone.transforms.chain.PersistentTransformChain'
    title = _(u'title_skeleton_persistent_transform_chain',
              default=u'A skeleton persistent transform chain.')
    description = None

    available = True

    def __repr__(self):
        return '<%s object at %s>' % (str(self.name), id(self))
