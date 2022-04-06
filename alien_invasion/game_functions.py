from operator import ne
import sys
import pygame
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from settings import Settings

def check_keydown_event(settings:Settings,screen:pygame.Surface,event,ship:Ship,bullets:Group):
    ''' 按下案件时的响应事件函数 '''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并将其加入bullets编组中
        fire_bullet(settings,screen,ship,bullets)
    
def check_keyup_event(event,ship:Ship):
    ''' 松开案件时的响应事件函数 '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings:Settings,screen:pygame.Surface,ship:Ship,bullets):
    ''' 响应按键和鼠标事件 ''' 
    for event in pygame.event.get(): # 这个事件模块的get()方法专门获取键盘鼠标事件,返回一个列表
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下按键时，移动标志置True
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(settings,screen,event,ship,bullets)
        # 松开按键时，移动标志置False
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship) 
      
            
def update_screen(settings:Settings,screen:pygame.Surface,ship:Ship,bullets:Group):
    ''' 更新屏幕上的图像，并切换到新屏幕 '''
    # 每次循环都会重新绘制屏幕
    screen.fill(settings.bg_color)
    
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    # 让重新绘制的屏幕可见
    pygame.display.flip()
    
    
def update_bullets(bullets:Group):
    ''' 更新屏幕上的子弹位置 '''
    bullets.update()

    # 删除出了图像框的子弹节约内存
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    
def fire_bullet(settings:Settings,screen:pygame.Surface,ship:Ship,bullets:Group):
    ''' 创建发射的子弹，并限制子弹数 '''
    if len(bullets) < settings.bullet_limit:
        new_bullet = Bullet(settings,screen,ship)
        bullets.add(new_bullet)