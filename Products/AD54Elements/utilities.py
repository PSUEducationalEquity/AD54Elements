from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

class AD54NonInstallable(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [u'Products.AD54Elements:uninstall',
                u'Products.AD54Elements:once',
                ]
