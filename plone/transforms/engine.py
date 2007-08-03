from persistent import Persistent

from zope.component import getSiteManager
from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformEngine


class TransformEngine(object):
    """A transform engine.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITransformEngine, TransformEngine)
      True
    """

    implements(ITransformEngine)

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
            for input_ in transform.inputs:
                available.append((input_, transform.output, transform))
        return available

    def transform(self, data, input_mimetype, output_mimetype):
        """
        The transform method takes some data in the input format and returns
        it in the output format.

        When no transform or transformation chain for the given input and
        output mimetype can be found a ValueError is raised.
        """
        available = self.available_transforms()
        available_inputs = [spec[0] for spec in available]
        available_outputs = [spec[1] for spec in available]

        # Is the input and output format available?
        if (input_mimetype not in available_inputs or
            output_mimetype not in available_outputs):
            raise ValueError("No transforms could be found to transform the "
                             "'%s' format into the '%s' format."
                             % (input_mimetype, output_mimetype))

        # Special behavior for filters, which have an identical input and
        # output encoding
        if input_mimetype == output_mimetype:
            matches = [spec[2] for spec in available
                        if spec[0] == input_mimetype and
                           spec[1] == input_mimetype]
            if len(matches) > 0:
                return matches[0].transform(data)

        # Find all transforms which match the input format
        matches = [spec for spec in available if spec[0] == input_mimetype]
        paths = []
        if len(matches) > 0:
            # XXX Add recursive algorithms, so non-direct matches are found as well
            for spec in matches:
                if spec[1] == output_mimetype:
                    paths.append(spec[2])

        # Sort by path length
        if len(paths) > 0:
            # XXX We only have a simple list of transforms right now.
            # paths.sort(key=len)
            return paths[0].transform(data)

        raise ValueError("No transforms could be found to transform the '%s' "
                         "format into the '%s' format."
                         % (input_mimetype, output_mimetype))


class PersistentTransformEngine(Persistent, TransformEngine):

    def __init__(self):
      self.selected_transforms = {}
