#!/usr/bin/python3
import datetime
import time
import pybitflyer
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api = pybitflyer.API(api_key='API_KEY', api_secret='API_SECRET')

http = urllib3.PoolManager()
LOT = 0.001

def order(side, size):
    print(api.sendchildorder(product_code="FX_BTC_JPY", child_oider_type="MARKET",
          minute_to_expire=60, side=side, size=size))

while True:
    txt = str(http.request('GET', 'https://twitter.com/bitFlyer').data.decode('utf-8'))[:200000]
    for t in ['剥離', 'SFD']:
          start = txt.find(t)
          print(txt[start:start+200])
          if t in txt:
               print('Yuzo Canon Sell')
               order('SELL', LOT)
               #time.sleep(13*30*60)
               time.sleep(3)
               print('Yuzo Canon Buy')
               order('BUY', LOT)
    time.sleep(2)

