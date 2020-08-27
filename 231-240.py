#231
'''
def n_plus_1(n):
    result = n + 1

n_plus_1(3)
print(result)
'''

#232
def make_url(string):
    return "www.{}.com".format(string)

print(make_url('naver'))

#233
def make_list(string):
    answer = []
    for i in range(len(string)):
        answer.append(string[i])
    return answer

print(make_list('abcd'))

#234
def pickup_even(some_list):
    answer = []
    for i in some_list:
        if i % 2 == 0:
            answer.append(i)
    return answer

print(pickup_even([3, 4, 5, 6, 7, 8]))

#235
def convert_int(string):
    return int(string.replace(',', ''))

convert_int("1,234,567")

#236
def 함수(num):
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#237
def 함수(num):
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238
def 함수1(num):
    return num + 4

def 함수2(num):
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#239
def 함수1(num):
    return num + 4

def 함수2(num):
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#240
def 함수0(num):
    return num * 2

def 함수1(num):
    return 함수0(num + 2)

def 함수2(num):
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
