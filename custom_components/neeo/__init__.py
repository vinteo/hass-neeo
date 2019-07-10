import logging
import requests
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.const import CONF_HOST
from homeassistant.helpers.discovery import load_platform

DOMAIN = 'neeo'

VERSION = '0.1.0'

CONF_RECIPES = 'recipes'

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
  DOMAIN: vol.Schema({
    vol.Required(CONF_HOST): cv.string,
  })
}, extra=vol.ALLOW_EXTRA)

def setup(hass, config):
  host = config[DOMAIN].get(CONF_HOST)
  neeo = Neeo(host)

  hass.data[DOMAIN] = {
    DOMAIN: neeo,
  }

  load_platform(hass, 'switch', DOMAIN, {}, config)

  return True


class Neeo(object):

  def __init__(self, host):
    self._host = host
    self.data = {}

  def recipes(self):
    try:
      url = 'http://{}:3000/v1/api/Recipes'.format(self._host)
      response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
      _LOGGER.error("No route to device '%s'", self._resource)

    self.data[CONF_RECIPES] = []

    for recipe in response.json():
      self.data[CONF_RECIPES].append(NeeoRecipe(self._host, recipe))

    return self.data[CONF_RECIPES]


class NeeoRecipe(object):

  def __init__(self, host, recipe):
    self._host = host
    self._recipe = recipe

  @property
  def name(self):
    return self._recipe['detail']['devicename']

  def status(self):
    try:
      url = self._recipe['url']['getPowerState']
      response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
      _LOGGER.error("No route to device '%s'", self._resource)

    return response.json()['active']

  def turn_on(self):
    try:
      url = self._recipe['url']['setPowerOn']
      response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
      _LOGGER.error("No route to device '%s'", self._resource)

  def turn_off(self):
    try:
      url = self._recipe['url']['setPowerOff']
      response = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
      _LOGGER.error("No route to device '%s'", self._resource)
