#161
for _ in range(100):
    print(_)

#162
for year in range(2002, 2051, 4):
    print(year)

#163
for i in range(3, 31, 3):
    print(i)

#164
for i in range(99, -1, -1):
    print(i)

for i in range(100):
    print(99 - i)

#165
for i in range(10):
    print(i / 10)

#166
for i in range(1, 10):
    print("3x{} = {}".format(i, 3*i))

#167
for i in range(1, 10):
    if i % 2 != 0:
        print("3x{} = {}".format(i, i*3))

#168
sum = 0
for i in range(1, 11):
    sum += i
print("sum : {}".format(sum))

#169
sum = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum += i
print("sum : {}".format(sum))

#170
multiply = 1
for i in range(1, 11):
    multiply *= i
print(multiply)
