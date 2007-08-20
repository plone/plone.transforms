from logging import DEBUG
from persistent import Persistent

from zope.component import getSiteManager
from zope.interface import implements

from plone.transforms.interfaces import ITransform
from plone.transforms.interfaces import ITransformEngine
from plone.transforms.log import log


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

    def find_transform(self, input_mimetype, output_mimetype):
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
            log(DEBUG, "No transforms could be found to transform the "
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

        # Sort by path length
        if len(paths) > 0:
            paths.sort()
            return paths[0]

        log(DEBUG, "No transforms could be found to transform the '%s' "
                   "format into the '%s' format." %
                   (input_mimetype, output_mimetype))
        return None

    def transform(self, data, input_mimetype, output_mimetype):
        """
        The transform method takes some data in one of the input formats.
        It returns either an ITransformResult in the output format or None
        if an error occurred.
        """
        transform = self.find_transform(input_mimetype, output_mimetype)
        if transform is None:
            return None

        return transform.transform(data)


class PersistentTransformEngine(Persistent, TransformEngine):

    def __init__(self):
      self.selected_transforms = {}
