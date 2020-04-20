#!/usr/bin/env python
# encoding: utf-8

class Dog(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "这只狗子名叫%s"%self.name

    def game(self):
        print("趴在地上玩耍。。")

class FlyDog(Dog):
    def game(self):
        print("%s飞到天上玩耍。。"%self.name)

class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        #和狗一起玩
        print("%s和%s一起玩耍"%(self.name,dog.name))
        #让狗自己玩
        dog.game()

#创建狗对象
tony = Dog("tony")

flytony = FlyDog("flyBaby")
print(flytony)

#创建人对象
mimi = Person("Mimi")
mimi.game_with_dog(flytony)
