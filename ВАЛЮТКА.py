import json
import requests
def get_exchange_rates(currency):
    r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    r_js = json.loads(r.text)
    value = r_js["Valute"][currency]["Value"]
    nominal = r_js["Valute"][currency]["Nominal"]
    return value / nominal
def get_result(count, name):
    exchange_rate = get_exchange_rates(name)
    curr_to_rub = round(count * exchange_rate, 2)
    rub_to_curr = round(count / exchange_rate, 2)
    return curr_to_rub, rub_to_curr
def generate_text(count, name):
    curr_to_rub, rub_to_curr = get_result(count, name)
    return f'''
    {charged_curr_count} {charged_curr_name} = {curr_to_rub} RUB
    {charged_curr_count} RUB = {rub_to_curr} {charged_curr_name}
    '''
def print_currencies():
    r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    r_js = json.loads(r.text)
    for currency in r_js["Valute"]:
        print(currency, r_js["Valute"][currency]["Name"])
charged_curr_count = abs(float(input('Введите количество: ')))
charged_curr_name = str(input('Введите код валюты [EUR, USD, SEK..(?)]: '))
if charged_curr_name == "?":
    print_currencies()
    charged_curr_name = str(input('Введите код валюты: '))
print(generate_text(charged_curr_count, charged_curr_name))
