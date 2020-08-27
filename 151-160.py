#151
list1 = [3, -20, -3, 44]
for i in list1:
    if i < 0:
        print(i)

#152
list2 = [3, 100, 23, 44]
for num in list2:
    if num % 3 == 0:
        print(num)

#153
list3 = [13, 21, 12, 14, 30, 18]
for num in list3:
    if num < 20 and num % 3 == 0:
        print(num)

#154
list4 = ['I', 'study', 'python', 'language', '!']
for word in list4:
    if len(word) >= 3:
        print(word)

#155
list5 = ['A', 'b', 'c', 'D']
for word in list5:
    if word.isupper():
        print(word)

#156
list6 = ['A', 'b', 'c', 'D']
for word in list6:
    if word.islower():
        print(word)

#157
list7 = ['dog', 'cat', 'parrot']
for word in list7:
    print(word.capitalize())

#158
list8 = ['hello.py', 'ex01.py', 'intro.hwp']
for file in list8:
    a = file.split('.')
    print(a[0])

#159
list9 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in list9:
    file_c = file.split('.')
    if file_c[1] == 'h':
        print(file)

#160
list10 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in list10:
    file_c = file.split('.')
    if file_c[1] == 'h' or file_c[1] == 'c':
        print(file)
        
