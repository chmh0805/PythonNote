#41
ticker = "btc_krw"
upper_ticker = ticker.upper()
print(upper_ticker)

#42
ticker = "BTC_KRW"
lower_ticker = ticker.lower()
print(lower_ticker)

#43
print('hello'.capitalize())

#44
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#45
print(file_name.endswith(('xlsx', 'xls')))

#46
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#47
a = 'hello world'
print(a.split())

#48
ticker = "btc_krw"
print(ticker.split('_'))

#49
date = "2020-05-01"
print(date.split('-'))

#50
data = "039490             "
print(data.rstrip())
