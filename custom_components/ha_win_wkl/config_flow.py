"""
Hass.io My Custom Switch Plugin Config Flow
"""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

from homeassistant.components.http.view import HomeAssistantView
from aiohttp import web


@config_entries.HANDLERS.register(DOMAIN)
class MyCustomSwitchFlowHandler(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        errors = {}
        if DOMAIN in self.hass.data:
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:
            # 在这里处理传入的参数，并验证其有效性
            # 如果参数有效，可以保存并跳转到下一步
            return self.async_create_entry(title="电脑唤醒插件-配置", data=user_input)

        # 在这里创建一个配置表单页面，让用户填写参数
        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                vol.Required("ip", default=""): str,
                vol.Required("name", default=""): str,
                vol.Required("mac", default=""): str,
                vol.Required("account", default=""): str,
            })
        )
