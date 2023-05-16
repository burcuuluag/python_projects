from datetime import datetime, timedelta
import requests
import asyncio
import telegram
import locale
import json
import os


API_KEY = 'API_KEY'
CITY = 'Izmir'
COUNTRY = 'TR'
UNITS = 'metric'
FILE = 'message_list.json'

WEATHER_EMOJIS = {
    "kapalı": "☁️",
    "yağmurlu": "🌧",
    "açık": "☀️",
    "güneşli": "☀️",
    "parçalı bulutlu": "⛅️",
    "çok bulutlu": "☁️",
    "az bulutlu": "☁️",
    "sisli": "🌫",
    "çiseliyor": "☔️",
    "rüzgarlı": "🌬",
    "sağanak yağmur": "☔️",
    "gökgürültülü fırtına": "🌩",
    "karlı": "❄️",
    "sulu kar": "🌨",
    "parçalı az bulutlu": "🌤",
    "hafif yağmur": "🌧"
}


def get_weather_forecast():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY},{COUNTRY}&units={UNITS}&lang=tr&appid={API_KEY}"
    response = requests.get(url).json()
    #with open('weather.json', 'w') as f:   #DOSYAYA YAZDIRMAYI SİL!
    #    response = json.dump(response, f)
    return response

    #with open('weather.json', 'r') as file:
    #    response = json.load(file)
    #return response


def get_items(response):
    forecast_list = []
    for item in response['list']:
        forecast = {}
        forecast['date'] = item['dt_txt'].split(' ')[0]
        forecast['time'] = item['dt_txt'].split(' ')[1]
        forecast['temp'] = item['main']['temp']
        forecast['description'] = item['weather'][0]['description']
        forecast['wind'] = item['wind']['speed']
        forecast['humidity'] = item['main']['humidity']
        forecast_list.append(forecast)
    return forecast_list


def convert_wind_speed_mps_to_kmph(forecast_list):
    for item in forecast_list:
        item['wind'] = round(item['wind'] * 3.6, 2) #birim (m/saniye)dir. km/saat'e doğrudan dönüştüremeyiz. önce km/saniyeye çevir. m/saniye * 3.6 yapmalıyız. 
    return forecast_list


def find_max_and_min_temp(forecast_list):
    today = datetime.today().strftime('%Y-%m-%d')
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    next_day = (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')

    message_list = []
    for date in [today, tomorrow, next_day]:
        highest_temp = None
        lowest_temp = None
        for item in forecast_list:
            if item['date'] == date:
                if highest_temp is None or item['temp'] > highest_temp:
                    highest_temp = item['temp']
                    highest_temp_item = item
                if lowest_temp is None or item['temp'] < lowest_temp:
                    lowest_temp = item['temp']
                    lowest_temp_item = item
        message_list.append({'highest_temp': highest_temp_item, 'lowest_temp': lowest_temp_item})

    return message_list


def write_to_message_list(message_list):
    with open(FILE, 'w+') as f:
        f.truncate(0)   #dosyanın içeriğini silmek için kullanılır
        json.dump(message_list, f, indent=2)
    return message_list


def format_message(message_list):
    locale.setlocale(locale.LC_TIME, 'tr_TR.utf-8')
    msg_list = []
    for item in message_list:
        h_date = item['highest_temp']['date']
        old_date_format = '%Y-%m-%d'
        new_date_format = '%d %B %Y'
        format_date = datetime.strptime(h_date, old_date_format)
        h_format_date = format_date.strftime(new_date_format)
        h_temp = item['highest_temp']['temp']
        l_temp = item['lowest_temp']['temp']
        h_description = item['highest_temp']['description']
        emoji = WEATHER_EMOJIS.get(h_description, "")
        h_wind = item['highest_temp']['wind']
        h_humidity = item['highest_temp']['humidity']
        msg_list.append(f'🌤 Hava Durumu Tahmini - {h_format_date}\n\n'
                f'🌡 *En Yüksek Sıcaklık:* {h_temp}°C\n'
                f'🌡 *En Düşük Sıcaklık:* {l_temp}°C\n'
                f'🌤 *Beklenen Hadise:* {emoji} {h_description}\n'
                f'🌬 *Rüzgar Hızı:* {h_wind} km/sn\n'
                f'💧 *Nem:* %{h_humidity}\n\n')
    return msg_list


async def send_message(msg_list):
    message = "".join(msg_list)
    await bot.sendMessage(CHAT_ID, message, parse_mode=telegram.constants.ParseMode.MARKDOWN)


if __name__ == '__main__':
    CHAT_ID = os.getenv('CHAT_ID')
    TOKEN = os.getenv('TOKEN')

    if CHAT_ID != None and TOKEN != None:
        bot = telegram.Bot(TOKEN)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        response = get_weather_forecast()
        items = get_items(response)
        km_per_secand = convert_wind_speed_mps_to_kmph(items)
        msg_list = find_max_and_min_temp(km_per_secand)
        write = write_to_message_list(msg_list)
        msg = format_message(write)
        loop.run_until_complete(send_message(msg))
    else:
        raise SystemExit("Make sure you define chat id and token.")