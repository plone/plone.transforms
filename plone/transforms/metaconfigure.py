from persistent.interfaces import IPersistent

from zope.component.zcml import PublicPermission
from zope.component.zcml import utility
from zope.interface import providedBy

from plone.transforms.interfaces import ICommandTransform
from plone.transforms.interfaces import IRankedTransform
from plone.transforms.interfaces import ITransform

INVALID_INTERFACES = frozenset((IPersistent, IRankedTransform, ))

KNOWN_BASE_NAMES = frozenset((
    ('plone.transforms.transform'),
    ('plone.transforms.chain'),
    ('plone.transforms.image.pil'),
    ))

def transformDirective(_context, provides=None, component=None, factory=None,
                       permission=None, name=None):

    if factory:
        if component:
            raise TypeError("Can't specify factory and component.")
        component = factory()
        factory = None

    if name is None:
        name = component.name
        if [True for n in KNOWN_BASE_NAMES if name.startswith(n)]:
            # If no name was specified or we are subclassing one of the
            # base classes, automatically generate the name based on the full
            # dotted class name.
            module = component.__module__
            classname = component.__class__.__name__
            name = component.name = module + '.' + classname

    if permission is None:
        # Default to all public permission
        permission = PublicPermission

    if provides is None:
        provides = list(providedBy(component))
        if len(provides) == 1:
            provides = provides[0]
        else:
            # Try to be a bit smarter about the interface guessing.
            for iface in provides:
                if (not iface.isOrExtends(ITransform) or
                    iface in INVALID_INTERFACES):
                    provides.remove(iface)
            # See if we still have more than one interface
            if len(provides) == 1:
                provides = provides[0]
            else:
                # See if we have both ITransform and something else in here
                if ITransform in provides:
                    provides.remove(ITransform)
                if len(provides) == 1:
                    provides = provides[0]
                else:
                    # Look again for ICommandTransform and something else
                    if ICommandTransform in provides:
                        provides.remove(ICommandTransform)
                    if len(provides) == 1:
                        provides = provides[0]
                    else:
                        raise TypeError("Missing 'provides' attribute")

    utility(_context, provides=provides, component=component, factory=factory,
                    permission=permission, name=name)
