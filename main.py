import json
import requests

url_string = "https://bank.gov.ua/NBU_Exchange/exchange_site?json&start=20241007&end=20241011&valcode=usd"

my_responce = requests.get(url_string)

print(my_responce)
print(my_responce.content)

responce_json = json.loads(my_responce.content)

print(responce_json)

for item in responce_json:
    print(item['rate'])

