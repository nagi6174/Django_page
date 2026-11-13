class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age    
    def introduce(self):
        print("私の名前は", self.name, "です。")
        print("年齢は", self.age, "です。")
    def check_sake(self):
        if self.age >= 20:
            print("お酒を飲むことができます。")
        else:
            print("お酒を飲むことはできません。")

name = input("名前を入力してください: ")
age = int(input("年齢を入力してください: "))
human = Human(name, age)
human.introduce()
human.check_sake()