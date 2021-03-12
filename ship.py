import pygame
class Ship():
    #初始化飞船并设置其初始位置
    def __init__(self,screen):
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')   #加载飞船图像
        self.rect = self.image.get_rect()  #获取图像矩形属性
        self.screen_rect = screen.get_rect()   #获取窗口矩形属性

        #将每搜飞船放在在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx   #飞船中心的x坐标与屏幕x轴中心对齐
        self.rect.bottom = self.screen_rect.bottom   #飞创下边缘的y轴坐标和屏幕下边缘对齐

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
