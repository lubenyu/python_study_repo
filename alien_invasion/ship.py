import pygame

class Ship():
    
    def __init__(self,screen:pygame.Surface):
        ''' 初始化飞船并初始化其位置'''
        self.screen = screen
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("./images/ship.bmp")
        # 获取船图像的外接矩形
        self.rect = self.image.get_rect()
        # 获取整个游戏框的外接矩形
        self.screen_rect = screen.get_rect()
        
        # 将每首船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 添加移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        ''' 根据移动标志调整位置'''
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        
    def blitme(self):
        ''' 在指定位置绘制飞船 '''
        self.screen.blit(self.image,self.rect)
        

       
# screen = pygame.display.set_mode((1200,800)) 
# l = Ship(screen)
# print(l.rect)