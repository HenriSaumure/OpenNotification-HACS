from homeassistant.core import HomeAssistant, ServiceCall
import aiohttp
import asyncio
from homeassistant.helpers import config_validation as cv
import voluptuous as vol
from .const import DOMAIN, CONF_SERVER, CONF_GUID

SERVICE_SEND_SCHEMA = vol.Schema({
    vol.Required("title"): cv.string,
    vol.Optional("description"): cv.string,
    vol.Optional("pictureLink"): cv.string,
    vol.Optional("icon"): cv.string,
    vol.Optional("actionLink"): cv.string,
    vol.Optional("isAlert"): cv.boolean,
})

async def async_setup_entry(hass: HomeAssistant, entry):
    server_url = entry.data[CONF_SERVER]
    guid = entry.data[CONF_GUID]

    async def handle_send(call: ServiceCall):
        title = call.data.get("title")
        description = call.data.get("message", "")
        pictureLink = call.data.get("pictureLink")
        icon = call.data.get("icon")
        actionLink = call.data.get("actionLink")
        isAlert = call.data.get("isAlert", False)

        payload = {
            "guid": guid,
            "title": title,
            "description": description,
            "pictureLink": pictureLink,
            "icon": icon,
            "actionLink": actionLink,
            "isAlert": isAlert,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(server_url, json=payload) as resp:
                if resp.status != 200:
                    hass.logger.error("OpenNotification failed: %s", await resp.text())

    hass.services.async_register(DOMAIN, "send", handle_send, schema=SERVICE_SEND_SCHEMA)

    return True
