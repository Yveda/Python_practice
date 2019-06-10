#创建Pygame窗口
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏,设置，创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)
        #每次循环时都重新绘制屏幕
        screen.fill(ai_setting.bg_color)
        #创建一艘飞船
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()