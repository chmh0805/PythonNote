#71
my_variable = ()
print(my_variable, type(my_variable))

#72
movie_rank = ('Doctor Strange', 'Split', 'Lucky')
print(movie_rank)

#73
a = (1)
print(a, type(a))
a = (1,)
print(a, type(a))

#74
'''
t = (1, 2, 3)
t[0] = 'a'
'''

#75
t = 1, 2, 3, 4
print(type(t))

#76
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#77
interest = ('Samsung', 'LG', 'SK Hynix')
interest = list(interest)
print(interest, type(interest))

#78
interest = tuple(interest)
print(interest, type(interest))

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print(a)

#80
data = tuple(range(2, 100, 2))
print(data)
