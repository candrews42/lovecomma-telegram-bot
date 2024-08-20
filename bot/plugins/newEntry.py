from typing import Dict, Any
import aiohttp
from .plugin import Plugin

class NewEntryPlugin(Plugin):
    """
    A plugin to log Telegram bot messages to the user's field journal
    """
    def get_source_name(self) -> str:
        return "FieldJournalLogger"

    def get_spec(self) -> [Dict]:
        return [
            {
                "name": "log_telegram_message",
                "description": "Log a Telegram bot message to the user's field journal",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "The text of the Telegram bot message"}
                    },
                    "required": ["message"]
                }
            }
        ]

    async def execute(self, function_name: str, helper, **kwargs) -> Dict[str, Any]:
        if function_name != "log_telegram_message":
            raise ValueError(f"Unknown function: {function_name}")

        url = "https://p3mxly.buildship.run/newEntry"
        headers = {
            "Content-Type": "application/json"
        }

        body = {
            "message": kwargs["message"]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=body, headers=headers) as response:
                status = response.status
                try:
                    data = await response.json()
                except aiohttp.ContentTypeError:
                    data = await response.text()

        return {
            "status": status,
            "data": data
        }