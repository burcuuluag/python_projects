from datetime import timedelta, datetime
from time import mktime
import feedparser
import asyncio
import json
import telegram
import os


ID_FILE = "./ids.json"


def read_stored_ids():
    ids_info = []
    try:
        with open(ID_FILE, "r") as f:
            ids_info = json.load(f)
    except:
        pass
    return ids_info


def get_feed_rss():
    rss_url = "https://news.google.com/rss/topics/CAAqJAgKIh5DQkFTRUFvS0wyMHZNSFl3YUhRM2NoSUNaVzRvQUFQAQ?hl=tr-TR&gl=TR&ceid=TR%3Atr"
    news_feed = feedparser.parse(rss_url)

    entry_list = []
    for item in news_feed.entries:
        entry_dict = {}
        entry_dict["title"] = item.title
        entry_dict["link"] = item.link
        entry_dict["guid"] = item.guid
        entry_dict["published"] = item.published
        entry_dict["published_parsed"] = item.published_parsed
        entry_list.append(entry_dict)
    return entry_list


def compare_ids(ids_info, entry_list):
    new_id_list = []
    if ids_info != None:
        for item1 in entry_list:
            for item2 in ids_info:
                if item1["guid"] == item2["guid"]:
                    break
            else:
                pub_time = datetime.fromtimestamp(
                    mktime(item1["published_parsed"]))
                if pub_time >= (datetime.now() - timedelta(hours=24)):
                    new_id_list.append(item1)
    else:
        new_id_list = entry_list

    return new_id_list


def write_new_id_json_file(ids_info, new_id_list):
    combined_entry = ids_info + new_id_list
    with open(ID_FILE, "w") as f:
        json.dump(combined_entry, f, indent=2)
    return new_id_list


def format_message(new_id_list):
    msg_list = []
    for i in new_id_list:
        title = i["title"]
        link = i["link"]
        msg_list.append(f"[{title}]({link})\n")

    return msg_list


async def send_message(bot, msg_list):
    for i, msg in enumerate(msg_list):
        await bot.sendMessage(CHAT_ID, msg, parse_mode=telegram.constants.ParseMode.MARKDOWN,
                              disable_notification=True)
        if (i+1) % 5 == 0:
            await asyncio.sleep(60)

if __name__ == '__main__':
    CHAT_ID = os.getenv('CHAT_ID')
    TOKEN = os.getenv('TOKEN')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    if CHAT_ID != None and TOKEN != None:
        bot = telegram.Bot(TOKEN)

        stored_id = read_stored_ids()
        current_id = get_feed_rss()
        new_ids = compare_ids(stored_id, current_id)
        write = write_new_id_json_file(stored_id, new_ids)
        message = format_message(write)
        loop.run_until_complete(send_message(bot, message))
    else:
        raise SystemExit("Make sure you define chat id and token.")
