#111
user_input = input()
print(user_input*2)

#112
user_num = input("숫자를 입력하세요: ")
print(int(user_num) + 10)

#113
user_num = int(input())
if user_num % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
user_input = int(input("입력값: "))
if (user_input + 20) > 255:
    answer = 255
else:
    answer = user_input + 20
print("출력값: {}".format(answer))

#115
user_input = int(input("입력값: "))
if (user_input - 20) < 0:
    answer = 0
elif (user_input - 20) > 255:
    answer = 255
else:
    answer = user_input - 20
print("출력값: ".format(answer))

#116
user_input = input("현재시간:")
h, m = user_input.split(':')
if m == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

#117
fruit = ['사과', '포도', '홍시']
user_input = input("좋아하는 과일은? ")
if user_input in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#118
warn_investment_list = ['Microsoft', 'Google', 'Naver', 'Kakao', 'SAMSUNG', 'LG']
user_invest = input()
if user_invest in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {'봄': '딸기', '여름': '토마토', '가을': '사과'}
season_list = list(fruit.keys())
user_season = input('제가 좋아하는 계절은: ')
if user_season in season_list:
    print('정답입니다.')
else:
    print('오답입니다.')

#120
fruit_list = list(fruit.values())
user_fruit = input("제가 좋아하는 과일은? ")
if user_fruit in fruit_list:
    print("정답입니다.")
else:
    print("오답입니다.")
