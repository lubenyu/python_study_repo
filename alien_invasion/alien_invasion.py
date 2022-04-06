#! /usr/bin/env python3

'''
    sys模块:系统相关的参数和函数
    pygame模块: 游戏相关实现的封装
'''
import sys
import pygame
from ship import Ship
from settings import Settings

# 导入函数模块
import game_functions as gf

# 开始游戏主干逻辑函数，
def run_game():
    # 初始化游戏
    pygame.init()
    # 创建主屏窗口
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    # 设置窗口标题，即游戏名称
    pygame.display.set_caption("Alien Invasion")
    
    '''
    # 创建颜色元组(三原色,所以为3个元素的元组)
    bg_color = ()
    '''
    #  创建飞船对象，
    ship = Ship(screen)
    
    # 开始游戏的主循环
    while True:
        
        # # 每次循环都会重绘屏幕，设置背景色填充
        # screen.fill(setting.bg_color)
        
        # ship.blitme()
        
        # 一直监视键盘和鼠标事件 
        gf.check_events(ship)
        
        # 当moving_right标志为 true时，调用类方法进行移动
        ship.update()

        # 让最近绘制的屏幕可见
        gf.update_screen(setting,screen,ship)
    
    
run_game()