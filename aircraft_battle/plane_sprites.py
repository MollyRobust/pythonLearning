import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed = 1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕上垂直移动
        self.rect.y += self.speed

class BackGround(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt = False):
        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2. 判断是否移除屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)

        # 3.指定敌机的初始随机位置
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0
        pass

    def update(self):

        # 1.调用父类方法，保持垂直飞行
        super().update()

        # 2.判断是否废除屏幕， 如果废除，从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机挂了%s"%self.rect)
        pass

class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法
        super().__init__("./images/me1.png", speed=0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()


    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        # 1.创建子弹精灵
        for i in (0,1,2):
            bullet = Bullet()
            # 2.设置精灵位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx

            # 3.把精灵添加到精灵组
            self.bullets.add(bullet)
            print("发射子弹")

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png",speed=-2)
        pass

    def update(self):

        # 调用父类方法 子弹严垂直方向飞行
        super().update()

        # 判断子弹是否废除屏幕
        if self.rect.bottom < 0:
            self.kill()
        pass

    def __del__(self):
        print("子弹被销毁")