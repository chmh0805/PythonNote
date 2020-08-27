#121
a = input ()
if a.islower():
    print(a.upper())
else:
    print(a.lower())

#122
score = int(input("score: "))
if score >= 81:
    grade = "A"
elif score >= 61:
    grade = "B"
elif score >= 41:
    grade = "C"
elif score >= 21:
    grade = "D"
else:
    grade = "E"
print("grade is {}".format(grade))

#123
a, b = input().split(' ')
if b == "달러":
    won = a * 1167
elif b == "엔":
    won = a * 1.096
elif b == "유로":
    won = a * 1268
else:
    won = a * 171
print("{} 원".format(won))

#124
a = int(input("input number1: "))
b = int(input("input number2: "))
c = int(input("input number3: "))
print(max(a, b, c))

#125
user = input("휴대전화 번호 입력: ").split('-')
if user[0] == "011":
    mobile_carrier = 'SKT'
elif user[0] == '016':
    mobile_carrier = 'KT'
elif user[0] == '019':
    mobile_carrier = 'LGU'
else:
    mobile_carrier = '알수없음'
print("당신은 {} 사용자입니다.".format(mobile_carrier))

#126
post = input("우편번호: ")[:3]
if post in ['010', '011', '012']:
    print("강북구")
elif post in ['013', '014', '015']:
    print('도봉구')
elif post in ['016', '017', '018', '019']:
    print('노원구')

#127
주민등록번호 = input("주민등록번호: ")
l, r = 주민등록번호.split('-')
if r[:1] == '1' or r[:1] == '3':
    print("남자")
elif r[:1] == '2' or r[:1] == '4':
    print('여자')

#128
if r[1:3] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
    print('서울 입니다.')
elif r[1:3] in ['09', '10', '11', '12']:
    print('서울이 아닙니다.')

#129
num = input("주민등록번호 : ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 \
        int(num[11]) * 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')

#130
import requests
btc = requests.get('https://api.bithumb.com/public/ticker/').json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가 + 변동폭) > 최고가:
    print('상승장')
else:
    print('하락장')
