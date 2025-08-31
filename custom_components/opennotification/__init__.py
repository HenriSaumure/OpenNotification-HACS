from homeassistant.core import HomeAssistant, ServiceCall
import aiohttp
import asyncio
from .const import DOMAIN, CONF_SERVER, CONF_GUID

async def async_setup_entry(hass: HomeAssistant, entry):
    server_url = entry.data[CONF_SERVER]
    guid = entry.data[CONF_GUID]

    async def handle_send(call: ServiceCall):
        payload = {
            "guid": guid,
            "title": call.data.get("title"),
            "description": call.data.get("description"),
            "pictureLink": call.data.get("pictureLink"),
            "icon": call.data.get("icon"),
            "actionLink": call.data.get("actionLink"),
            "isAlert": call.data.get("isAlert", False),
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(server_url, json=payload) as resp:
                if resp.status != 200:
                    hass.logger.error("OpenNotification failed: %s", await resp.text())

    hass.services.async_register(DOMAIN, "send", handle_send)

    # Register as notify platform
    hass.services.async_register('notify', 'opennotification', handle_send)

    return True
