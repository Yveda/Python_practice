class Settings():
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #飞船设置
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #外星人设置  
        #撞到屏幕屏幕边缘时候向下的移动速度
        self.fleet_drop_speed = 10
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的位置"""
        #飞船的设置，移动飞船的时候是1.5像素而不是1像素, factor翻译成系数
        self.ship_speed_factor = 1.5
        #子弹设置(宽3像素，高15像素，灰色，子弹速度比飞船速度低)
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #提高外星人点数
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)