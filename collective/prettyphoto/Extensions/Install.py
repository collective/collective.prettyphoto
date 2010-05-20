from Products.CMFCore.utils import getToolByName


def uninstall(portal):
    """Run uninstall profile."""

    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.prettyphoto:uninstall')
    setup_tool.setBaselineContext('profile-Products.CMFPlone:plone')
    return "Ran all uninstall steps."