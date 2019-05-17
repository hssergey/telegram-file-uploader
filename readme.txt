Simple command-line tool for uploading files to telegram channels

Install:
1. Clone the repository
2. execute: cp settings.py.template settings.py
3. edit settings.py - set your own authentication keys
4. execute  python3 -m venv venv
5. execute: source venv/bin/activate
6. execute: pip install -r requirements.txt

Now it's ready to work


Usage: python main.py <mode> <chat_id> <filename>\nwhere mode is:
--get-chats  -  get chat list for obtaining chat id
--upload-file  -  upload file to specified chat