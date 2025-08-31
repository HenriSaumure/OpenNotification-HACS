from homeassistant.core import HomeAssistant, ServiceCall
import aiohttp
import asyncio
from homeassistant.helpers import config_validation as cv
import voluptuous as vol
from .const import DOMAIN, CONF_SERVER, CONF_GUID

SERVICE_SEND_SCHEMA = vol.Schema({
    vol.Optional("title"): cv.string,
    vol.Optional("description"): cv.string,
    vol.Optional("pictureLink"): cv.string,
    vol.Optional("icon"): cv.string,
    vol.Optional("actionLink"): cv.string,
    vol.Optional("isAlert"): cv.boolean,
})

NOTIFY_SCHEMA = vol.Schema({
    vol.Required("message"): cv.string,
    vol.Optional("title"): cv.string,
    vol.Optional("data"): vol.Schema({
        vol.Optional("pictureLink"): cv.string,
        vol.Optional("icon"): cv.string,
        vol.Optional("actionLink"): cv.string,
        vol.Optional("isAlert"): cv.boolean,
    }),
})

async def async_setup_entry(hass: HomeAssistant, entry):
    server_url = entry.data[CONF_SERVER]
    guid = entry.data[CONF_GUID]

    async def handle_send(call: ServiceCall):
        if call.domain == 'notify':
            title = call.data.get('title', 'Home Assistant')
            description = call.data.get('message', '')
            data = call.data.get('data', {})
        else:
            title = call.data.get("title")
            description = call.data.get("description")
            data = call.data

        payload = {
            "guid": guid,
            "title": title,
            "description": description,
            "pictureLink": data.get("pictureLink"),
            "icon": data.get("icon"),
            "actionLink": data.get("actionLink"),
            "isAlert": data.get("isAlert", False),
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(server_url, json=payload) as resp:
                if resp.status != 200:
                    hass.logger.error("OpenNotification failed: %s", await resp.text())

    hass.services.async_register(DOMAIN, "send", handle_send, schema=SERVICE_SEND_SCHEMA)

    # Register as notify platform
    hass.services.async_register('notify', 'opennotification', handle_send, schema=NOTIFY_SCHEMA)

    return True
