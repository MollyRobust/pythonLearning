import time
import pygame
from plane_sprites import *



class PlanGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("初始化")
        # 调用父类的初始化方法
        super().__init__()

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，精灵和精灵组创建
        self.__create_sprites()

        # 4.设置定时器事件 - 创建敌机 - 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 英雄发射子弹事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.时间监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新精灵组
            self.__update_sprite()

            # 5. 显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵加入到敌机精灵组
                self.enemy_group.add(enemy)

            #使用时间监听方式捕获按键
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法获取键盘按键 - 返回按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


        pass


    def __check_collide(self):

        # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 2.英雄与敌机同归于尽
        dead_enemy_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(dead_enemy_list):
            self.hero.kill()
            PlanGame.__game_over()

    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        pass

    @staticmethod
    def __game_over(self):
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象

    # 启动游戏
    PlanGame().start_game()
