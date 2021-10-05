import os
import json
import coinmarketcap
from forex_python.bitcoin import BtcConverter
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook

# Location variables
merged_data_location = 'D:\\Coding\\Projects\\CryptoT\\merged_excel.xlsx'
source_data_location = 'C:\\Users\\veres\\Desktop\\CryptoTrading\\CryptoT_list.xlsx'

with open(coinmarketcap.coinmarketcap_json_location, "r") as json_file:
    contents = json_file.read()
asciiContents = contents.encode("ascii", errors="ignore")
data = json.loads(asciiContents)

def convert_to_btc(usd_price):
    usd_to_btc = BtcConverter().convert_to_btc(usd_price, 'USD') * 100000000
    return int(usd_to_btc)
    # return '{:.8f}'.format(float(usd_to_btc)) --> if you want to return the satoshi format

coin_list = coinmarketcap.list_of_coins.split(',')

def coin_price_calculator(coins):
    coin_list = coins

    symbol_list = ['',]
    usd_price_list = ['',]
    btc_price_list = ['',]

    filepath = source_data_location
    wb = load_workbook(filepath)
    sheet = wb.active

    def create_new_column(column_letter):
        column_column_letter = sheet[column_letter]
        saved_data_column_letter= []
        for x in range(len(column_column_letter)):
            saved_data_column_letter.append(column_column_letter[x].value)
        return saved_data_column_letter

    BuyZone1A = create_new_column('D')
    BuyZone1B = create_new_column('E')
    BuyZone2A = create_new_column('F')
    BuyZone2B = create_new_column('G')
    FirstTarget = create_new_column('H')
    SecondTarget = create_new_column('I')
    StopOut = create_new_column('J')
    # ConfirmCoin = create_new_column('K')
    DateToday = create_new_column('L')

    for coin_name in range(len(coin_list)):
        symbol = data['data'][coin_list[coin_name]]['symbol']
        usd_price = data['data'][coin_list[coin_name]]['quote']['USD']['price']
        btc_price = convert_to_btc(usd_price)
        symbol_list.append(symbol)
        usd_price_list.append(usd_price)
        btc_price_list.append(btc_price)

    return zip(symbol_list, btc_price_list, usd_price_list, BuyZone1A, BuyZone1B, BuyZone2A, BuyZone2B, FirstTarget, SecondTarget, StopOut, DateToday) # ConfirmCoin )

final_file = coin_price_calculator(coin_list)

pd.DataFrame(final_file).to_excel(merged_data_location,
    header=['Symbol', 'BTC price', 'USD price', 'Buy1A', 'Buy1B', 'Buy2A', 'Buy2B', 'Target1', 'Target2', 'Stop', 'Date'], # 'CoinName',
    index=False)