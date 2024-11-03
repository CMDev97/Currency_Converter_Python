import requests
import json

cache = {}


def load_dictionary(currency_from):
    r = requests.get(f"http://www.floatrates.com/daily/{currency_from}.json")
    if r.status_code == 200:
        return json.loads(r.text)
    return {}


def load_on_cache(extract_value, dictionary_response):
    global cache
    if extract_value in dictionary_response:
        cache[extract_value.upper()] = dictionary_response[extract_value]['rate']


def print_cache(final_amount, currency):
    print("Oh! It is in the cache!")
    print(f"You received {final_amount:.2f} {currency}.")


def print_not_in_cache(final_amount, currency):
    print("Sorry, but it is not in the cache!")
    print(f"You received {final_amount:.2f} {currency}.")


end_currency = input().lower()
tmp_dict = load_dictionary(end_currency)
load_on_cache('eur', tmp_dict)
load_on_cache('usd', tmp_dict)

while True:
    start_currency = input().lower()
    if start_currency == "":
        break
    amount = float(input())

    print("Checking the cache...")

    if start_currency.upper() in cache:
        rate = cache[start_currency.upper()]
        print_cache(amount*rate, start_currency)
    else:
        tmp_dict = load_dictionary(end_currency)
        load_on_cache(start_currency, tmp_dict)
        rate = cache[start_currency.upper()]
        print_not_in_cache(amount * rate, start_currency)
