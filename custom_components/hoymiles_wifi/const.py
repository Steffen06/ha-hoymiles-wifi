"""Constants for the Hoymiles integration."""

DOMAIN = "hoymiles_wifi"
NAME = "Hoymiles"
DOMAIN = "hoymiles_wifi"
DOMAIN_DATA = f"{DOMAIN}_data"
CONFIG_VERSION = 3

ISSUE_URL = "https://github.com/suaveolent/ha-hoymiles-wifi/issues"

CONF_UPDATE_INTERVAL = "update_interval"
CONF_DTU_SERIAL_NUMBER = "dtu_serial_number"
CONF_INVERTERS = "inverters"
CONF_THREE_PHASE_INVERTERS = "three_phase_inverters"
CONF_PORTS = "ports"
CONF_METERS = "meters"

DEFAULT_UPDATE_INTERVAL_SECONDS = 35
MIN_UPDATE_INTERVAL_SECONDS = 1

DEFAULT_CONFIG_UPDATE_INTERVAL_SECONDS = 60 * 5
DEFAULT_APP_INFO_UPDATE_INTERVAL_SECONDS = 60 * 60 * 2


HASS_DATA_COORDINATOR = "data_coordinator"
HASS_CONFIG_COORDINATOR = "config_coordinator"
HASS_APP_INFO_COORDINATOR = "app_info_coordinator"
HASS_DTU = "dtu"
HASS_DATA_UNSUB_OPTIONS_UPDATE_LISTENER = "unsub_options_update_listener"


FCTN_GENERATE_DTU_VERSION_STRING = "generate_dtu_version_string"
FCTN_GENERATE_INVERTER_HW_VERSION_STRING = "generate_version_string"
FCTN_GENERATE_INVERTER_SW_VERSION_STRING = "generate_sw_version_string"

STARTUP_MESSAGE = f"""

-------------------------------------------------------------------
{NAME}
This is a custom integration!
If you have any issues with it please open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
