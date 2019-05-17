import settings
from telethon.client.telegramclient import TelegramClient
import asyncio
import sys


help = "Usage: python main.py <mode> <chat_id> <filename>\nwhere mode is:\n--get-chats  -  get chat list for obtaining chat id\n--upload-file  -  upload file to specified chat"

if len(sys.argv) == 1:
	print(help)
	sys.exit()
	
loop = asyncio.get_event_loop()

async def main():
	client = None
	if settings.use_proxy:
		client = TelegramClient('telegramFileUploader', settings.api_id, settings.api_hash, proxy = settings.proxy_data)
	else:
		client = TelegramClient('telegramFileUploader', settings.api_id, settings.api_hash)
	await client.start()

	if sys.argv[1] == "--get-chats":
		dialogs = await client.get_dialogs()
		for dialog in dialogs:
			print("%s - %s" % (dialog.name, dialog.entity.id))
	
	elif sys.argv[1] == "--upload-file":
		chat_id = sys.argv[2]
		filename = sys.argv[3]
		entity = None
		dialogs = await client.get_dialogs()
		for dialog in dialogs:
			id = str(dialog.entity.id)
			if id == chat_id:
				entity = dialog.entity
				break
		if not entity:
			print("chat with id %s not found" % chat_id)
			sys.exit(1)
		result = await client.send_file(entity, filename)
# 		print(result)


loop.run_until_complete(main())