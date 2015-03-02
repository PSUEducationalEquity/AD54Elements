# -*- coding: utf-8 -*-
"""Base fixtures for the AD54Elements tests."""
from plone.app.testing import PLONE_FIXTURE, PloneSandboxLayer
from plone.app.testing import quickInstallProduct
from plone.app.testing.layers import IntegrationTesting, FunctionalTesting
from plone.testing import z2


class AD54ElementsLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        #: Load ZCML for the package being tested.
        import Products.AD54Elements
        self.loadZCML(package=Products.AD54Elements)
        z2.installProduct(app, 'Products.AD54Elements')

    def setUpPloneSite(self, portal):
        #: Install the package in the Plone site.
        quickInstallProduct(portal, 'Products.AD54Elements')


AD54ELEMENTS_FIXTURE = AD54ElementsLayer()
AD54ELEMENTS_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(AD54ELEMENTS_FIXTURE,),
                       name="AD54Elements:Integration")
AD54ELEMENTS_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(AD54ELEMENTS_FIXTURE,),
                       name="AD54Elements:Functional")
