#171
price_list = [32100, 32150, 32000, 32500]
for price in range(len(price_list)):
    print(price_list[price])

#172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print("{} {}".format(i, price_list[i]))

#173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print("{} {}".format((len(price_list) - 1) - i, price_list[i]))

#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, len(price_list)):
    print("{} {}".format((90 + (i * 10)), price_list[i]))

#175
my_list = ['a', 'b', 'c', 'd']
for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

#176
my_list = ['a', 'b', 'c', 'd', 'e']
for i in range(2, len(my_list)):
    print(my_list[i-2], my_list[i-1], my_list[i])

#177
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1] - my_list[i])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print(sum(my_list[i:i+3]) / 3)

#180
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append((high_prices[i]-low_prices[i]))
print(volatility)
