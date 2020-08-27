#145
list1 = ['dog', 'cat', 'parrot']
for x in list1:
    print(x[0])

#146
list2 = [1, 2, 3]
for num in list2:
    print("3 x {}".format(num))

#147
list3 = [1, 2, 3]
for num in list3:
    print("3 x {} = {}".format(num, num*3))

#148
list4 = ['가', '나', '다', '라']
for sth in list4[1:]:
    print(sth)

#149
list5 = ['a', 'b', 'c', 'd']
for _ in list5[::2]:
    print(_)

#150
list6 = ['a', 'b', 'c', 'd']
for i in list6[::-1]:
    print(i)
