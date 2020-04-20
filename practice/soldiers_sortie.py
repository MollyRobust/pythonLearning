#!/usr/bin/env python
# encoding: utf-8
class Gun:

    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        #首先判断是否有子弹
        if self.bullet_count <= 0:
            print("没有子弹了。。。")
            return
        print("piu~")
        self.bullet_count -= 1

class Soldier:

    def __init__(self,name,time,lover):
        self.name = name
        self.time = time
        self.lover = lover
        #在不知是否有资格拿枪的情况下先设置为None
        self.gun = None

    def __str__(self):
        return "我是不怕牺牲的战士%s"%self.name

    # 士兵开枪
    def fire(self,gun):
        if self.time > 1:
            self.gun = gun

        if self.gun is None:
            print("对不起，你还没有枪，开不了火。。。")
        else:
            print("我有一把%s,我要保卫%s!至死不渝!"%(gun.model,self.lover))
            gun.shoot()

#创建枪对象
gun = Gun("JS7.62mm狙击枪")
gun.add_bullet(10)

#创建士兵对象
soldier = Soldier("赵鸿飞",3,"王斯然")
soldier.fire(gun)