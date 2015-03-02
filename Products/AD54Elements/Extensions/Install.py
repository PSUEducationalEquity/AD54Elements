from Products.CMFCore.utils import getToolByName
from Products.AD54Elements.migrations import delete_import_step

def install(portal, reinstall=False):
    setup_tool = getToolByName(portal, 'portal_setup')

    # run our complete profile
    setup_tool.runAllImportStepsFromProfile('profile-Products.AD54Elements:default')
    return "Ran all import steps"

def uninstall(portal, reinstall=False):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-Products.AD54Elements:uninstall')

    # clean up our import_steps past and present
    delete_import_step(setup_tool, u'ad54elements_various')
    delete_import_step(setup_tool, u'ad54elements_loaddefaults')

    return "Ran all uninstall steps"

