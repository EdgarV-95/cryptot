from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import xlrd

# Location variables
coinmarketcap_json_location = 'D:\\Coding\\Projects\\CryptoT\\coinkmarketcap_json.txt'
####################################################################################################
# Variables
df = pd.read_excel('C:\\Users\\veres\\Desktop\\CryptoTrading\\CryptoT_list.xlsx')
coin_list = df.iloc[:,10].tolist()
new_coins = []
for c in coin_list:
    new_coins.append(c)
list_of_coins = ','.join(new_coins)

# list_of_coins = 'IRIS,KAVA,ELF,STPT,KSM,FIO,RCN,TCT,BEAM,VET,RLC,BTS,WTC,IDEX,NULS,BAT,QKC,BLZ,COS,PNT'
api_key = '9b9d957b-fb98-46b3-89e2-9d2ef608aa42'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol': list_of_coins,
    'convert': 'USD',
    'aux': 'is_fiat'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  parseData = json.dumps(response.json())
  f = open(coinmarketcap_json_location, "w")
  f.write(parseData)
  f.close()
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)