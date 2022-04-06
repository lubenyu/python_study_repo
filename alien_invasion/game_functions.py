import sys
import pygame
from ship import Ship

from settings import Settings

def check_events(ship:Ship):
    ''' 响应按键和鼠标事件 ''' 
    for event in pygame.event.get(): # 这个事件模块的get()方法专门获取键盘鼠标事件,返回一个列表
        if event.type == pygame.QUIT:
            sys.exit()
        # 向右事件
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            
        # # 向左事件
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         ship.moving_left = True
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         ship.moving_left = False
             
            
def update_screen(settings:Settings,screen:pygame.Surface,ship:Ship):
    ''' 更新屏幕上的图像，并切换到新屏幕 '''
    # 每次循环都会重新绘制屏幕
    screen.fill(settings.bg_color)
    ship.blitme()
    
    # 让重新绘制的屏幕可见
    pygame.display.flip()