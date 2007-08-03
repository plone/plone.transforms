from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from plone.transforms.message import PloneMessageFactory as _


class ConfigurationForm(BrowserView):

    template = ZopeTwoPageTemplateFile('engine_configuration.pt')

    def __call__(self):
        if 'submitted' in self.request:
            self.process()
        return self.template()    

    def process(self):
        # Do some work
        IStatusMessage(self.request).addStatusMessage(_(u'Changes saved.'))
