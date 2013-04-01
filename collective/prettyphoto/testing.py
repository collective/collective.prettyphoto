# -*- coding: utf-8 -*-
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_ID
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2
from zope.configuration import xmlconfig

import pkg_resources

try:
    pkg_resources.get_distribution('plone.app.collection')
except pkg_resources.DistributionNotFound:
    HAS_COLLECTION = False
else:
    HAS_COLLECTION = True


class PrettyPhotoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.prettyphoto
        xmlconfig.file(
            'testing.zcml',
            collective.prettyphoto,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.prettyphoto:testing')
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")

        setRoles(portal, TEST_USER_ID, ['Manager'])

        # Add a Folder
        portal.invokeFactory("Folder",
                             id="test-folder", title=u"Test Folder")

        # Add a Collection
        portal.invokeFactory(HAS_COLLECTION and 'Collection' or 'Topic',
                             id="test-collection", title=u"Test Collection")


COLLECTIVE_PRETTYPHOTO_FIXTURE = PrettyPhotoLayer()
COLLECTIVE_PRETTYPHOTO_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_PRETTYPHOTO_FIXTURE, ),
    name="collective.prettyphoto:Integration")
COLLECTIVE_PRETTYPHOTO_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_PRETTYPHOTO_FIXTURE, ),
    name="collective.prettyphoto:Functional")
COLLECTIVE_PRETTYPHOTO_ROBOT = FunctionalTesting(
    bases=(COLLECTIVE_PRETTYPHOTO_FIXTURE, z2.ZSERVER_FIXTURE),
    name="collective.prettyphoto:Robot")
