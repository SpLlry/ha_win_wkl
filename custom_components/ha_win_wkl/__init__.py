import asyncio
import json
import requests
from homeassistant import config_entries, core
from .const import (
    DOMAIN
)
import logging
import subprocess
from datetime import timedelta
from .utils import ping_ip
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryNotReady

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [
    "switch",
]


async def async_setup(hass: core.HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass, entry):
    _LOGGER.debug("Setting up My Device component")
    ip = entry.data.get('ip')
    name = entry.data.get('name')
    mac = entry.data.get('mac')
    account = entry.data.get('account')

    # result = subprocess.run(["ping", "-n", "1", "-w", "1000", ip], capture_output=True, text=True)

    if ping_ip(ip):
        status = "0"
    else:
        status = "-1"

    _LOGGER.debug(f"获取初始化信息完成，开始创建设备IP: {ip}, Name:{name}, Mac:{mac}, Status: {status}")

    coordinator = DEVICEDataUpdateCoordinator(hass, entry, ip, name, mac, status)

    await coordinator.async_refresh()
    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][ip] = coordinator

    _LOGGER.info(f"创建设备完成IP: {ip}, Name:{name}, Mac:{mac}, Status: {status}")

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def update_listener(hass, entry):
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    return unload_ok


class DEVICEDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching DEVICE data."""

    def __init__(self, hass, entry, ip, name, mac, status):
        # 使用 update_interval 的代码

        self.hass = hass
        self.entry = entry

        self.ip = ip
        self.name = name
        self.mac = mac
        self.status = status

        self._isenable = True

        super().__init__(
            hass,
            _LOGGER,
            name=self.name,
            update_interval=timedelta(minutes=10),
        )

    def set_device_enabled(self, enabled):
        # 设置设备是否可用
        self._isenable = enabled

    async def _async_update_data(self):
        """Fetch data from My Custom Device."""
        try:
            if ping_ip(self.ip):
                self.status = "0"
            else:
                self.status = "-1"
            return json.loads('{"ip":"' + self.ip
                              + '","name":"' + self.name
                              + '","status":"' + self.status + '"}')
        except Exception as err:
            raise UpdateFailed(f"Error communicating with My Custom Device: {err}")
