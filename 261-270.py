#261
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        print(self.name)

    def get_code(self):
        print(self.code)

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, 배당수익률):
        self.배당수익률 = 배당수익률

'''
#262
samsung = Stock('삼성전자', '005930')
print(samsung.name)

#263
a = Stock(None, None)
a.set_name('삼성전자')
print(a.name)

#264
a.set_code('005930')
print(a.code)

#265
a.get_name()
a.get_code()
'''
#266

#267
s = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
print(s.per)

#268

#269
s.set_per(12.75)
print(s.per)

#270
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
hyundai = Stock('현대차', '005380', 8.70, 0.35, 4.27)
lg = Stock('LG전자', '066570', 317.34, 0.69, 1.37)
company_list = [samsung, hyundai, lg]

for i in company_list:
    i.get_code()
    print(i.per)
