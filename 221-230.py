#221
def print_reverse(word):
    print(word[::-1])

print_reverse('python')

#222
def print_score(some_list):
    print(sum(some_list) / len(some_list))

print_score([1, 2, 3])

#223
def print_even(some_list):
    for num in some_list:
        if num % 2 == 0:
            print(num)

print_even([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(some_dict):
    for keys in some_dict.keys():
        print(keys)

print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

#225
my_dict = {"10/26": [100, 130, 100, 100],
            "10/27": [10, 12, 10, 11]}

def print_value_by_key(some_dict, key):
    print(some_dict[key])

print_value_by_key(my_dict, "10/26")

#226
def print_5xn(string):
    for i in range(int(len(string) / 5) + 1):
        print(string[i*5:(i+1)*5])

print_5xn('아이엠어보이유알어걸')

#227
def print_mxn(string, m):
    for i in range(int(len(string) / m) + 1):
        print(string[i*m:(i+1)*m])

print_mxn('아이엠어보이유알어걸', 3)

#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))

calc_monthly_salary(12000000)

#229
def my_print(a, b):
    print('왼쪽:', a)
    print('오른쪽:', b)

my_print(a=100, b=200)

#230
def my_print(a, b):
    print('왼쪽:', a)
    print('오른쪽:', b)

my_print(b=100, a=200)
