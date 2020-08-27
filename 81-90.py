#81
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

#82
_, _, *valid_score = scores
print(valid_score)

#83
_, *valid_score, _ = scores
print(valid_score)

#84
temp = {}
print(temp, type(temp))

#85
ice_cream = {
'Merona': 1000,
'Polapo': 1200,
'Bbangbare': 1800
}
print(ice_cream)

#86
ice_cream['Shark'] = 1200
ice_cream['World'] = 1500
print(ice_cream)

#87
print('{} Price: {}'.format('Merona', ice_cream['Merona']))

#88
ice_cream['Merona'] = 1300
print(ice_cream)

#89
del ice_cream['Merona']
print(ice_cream)

#90
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
