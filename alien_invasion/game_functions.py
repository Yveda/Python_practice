#储存大量让游戏运行的函数
import sys
import pygame
def check_events(ship):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #检查下是否按右箭头
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            # #向右移动飞船
            # ship.rect.centerx += 1
        #松开右箭头的时候设置为false
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_setting, screen, ship):
    #更新屏幕上的图像，并切换到新屏幕
    #每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #让最新绘制的屏幕可见
    pygame.display.flip()