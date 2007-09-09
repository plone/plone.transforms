from zope.component.zcml import IUtilityDirective


class ITransformDirective(IUtilityDirective):
    """Directive which registers a new transform.

    This is basically an utility registration which is smart enough to figure
    out some things by itself, so you don't need to write them.
    """
