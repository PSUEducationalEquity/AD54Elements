import logging

def delete_import_step(setup_tool, step):
    registry = setup_tool.getImportStepRegistry()
    if step in registry.listSteps():
        try:
            registry.unregisterStep(step)
        except AttributeError:
            del registry._registered[step]
        setup_tool._p_changed = True
        log = logging.getLogger("AD54Elements")
        log.info("Deleted %s import step", step)

def from_2_0_to_2_1(context):
    # delete the ad54elements_various step for anyone following trunk (1 -> 2)
    delete_import_step(context, u'ad54elements_various')

    # run the new import step (1 -> 2)
    context.runImportStepFromProfile('profile-Products.AD54Elements:default',
            'ad54elements_loaddefaults')

    # log it
    log = logging.getLogger("AD54Elements")
    log.info("Ran load defaults import step")


def from_2_1_to_2_2(context):
    # run the cssregistry and jsregistry import steps (2 -> 3)
    context.runImportStepFromProfile('profile-Products.AD54Elements:default',
            'cssregistry')
    context.runImportStepFromProfile('profile-Products.AD54Elements:default',
            'jsregistry')

    # log it
    log = logging.getLogger("AD54Elements")
    log.info("Ran cssregistry and jsregistry import steps")

def from_2_2_to_3_0(context):
    # run the jsregistry import steps (3 -> 4)
    context.runImportStepFromProfile('profile-Products.AD54Elements:default',
            'jsregistry')

    # log it
    log = logging.getLogger("AD54Elements")
    log.info("Ran jsregistry import steps")
