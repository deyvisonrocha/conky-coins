import urllib
import requests
import babel.numbers, decimal

bitcoin = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=BRL"
btc_res = requests.get(bitcoin)
btc_data = btc_res.json()[0]
btc_price = babel.numbers.format_currency(decimal.Decimal(btc_data['price_usd']), '')
btc_brl_price = babel.numbers.format_currency(decimal.Decimal(btc_data['price_brl']), 'BRL')

file = open('/home/deyvison/.conky/Rocks/bitcoin.txt','w')
file.write('$'+btc_price+'\n')
file.write(btc_data['percent_change_24h']+'%'+'\n')
file.write(btc_brl_price+'\n')
file.write(btc_data['rank']+'\n')
file.close()

raiblocks = "https://api.coinmarketcap.com/v1/ticker/raiblocks/?convert=BRL"
xrb_res = requests.get(raiblocks)
xrb_data = xrb_res.json()[0]
xrb_price = babel.numbers.format_currency(decimal.Decimal(xrb_data['price_usd']), '')
xrb_btc_price = xrb_data['price_btc']
xrb_brl_price = babel.numbers.format_currency(decimal.Decimal(xrb_data['price_brl']), 'BRL')

file = open('/home/deyvison/.conky/Rocks/raiblocks.txt','w')
file.write('$'+xrb_price+'\n')
file.write(xrb_data['percent_change_24h']+'%'+'\n')
file.write(xrb_btc_price+'\n')
file.write(xrb_brl_price+'\n')
file.write(xrb_data['rank']+'\n')
file.close()