from Products.CMFCore.utils import getToolByName

def importDefaults(context):
    """Run the once profile if there is no configuration."""
    if context.readDataFile('ad54elements_various.txt') is None:
        return
    portal = context.getSite()
    logger = context.getLogger('AD54Elements')

    # if our properties tool does not exist, run the "once" profile to set defaults
    ad54_props = getToolByName(getToolByName(portal, 'portal_properties'), 'ad54elements_properties', None)
    if ad54_props is None:
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile('profile-Products.AD54Elements:once')
        logger.info('Performed one-time settings import.')
    else:
        logger.info('One-time settings import skipped.')

