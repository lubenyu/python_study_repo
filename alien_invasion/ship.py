import pygame

from settings import Settings

class Ship():
    
    def __init__(self,settings:Settings,screen:pygame.Surface):
        ''' 初始化飞船并初始化其位置'''
        self.screen = screen
        self.settings = settings 
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("./images/ship.bmp")
        # 获取船图像的外接矩形
        self.rect = self.image.get_rect()
        # 获取整个游戏框的外接矩形
        self.screen_rect = screen.get_rect()
        
        # 将每首船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)
        print(self.center)
        
        # 添加移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        ''' 根据移动标志调整位置'''
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # 更新飞船的矩形框--根据self.center
        self.rect.centerx = self.center

        
    def blitme(self):
        ''' 在指定位置绘制飞船 '''
        self.screen.blit(self.image,self.rect)
        


