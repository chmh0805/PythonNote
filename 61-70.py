#61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65
interest = ['samsung', 'LG', 'Naver']
print(interest[::2])

#66
interest = ['Samsung', 'LG', 'Naver', 'SK Hynix', 'MiraeAsset']
print(" ".join(interest))

#67
print("/".join(interest))

#68
print("\n".join(interest))

#69
string = 'Samsung/LG/Naver'
interest = string.split('/')
print(interest)

#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

#70-1
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
