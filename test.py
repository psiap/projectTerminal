import requests
ADDRESS = 'bc1pf95gr6xhcg4alnzffd3wrg0z6xde3fhwceppvr6xn58u5xa86drsrm5yg2'
COIN = 'bitcoin'

url = f'https://api.blockchair.com/{COIN}/dashboards/address/{ADDRESS}'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    received_value = data['data'][ADDRESS]['address']['received_usd']
    print(f'На адресе {ADDRESS} получено {received_value} {COIN}')
else:
    print(f'Произошла ошибка при выполнении запроса: {response.status_code}')