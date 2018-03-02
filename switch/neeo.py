from custom_components.neeo import DOMAIN
from homeassistant.components.switch import SwitchDevice
from urllib.parse import unquote

def setup_platform(hass, config, add_devices, discovery_info=None):
  neeo = hass.data[DOMAIN][DOMAIN]

  switches = []
  for recipe in neeo.recipes():
    switches.append(RecipeSwitch(recipe))

  add_devices(switches, True)


class RecipeSwitch(SwitchDevice):

  def __init__(self, recipe):
    self._recipe = recipe
    self._is_on = False

  @property
  def name(self):
    """Return the name of the binary sensor."""
    return 'NEEO {}'.format(unquote(self._recipe.name))

  @property
  def is_on(self):
    """Return true if the binary sensor is on."""
    return bool(self._is_on)

  def update(self):
    """Get the latest data """
    self._is_on = self._recipe.status()

  def turn_on(self, **kwargs):
    """Turn the device on."""
    self._recipe.turn_on()
    self._is_on = 1
    self.schedule_update_ha_state()

  def turn_off(self, **kwargs):
    """Turn the device off."""
    self._recipe.turn_off()
    self._is_on = 0
    self.schedule_update_ha_state()
