#!/usr/bin/env python
# encoding: utf-8

class Furniture:

    def __init__(self,name,size):
        self.name = name
        self.size = size

    def __str__(self):
        return "[%s]占地 %.2f 平米"%(self.name,self.size)

class House:

    def __init__(self,house_type,size):
        self.house_type = house_type
        self.size = size

        #初始化剩余面积
        self.free_size = size

        #家具名称列表 初始为空
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f"
                %(self.house_type,self.size,self.free_size))

    def add_items(self,item):
        print("要添加%s"%item)
        self.free_size -= item.size

# 创建家具
bed = Furniture("双人床",20)
desk = Furniture("桌子",6.5)
bookshelf = Furniture("书架",2)
print(bed)
print(desk)
print(bookshelf)

# 创建房子对象
my_home = House("两室一厅",100)
#给房子中添加家具
my_home.add_items(bed)
my_home.add_items(desk)
my_home.add_items(bookshelf)
print(my_home)