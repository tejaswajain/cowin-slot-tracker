import requests
import datetime
import json
from telethon import TelegramClient

api_id = 
api_hash = ''
bot_token = ''

MESSAGE = "{address} : {capacity} :  {vaccine} : {date}"


def seek_slots_info():
    """To get the list of open slots for the next 3 days
    """
    final_data = []
    api_endpoint = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    # get list of dates for next 3 days
    date_list = [datetime.datetime.today() + datetime.timedelta(days=x)
                 for x in range(3)]
    api_date_string = [x.strftime("%d-%m-%Y") for x in date_list]

    for check_date in api_date_string:
        response = requests.get(api_endpoint, headers=header, params={
            'district_id': 315, 'date': check_date
        })
        if response.ok and ('sessions' in json.loads(response.text)):
            json_response = json.loads(response.text).get('sessions')
            for index, value in enumerate(json_response):
                if value.get("available_capacity") > 3 and value.get("min_age_limit") < 45:
                    final_data.append(MESSAGE.format(address=value.get('address'), capacity=value.get(
                        'available_capacity'), vaccine=value.get('vaccine'), date=value.get('date')))
    if len(final_data) > 0:
        msg = '\n'.join(final_data)
        return msg
    
async def send_telegram_notification(bot_object, message):
    """To send notification in telegram
    """
    entity = await bot_object.get_entity('tejaswajain')
    await bot_object.send_message(entity=entity, message=message)

if __name__ == "__main__":
    result = seek_slots_info()
    if result:
        print("Got data")
        bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
        with bot:
            bot.loop.run_until_complete(send_telegram_notification(bot, result))
