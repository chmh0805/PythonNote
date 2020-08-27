#91
inventory = {
'Merona': [300, 20],
'Bibibik': [400, 3],
'Shark': [250, 100]
}
print(inventory)

#92
print('{} won'.format(inventory['Merona'][0]))

#93
inventory = {
'Merona': [300, 20],
'Bibibik': [400, 3],
'Shark': [250, 100]
}
print("Merona count : {}".format(inventory['Merona'][1]))

#94
inventory['World'] = [500, 7]
print(inventory)

#95
icecream = {'Tank': 1200, 'Polapo': 1200, 'Bbangbare': 1800, 'World': 1500, 'Merona': 1000}
icecream_list = list(icecream.keys())
print(icecream_list)

#96
icecream_values = list(icecream.values())
print(icecream_values)

#97
print(sum(icecream_values))

#98
new_product = {'Pot': 2700, 'Amatna': 1000}
icecream.update(new_product)
print(icecream)

#99
keys = ("apple", 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
