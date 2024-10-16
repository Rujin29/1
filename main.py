import json
import requests
import matplotlib.pyplot as plt

# Запрос к API НБУ
url_string = "https://bank.gov.ua/NBU_Exchange/exchange_site?json&start=20241007&end=20241011&valcode=usd"
my_response = requests.get(url_string)

# Проверка статуса запроса
if my_response.status_code == 200:
    response_json = json.loads(my_response.content)

    # Сбор дат и курсов
    dates = []
    rates = []

    for item in response_json:
        dates.append(item['exchangedate'])
        rates.append(item['rate'])

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b')

    # Оформление графика
    plt.title('Exchange Rate of USD (NBU)', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Exchange Rate (UAH)', fontsize=12)
    plt.xticks(rotation=45)  # Поворот подписей по оси X для лучшей читаемости
    plt.grid(True)

    # Показ графика
    plt.tight_layout()
    plt.show()
else:
    print("Error: Unable to fetch data")


