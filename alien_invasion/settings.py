class Settings():
    """ 存储《外星人入侵》中所有设置的类 """
    
    def __init__(self):
        ''' 初始化游戏设置 '''
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # 控制飞船的速度
        self.ship_speed_factor = 0.5
        
        # 子弹设置
        self.bullet_speed_factor = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        # 限制子弹数
        self.bullet_limit = 3

        