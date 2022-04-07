import random 
import pygame
from pygame.sprite import Sprite
from settings import Settings

# 创建外星人类模板
class Alien(Sprite):
    ''' 表示单个外星人的类 '''
    # 初始化外星人并设置起始位置
    def __init__(self,settings:Settings,screen:pygame.Surface):
        super().__init__()
        
        self.screen = screen
        self.settings = settings
        
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        
        # 外星人出现位置
        self.rect.y = 0
        self.rect.x = random.randint(0,550)
        
    def biltme(self):
        ''' 指定位置绘制外星人 '''
        self.screen.blit(self.image,self.rect)
    