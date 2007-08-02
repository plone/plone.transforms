from zope.interface import Attribute, Interface


class IEngineRegistration(Interface):
    """
    A registration for a transformation engine.
    """


class ILocalEngineRegistration(IEngineRegistration):
    """
    A registration for a local transformation engine.
    """

    interface_name = Attribute("A full dotted path which represents an "
                               "interface, like ITransformEngine.")

    name = Attribute("The name of the transform engine.")


class IRemoteEngineRegistration(IEngineRegistration):
    """
    A registration for a remote transformation engine.
    """

    host = Attribute("The hostname or IP address of the server the engine "
                     "is running on.")

    port = Attribute("The port on which the engine is listening.")

    method = Attribute("The method to get the engine back.")
