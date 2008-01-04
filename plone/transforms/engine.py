from persistent.list import PersistentList

from zope.component import queryUtility
from zope.component import getSiteManager
from zope.dottedname.resolve import resolve
from zope.interface import implements

from plone.transforms.interfaces import IConfigurableTransformEngine
from plone.transforms.interfaces import IRankedTransform
from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformEngine
from plone.transforms.log import log_debug


class TransformEngine(object):
    """A transform engine.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformEngine, TransformEngine)
      True
    """

    implements(ITransformEngine)

    # TODO This could be cached on the instance -> use plone.memoize.instance
    def unavailable_transforms(self):
        """
        Returns a list of all currently registered but unavailable transforms.
        The list entries are triples of
        (input mimetype, output mimetype, transform).
        """
        sm = getSiteManager()
        transforms = sm.getAllUtilitiesRegisteredFor(ITransform)

        # Get a list of all available transforms, 
        unavailable = []
        for transform in transforms:
            if not transform.available:
                for input_ in transform.inputs:
                    unavailable.append((input_, transform.output, transform))
        return unavailable

    # TODO This could be cached on the instance -> use plone.memoize.instance
    def available_transforms(self):
        """
        Returns a list of all available transforms. The list entries are
        triples of (input mimetype, output mimetype, transform).
        """
        sm = getSiteManager()
        transforms = sm.getAllUtilitiesRegisteredFor(ITransform)

        # Get a list of all available transforms, 
        available = []
        for transform in transforms:
            if transform.available:
                for input_ in transform.inputs:
                    available.append((input_, transform.output, transform))
        return available

    def find_transform(self, input_mimetype, output_mimetype, use_ranked=True):
        """
        The find_transform method returns the transform which is going to
        be used for a particular input / output mimetype combination.
        """
        available = self.available_transforms()
        available_inputs = [spec[0] for spec in available]
        available_outputs = [spec[1] for spec in available]

        # Is the input and output format available?
        if (input_mimetype not in available_inputs or
            output_mimetype not in available_outputs):
            log_debug("No transforms could be found to transform the "
                      "'%s' format into the '%s' format." %
                      (input_mimetype, output_mimetype))
            return None

        # Special behavior for filters, which have an identical input and
        # output encoding
        matches = []
        if input_mimetype == output_mimetype:
            matches = [spec[2] for spec in available
                        if spec[0] == input_mimetype and
                           spec[1] == input_mimetype]

        if len(matches) > 0:
            return matches[0]

        # Find all transforms which match the input format
        matches = [spec for spec in available if spec[0] == input_mimetype]
        paths = []
        if len(matches) > 0:
            # TODO Add recursive algorithms, so non-direct matches are found as well
            for spec in matches:
                if spec[1] == output_mimetype:
                    paths.append(spec[2])

        # Sort by some criteria
        if len(paths) > 0:
            def _criteria(value):
                ranked = IRankedTransform.providedBy(value)
                rank = 100
                if ranked:
                    rank = value.rank
                return rank

            if use_ranked:
                paths.sort(key=_criteria)
            return paths[0]

        log_debug("No transforms could be found to transform the '%s' "
                  "format into the '%s' format." %
                  (input_mimetype, output_mimetype))
        return None

    def transform(self, data, input_mimetype, output_mimetype, options=None):
        """Returns the transform result."""
        transform = self.find_transform(input_mimetype, output_mimetype)
        if transform is None:
            return None

        if options is None:
            options = {}
        options['input_mimetype'] = input_mimetype
        options['output_mimetype'] = output_mimetype

        return transform.transform(data, options=options)


class ConfigurableTransformEngine(PersistentList, TransformEngine):
    """
    A transformation engine, which provides helper methods to transform data.
    
    It bases its transform finding algorithm on the explicitely set
    configuration information stored in itself.

    It stores a list of (interface, name) tuples.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IConfigurableTransformEngine, ConfigurableTransformEngine)
      True
    """

    implements(IConfigurableTransformEngine)

    def __init__(self):
        super(ConfigurableTransformEngine, self).__init__()

    def __repr__(self):
        return '<ConfigurableTransformEngine object at %s>' % id(self)

    def unavailable_transforms(self):
        """
        Returns a list of all currently registered but unavailable transforms.
        The list entries are triples of
        (input mimetype, output mimetype, transform).
        """
        unavailable = []
        for interface_name, name in self:
            interface = resolve(interface_name)
            transform = queryUtility(interface, name=name)
            if transform is not None and not transform.available:
                for input_ in transform.inputs:
                    unavailable.append((input_, transform.output, transform))
        return unavailable

    def available_transforms(self):
        """
        Returns a list of all available transforms. The list entries are
        triples of (input mimetype, output mimetype, transform).
        """
        available = []
        for interface_name, name in self:
            interface = resolve(interface_name)
            transform = queryUtility(interface, name=name)
            if transform is not None and transform.available:
                for input_ in transform.inputs:
                    available.append((input_, transform.output, transform))
        return available

    def find_transform(self, input_mimetype, output_mimetype):
        """
        The find_transform method returns the transform which is going to
        be used for a particular input / output mimetype combination.
        
        The configurable transform engine does only take the order in its own
        registry list into account and ignores the ones specifed via
        IRankedTransform.
        """
        return super(ConfigurableTransformEngine, self).find_transform(
            input_mimetype, output_mimetype, use_ranked=False)
