import settings
from telethon.client.telegramclient import TelegramClient
import asyncio


loop = asyncio.get_event_loop()


async def main():
	client = None
	if settings.use_proxy:
		client = TelegramClient('telegramFileUploader', settings.api_id, settings.api_hash, proxy = settings.proxy_data)
	else:
		client = TelegramClient('telegramFileUploader', settings.api_id, settings.api_hash)
	await client.start()
	
	dialogs = await client.get_dialogs()
	
	for dialog in dialogs:
		print("%s - %s" % (dialog.name, dialog.entity.id))
	


loop.run_until_complete(main())