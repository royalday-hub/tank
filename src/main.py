import pygame

# ��ʼ������
pygame.init()
high = 800
width = 600
# ���ô��ڸ߶�
screen = pygame.display.set_mode((high, width))
# ���ô��ڱ���
pygame.display.set_caption("̹�˴�ս")
#������Ϸ���1̹��ͼƬ
tank_my_1 = pygame.image.load("E:\work\PY_workspace\tank\material\tank.png")
#������Ϸ���2̹��ͼƬ
tank_enemy_2 = pygame.image.load("E:\work\PY_workspace\tank\material\tank2.png")
#������Ϸ���3̹��ͼƬ
tank_enemy_3 = pygame.image.load("E:\work\PY_workspace\tank\material\tank3.png")

#��ӱ�����Ч
pygame.mixer.music.load("E:\work\PY_workspace\tank\material\bg.wav")
#����ӵ�������Ч
emission = pygame.mixer.music.load("E:\work\PY_workspace\tank\material\laser.wav")
#��ӻ��е�����Ч
hit = pygame.mixer.music.load("E:\work\PY_workspace\tank\material\explosion.wav")



