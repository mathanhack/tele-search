import os
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
phone_number = os.environ['PHONE_NUMBER']

search_term = input("Enter search term: ")

with TelegramClient('anon', api_id, api_hash) as client:
    client.start(phone_number)
    
    dialogs = client.get_dialogs()

    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            result = client(SearchRequest(
                peer=dialog.input_entity,
                q=search_term,
                filter=InputMessagesFilterEmpty(),
                min_date=None,
                max_date=None,
                offset_id=0,
                add_offset=0,
                limit=100,
                max_id=0,
                min_id=0,
                hash=0
            ))
            for message in result.messages:
                print(f"{dialog.name}: {message.to_dict()}")
