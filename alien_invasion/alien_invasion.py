'''
    sys模块:系统相关的参数和函数
    pygame模块: 游戏相关实现的封装
'''
from pygame.sprite import Group
import sys
import pygame
from ship import Ship
from settings import Settings
from alien import Alien

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
    ship = Ship(setting,screen)
    
    # 创建一个用于存储子弹的编组
    bullets = Group()
    
    # 创建一个外星人对象
    alien = Alien(setting,screen)
    
    # 开始游戏的主循环
    while True:
        
        # # 每次循环都会重绘屏幕，设置背景色填充
        # screen.fill(setting.bg_color)
        
        # ship.blitme()
        
        # 一直监视键盘和鼠标事件 
        gf.check_events(setting,screen,ship,bullets)
        
        # 飞船更新
        ship.update()

        # 子弹更新
        gf.update_bullets(bullets)
        
        # 让最近绘制的屏幕可见
        gf.update_screen(setting,screen,ship,bullets,alien)
    
    
run_game()