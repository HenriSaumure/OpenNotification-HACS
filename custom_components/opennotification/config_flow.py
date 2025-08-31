import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .const import DOMAIN, CONF_SERVER, CONF_GUID

class OpenNotificationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_NAME, default="OpenNotification"): str,
            vol.Required(CONF_SERVER, default="https://api.opennotification.org/notification"): str,
            vol.Required(CONF_GUID): str
        })
        return self.async_show_form(step_id="user", data_schema=schema)
