import requests
ADDRESS = 'bc1pf95gr6xhcg4alnzffd3wrg0z6xde3fhwceppvr6xn58u5xa86drsrm5yg2'
COIN = 'bitcoin'

url = f'https://api.blockchair.com/{COIN}/dashboards/address/{ADDRESS}?key=A___nBsJDbXc1imJ45CjYox9BBTHbaZ8'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    received_value = data['data'][ADDRESS]['address']['received_usd']
    print(f'На адресе {ADDRESS} получено {received_value} {COIN}')
else:
    print(f'Произошла ошибка при выполнении запроса: {response.status_code}')

import requests

# Установите свой API-ключ для Blockchair
api_key = "A___nBsJDbXc1imJ45CjYox9BBTHbaZ8"

# Вызов метода API /stats для получения текущей цены BTC в долларах
response = requests.get(f"https://api.blockchair.com/bitcoin/stats?apikey={api_key}")
if response.status_code == 200:
    data = response.json()
    btc_price = data["data"]["market_price_usd"]

    # Конвертируйте 100 долларов в BTC
    usd_amount = 100
    btc_amount = usd_amount / btc_price
    print(f"{usd_amount} USD = {btc_amount:.8f} BTC")
else:
    print("Ошибка при получении данных с Blockchair API")
