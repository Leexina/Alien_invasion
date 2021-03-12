import sys
import pygame 
from settings import Settings
from ship import Ship

def run_game():         #初始化游戏并创建一个屏幕对象
    pygame.init()       #初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))  #创建显示窗口
    pygame.display.set_caption("Alien Invasion")  #设置窗口标题
    background_color = (230,230,230)   #设置背景颜色
    ship = Ship(screen)   #创建一艘飞船


    #开始游戏主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.background_color)    #用背景颜色填充屏幕
        ship.blitme()   #在指定位置绘制飞船
        pygame.display.flip()  #每次循环时都重绘屏幕，让最近绘制的屏幕可见  

run_game()