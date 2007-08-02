from zope.interface import implements

from plone.transforms.interfaces import ILocalEngineRegistration


class LocalEngineRegistration(object):
    """A registration for a local transformation engine.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ILocalEngineRegistration, LocalEngineRegistration)
      True
    """
    implements(ILocalEngineRegistration)

    interface_name = None
    name = None

    def __init__(self, interface_name, name=None):
        self.interface_name = interface_name
        self.name = name
