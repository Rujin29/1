import requests

from urllib3 import request

url_string = "https://bank.gov.ua/NBU_Exchange/exchange_site?json&start=20241007&end=20241011&valcode=usd"

requests.get(url_string)
