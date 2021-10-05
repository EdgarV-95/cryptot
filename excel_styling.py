import pandas as pd
import main

df = pd.read_excel(main.merged_data_location)
df['Buy Zone 1'] = df['BTC price'] / df['Buy1A'].astype(float)
df['Buy Zone 2'] = df['BTC price'] / df['Buy1B'].astype(float)
df['Buy Zone 3'] = df['BTC price'] / df['Buy2A'].astype(float)
df['Buy Zone 4'] = df['BTC price'] / df['Buy2B'].astype(float)

status_tracker = 1

df_styled = df.style\
    .applymap(lambda x: 'background-color: %s' % 'green' if x < status_tracker else 'background-color: %s' % 'red', subset=['Buy Zone 1'])\
    .applymap(lambda x: 'color: %s' % 'green' if x < status_tracker else 'color: %s' % 'red', subset=['Buy Zone 1'])\
    .applymap(lambda x: 'background-color: %s' % 'green' if x < status_tracker else 'background-color: %s' % 'red', subset=['Buy Zone 2'])\
    .applymap(lambda x: 'color: %s' % 'green' if x < status_tracker else 'color: %s' % 'red', subset=['Buy Zone 2'])\
    .applymap(lambda x: 'background-color: %s' % 'green' if x < status_tracker else 'background-color: %s' % 'red', subset=['Buy Zone 3'])\
    .applymap(lambda x: 'color: %s' % 'green' if x < status_tracker else 'color: %s' % 'red', subset=['Buy Zone 3'])\
    .applymap(lambda x: 'background-color: %s' % 'green' if x < status_tracker else 'background-color: %s' % 'red', subset=['Buy Zone 4'])\
    .applymap(lambda x: 'color: %s' % 'green' if x < status_tracker else 'color: %s' % 'red', subset=['Buy Zone 4'])\

df_styled.to_excel('C:\\Users\\veres\\Desktop\\CryptoTrading\\Latest_Crypto_list.xlsx', engine='openpyxl', index=False)