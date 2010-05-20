from logging import getLogger
from plone.browserlayer import utils as layerutils
from collective.prettyphoto.interfaces import IPrettyPhotoSpecific

log = getLogger('collective.prettyphoto')


def resetLayers(context):
    """Remove custom browserlayer on uninstall."""

    if context.readDataFile('collective.prettyphoto_uninstall.txt') is None:
        return
    
    if IPrettyPhotoSpecific in layerutils.registered_layers():
        layerutils.unregister_layer(name='collective.prettyphoto')
        log.info('Browser layer "collective.prettyphoto" uninstalled.')


