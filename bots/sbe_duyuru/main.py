from datetime import datetime
import telegram
import asyncio
import json
import feedparser
import os

FILE = "./announcement.txt"

def read_announcement_info():
    date_info = []
    try:
        with open(FILE, 'r') as f:
            date_info = json.load(f)
    except:
        pass
    return date_info


def parse_rss_announcement():
    rss_url = 'https://sbe.deu.edu.tr/news-category/duyurular/feed/'
    announcement_feed = feedparser.parse(rss_url)

    entry_list = []
    for item in announcement_feed.entries:
        entry_dict = {}
        entry_dict['title'] = item.title
        entry_dict['link'] = item.link
        entry_dict['updated'] = item.updated
        entry_list.append(entry_dict)
    return entry_list


def change_date_format(entry_list):
    rss_date_format = "%a, %d %b %Y %H:%M:%S %z"
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    updated_date_list = []
    for i in entry_list:
        dt = datetime.strptime(i['updated'], rss_date_format)
        dt_str = dt.strftime(new_date_format)
        i['updated'] = dt_str
        updated_date_list.append(i)
    return updated_date_list


def store_date(updated_date_list):
    if len(updated_date_list) != 0:
        with open(FILE, 'w') as f:
            json.dump(updated_date_list[0]['updated'], f)


def compare_date_info(date_info, updated_date_list):
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    new_list = []
    if date_info != '':
        for i in range(len(updated_date_list)):
            if updated_date_list[i]['updated'] > date_info:
                new_list.append(updated_date_list[i])
    else:
        for i in range(len(updated_date_list)):
            new_list.append(updated_date_list[i])
    sorted_date_list = sorted(new_list, key=lambda x: datetime.strptime(x['updated'], new_date_format))
    return sorted_date_list


def add_ascape_chararacter(sorted_date_list):
    unsupported = '_*[`'
    for item in sorted_date_list:
        for chr in unsupported:
            item['title'] = item['title'].replace(chr, '\\' + chr)

    return sorted_date_list

def format_message(sorted_date_list):
    msg_list = []
    for i in sorted_date_list:
        title = i['title']
        link = i['link']
        date = i['updated']
        old_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        new_date_format = "%d-%m-%Y  %H:%M:%S"
        format_date = datetime.strptime(date, old_date_format)
        format_date = format_date.strftime(new_date_format)
        msg_list.append(f'📣 [{title}]({link})\n\n🗓 *Duyuru tarihi:* {format_date}\n')
    return msg_list


async def send_message(bot, msg_list):
    for i, msg in enumerate(msg_list):
        await bot.sendMessage(CHAT_ID, msg, parse_mode = telegram.constants.ParseMode.MARKDOWN,
                              disable_notification = True)
        if (i+5) % 5 == 0:
            await asyncio.sleep(60)


if __name__ == '__main__':
    CHAT_ID = os.getenv('CHAT_ID')
    TOKEN = os.getenv('TOKEN')

    if CHAT_ID != None and TOKEN != None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot = telegram.Bot(TOKEN)

        date_info = read_announcement_info()
        parse = parse_rss_announcement()
        updated_date = change_date_format(parse)
        store_date(updated_date)
        updated_entry_list = compare_date_info(date_info, updated_date)
        chr = add_ascape_chararacter(updated_entry_list)
        msg = format_message(chr)
        loop.run_until_complete(send_message(bot, msg))
    else:
        raise SystemExit('Make sure you define chat id and token')