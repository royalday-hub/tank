import pygame

# 初始化界面
pygame.init()
high = 800
width = 600
# 设置窗口高度
screen = pygame.display.set_mode((high, width))
# 设置窗口标题
pygame.display.set_caption("坦克大战")
#设置游戏玩家1坦克图片
tank_my_1 = pygame.image.load("E:\work\PY_workspace\tank\material\tank.png")
#设置游戏玩家2坦克图片
tank_enemy_2 = pygame.image.load("E:\work\PY_workspace\tank\material\tank2.png")
#设置游戏玩家3坦克图片
tank_enemy_3 = pygame.image.load("E:\work\PY_workspace\tank\material\tank3.png")

#添加背景音效
pygame.mixer.music.load("E:\work\PY_workspace\tank\material\bg.wav")
#添加子弹发射音效
emission = pygame.mixer.music.load("E:\work\PY_workspace\tank\material\laser.wav")
#添加击中敌人音效
hit = pygame.mixer.music.load("E:\work\PY_workspace\tank\material\explosion.wav")



