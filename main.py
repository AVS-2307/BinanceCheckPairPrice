import requests
import json
import time

base = 'https://fapi.binance.com'
path = '/fapi/v1/ticker/price'

url = base + path
param = {'symbol': 'XRPUSDT'}

list_ = []

while True:
    if len(list_) <= 3600:
        r = requests.get(url, params=param)
        if r.status_code == 200:
            data = r.json()
        else:
            print('error')

        list_.append(float(data['price']))
        for i in range(0, len(list_)-1):
            if list_[i+1] / list_[i] <= 0.01:
                print('Падение цены на 1%')
            i += 1
    else:
        list_.pop(0)

    #print(list_)
    time.sleep(1)



