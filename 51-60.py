# -*- conding: utf-8 -*-

#51
movie_rank = ['doctor', 'split', 'lucky']
print(movie_rank)

#52
movie_rank.append('batman')
print(movie_rank)

#53
movie_rank.insert(1, "superman")
print(movie_rank)

#54
'''
movie_rank.remove('lucky')
print(movie_rank)
또는
'''
del movie_rank[3]
print(movie_rank)

#55
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}")
print(f"min: {min(nums)}")

#58
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59
cook = ["피자", "김밥", "만두", '양념치킨', '족발', '피자', '김치만두', '쫄면', "쏘세지", '라면', '팥빙수', '김치전']
print(len(cook))

#60
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))
