import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from time import mktime
import telegram
import asyncio
import requests
from datetime import datetime
import json
import datetime
import os


ID_FILE = './eventid.json'


def read_stored_ids():
    ids_info = []
    try:
        with open(ID_FILE, "r") as f:
            ids_info = json.load(f)
    except:
        pass
    return ids_info


def get_requests():
    end_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    start_time = (datetime.datetime.now() - timedelta(hours=24)
                  ).strftime("%Y-%m-%dT%H:%M:%S")
    url = f"https://deprem.afad.gov.tr/apiv2/event/filter?minlat=36&maxlat=42&minlon=26&maxlon=45&start={start_time}&end={end_time}&minmag=4&format=xml"
    response = requests.get(url).text
    #with open("filter.xml", "r") as f:
    #    response = f.read()
    return response


def parse(response):
    tree = ET.ElementTree(ET.fromstring(response))
    root = tree.getroot()

    namespace = "{http://schemas.datacontract.org/2004/07/EventAPIv2.Model}"
    earthquake_list = []
    for earthquake in root.findall(f"{namespace}Earthquake"):
        entry_dict = {}
        entry_dict['country'] = earthquake.find(f"{namespace}Country").text
        entry_dict['date'] = earthquake.find(f"{namespace}Date").text
        entry_dict['depth'] = earthquake.find(f"{namespace}Depth").text
        entry_dict['eventid'] = earthquake.find(f"{namespace}EventID").text
        entry_dict['latitude'] = earthquake.find(f"{namespace}Latitude").text
        entry_dict['location'] = earthquake.find(f"{namespace}Location").text
        entry_dict['longitude'] = earthquake.find(f"{namespace}Longitude").text
        entry_dict['magnitude'] = earthquake.find(f"{namespace}Magnitude").text
        entry_dict['province'] = earthquake.find(f"{namespace}Province").text
        earthquake_list.append(entry_dict)
    return earthquake_list


def unique_earthquake_list(earthquake_list):
    unique_earthquake_list = []
    unique_ids = set()

    for item in earthquake_list:
        if item['eventid'] not in unique_ids:
            unique_ids.add(item['eventid'])
            unique_earthquake_list.append(item)
        else:
            continue

    return unique_earthquake_list


def compare_eventid(ids_info, unique_earthquake_list):
    new_earthquake_list = []
    if ids_info != []:
        for item1 in unique_earthquake_list:
            for item2 in ids_info:
                if item1['eventid'] == item2['eventid']:
                    break
            else:
                pub_time = datetime.datetime.fromtimestamp(mktime(
                    datetime.datetime.strptime(item1["date"], '%Y-%m-%dT%H:%M:%S').timetuple()))
                if pub_time >= (datetime.datetime.now() - timedelta(hours=24)):
                    new_earthquake_list.append(item1)
    else:
        new_earthquake_list = unique_earthquake_list

    return new_earthquake_list


def write_to_earthquake_list(ids_info, new_earthquake_list):
    combined_info = ids_info + new_earthquake_list
    with open(ID_FILE, "w") as f:
        json.dump(combined_info, f, indent=2)
    return new_earthquake_list

def remove_unsupported_characters(new_earthquake_list):
    for item in new_earthquake_list:
        item['location'] = item['location'].replace("[", "").replace("]", "")
        item['country'] = item['country'].replace("[", "").replace("]", "")
    return new_earthquake_list


def format_message(new_earthquake_list):
    msg_list = []
    notif = False
    for eartquake in new_earthquake_list:
        #if eartquake['country'] == "Bulgaristan" or eartquake['country'] == 'İran' or \
        #   eartquake['country'] == "Irak" or eartquake['country'] == 'Yunanistan' or \
        #   eartquake['country'] == 'Ermenistan' or eartquake['country'] == 'Suriye' or \
        #   eartquake['country'] == "Gürcistan" or eartquake['country'] == "Azerbaycan":
        #    continue
        date = eartquake['date']
        date_format = '%Y-%m-%dT%H:%M:%S'
        dates = datetime.datetime.strptime(date, date_format)
        new_date = dates + datetime.timedelta(hours=3)
        depth = eartquake['depth']
        latitude = eartquake['latitude']
        longitude = eartquake['longitude']
        location = eartquake['location']
        magnitude = float(eartquake['magnitude'])
        if magnitude >= 7:
            color_code = "⚫️"
        elif magnitude >= 6:
            color_code = "🔴"
        elif magnitude >= 5:
            color_code = "🟠"
        elif magnitude >= 4:
            color_code = "🟡"
        notif = magnitude < 5
        msg_list.append(
            f'{color_code} *{magnitude}* - [{location}](https://www.google.com/maps/@?api=1&map_action=map&basemap=satellite&center={latitude},{longitude}&zoom=12)\n\n'
            f'🕐 *Tarih:* {new_date}\n🌍 *Yer:* {latitude}, {longitude}\n⬇️ *Derinlik:* {depth} km')
    return msg_list, notif


async def send_message(bot, msg_list, notif):
    for i, msg in enumerate(msg_list):
        await bot.sendMessage(CHAT_ID, msg, parse_mode=telegram.constants.ParseMode.MARKDOWN,
                                disable_notification=notif)
        if (i+1) % 5 == 0:
            await asyncio.sleep(60)


if __name__ == '__main__':
    CHAT_ID = os.getenv('CHAT_ID')
    TOKEN = os.getenv('TOKEN')

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    if CHAT_ID != None and TOKEN != None:
        bot = telegram.Bot(TOKEN)

        stored = read_stored_ids()
        response = get_requests()
        feed = parse(response)
        new_id = compare_eventid(stored, feed)
        write_to_earthquake_list(stored, new_id)
        unsupported_chr = remove_unsupported_characters(new_id)
        msg, notif = format_message(unsupported_chr)
        loop.run_until_complete(send_message(bot, msg, notif))
    else:
        raise SystemExit("Make sure you define chat id and token.")