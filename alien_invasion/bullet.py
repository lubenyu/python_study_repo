from settings import Settings
import pygame
from pygame.sprite import Sprite
from ship import Ship

# 继承自Sprite
class Bullet(Sprite):
    ''' 一个对飞船发射的子弹进行管理的类 '''
    def __init__(self,settings:Settings,screen:pygame.Surface,ship:Ship):
        super().__init__()
        self.screen = screen
        
        # 在(0,0)处船舰一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
        
    # 子弹位置更新方法    
    def update(self):
        ''' 向上移动的子弹 '''
        # 更新表示子弹位置的数值
        self.y -= self.speed_factor
        # 更新表示子弹框的位置
        self.rect.y = self.y
        
    # 在screen中绘制子弹
    def draw_bullet(self):
        ''' 在屏幕上绘制子弹 '''
        pygame.draw.rect(self.screen,self.color,self.rect)


















    
    # def __init__(self,setings:Settings):
    #     self.speed_factor = setings.bullet_speed_factor
    #     self.width = setings.bullet_width
    #     self.height = setings.bullet_height
    #     self.color = setings.bullet_color
        
    #     pass
    
    
    
    