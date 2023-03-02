import random
import json
import telegram
import os
import asyncio

FILE = "./moderator.json"

member_list = ["Eda Akyildiz", "Elif Altas", "Merve Ece Altinok",
               "Kaan Ay", "Serdar Barbaros", "Didem Bilgi",
               "Okan Celebi", "Mert Aydin Celik", "Osman Sinan Dincturk"]

def read_stored_moderator():
    moderator_names = []
    try:
        with open(FILE, 'r') as f:
            moderator_names = json.load(f)
            f.close()
    except:
        pass

    return moderator_names

def choose_random_moderator(moderator_names):
    remaining_members = list(set(member_list) - set(moderator_names))
    if remaining_members:
        weights = []
        for member in member_list:
            if member in remaining_members:
                weights.append(2)
            else:
                weights.append(1)
        moderator = random.choices(member_list, weights=weights)[0]
        message = f"*Moderator:* {moderator}"
        return message, [moderator]
    else:
        return None, []

def check_and_write_to_file(moderator_names, moderator_list):
    updated_moderator_names = moderator_names + moderator_list
    if len(updated_moderator_names) >= len(member_list):
        with open(FILE, "w"):
            pass
    else:
        with open(FILE, "w") as f:
            json.dump(updated_moderator_names, f, indent=2)

async def send_message(message):
    if MESSAGE_THREAD_ID != None:
        await bot.sendMessage(CHAT_ID, message, parse_mode=telegram.constants.ParseMode.MARKDOWN, 
                              disable_notification=True, message_thread_id=MESSAGE_THREAD_ID)
    else:
        await bot.sendMessage(CHAT_ID, message, parse_mode=telegram.constants.ParseMode.MARKDOWN,
                              disable_notification=True)


if __name__ == '__main__':
    CHAT_ID = os.getenv("CHAT_ID")
    TOKEN = os.getenv("TOKEN")
    MESSAGE_THREAD_ID = os.getenv("MESSAGE_THREAD_ID")

    if CHAT_ID != None and TOKEN != None:
        moderator_names = read_stored_moderator()
        message, moderator = choose_random_moderator(moderator_names)
        check_and_write_to_file(moderator_names, moderator)
        bot = telegram.Bot(TOKEN)
        asyncio.run(send_message(message))
    else:
        raise SystemExit("Chat id and token is None. Please check!")

