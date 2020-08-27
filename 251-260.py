#252
class Human:
    pass

print(type(Human))

#253
areum = Human()

#254
class Human:
    def __init__(self):
        print('응애응애')

areum = Human()

#255
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return "이름은 {}이고 {}살이며, 성별은 {}입니다.".format(self.name, self.age, self.gender)

areum = Human("아름", 25, "여자")
print(areum.name)
print(areum)

#256
print("이름: {}, 나이: {}, 성별: {}".format(areum.name, areum.age, areum.gender))

#257
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('나의 죽음을 알리지 말라.')

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")
areum.who()

#258
areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")
areum.who()

#259
del areum

#260
class OMG:
    def print():
        print("Oh my god")

myStock = OMG()
myStock.print()
