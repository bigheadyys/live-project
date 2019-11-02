import pygame
import sys
import traceback
from pygame.locals import *

# 初始化Pygame
pygame.init()

# 创建制定大小的窗口
size = width,height = 600,600
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("福州大学测评软件")

clock = pygame.time.Clock()#设置时针

#首页
home_jpg = pygame.image.load("素材/首页.png").convert()

#最佳美食聚集地背景
best_food_jpg = pygame.image.load("素材/最佳美食聚集地.png").convert()

#最佳美食聚集地按钮
best_food_button = pygame.image.load("素材/美食.png").convert_alpha()
best_food_button_rect = best_food_button.get_rect()
best_food_button_rect.left,best_food_button_rect.top = 378,360

#最佳服饰按钮
best_cl_button = pygame.image.load("素材/服饰.png").convert_alpha()
best_cl_button_rect = best_cl_button.get_rect()
best_cl_button_rect.left,best_cl_button_rect.top = 80,360

#最受欢迎商圈背景
most_popular_mall_jpg = pygame.image.load("素材/最受欢迎商圈.png").convert()

#最受欢迎商圈按钮
best_popular_mall_button = pygame.image.load("素材/商圈.png").convert_alpha()
best_popular_mall_button_rect = best_popular_mall_button.get_rect()
best_popular_mall_button_rect.left,best_popular_mall_button_rect.top = 80,90

#餐厅按钮
best_shop_button = pygame.image.load("素材/餐厅.png").convert_alpha()
best_shop_button_rect = best_shop_button.get_rect()
best_shop_button_rect.left,best_popular_mall_button_rect.top = 378,90

#返回按钮
re_button = pygame.image.load("素材/返回按钮.png").convert_alpha()
re_button_rect = re_button.get_rect()
re_button_rect.left,re_button_rect.top = 0,0

def main():
    home_flag = True#主页
    best_food_flag = False#最佳美食聚集地
    most_popular_mall_flag = False#最受欢迎商圈
    best_cl_flag = False#最佳服饰
    best_shop_flag = False#餐厅
    
    while True:
        #事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if best_food_button_rect.collidepoint(event.pos) and home_flag:
                        home_flag = False
                        best_food_flag = True
                    
                    #返回按钮
                    if re_button_rect.collidepoint(event.pos) and not home_flag:
                        home_flag = True
                        best_food_flag = False
                        most_popular_mall_flag = False
                        best_cl_flag = False
                        best_shop_flag = False

        #绘制    
        if best_food_flag:
            screen.blit(best_food_jpg,(0,0))
            
        if most_popular_mall_flag:
            screen.blit(most_popular_mall_jpg,(0,0))
        #主页
        if home_flag:
            screen.blit(home_jpg,(0,0))
            screen.blit(best_food_button,(378,360))
            screen.blit(best_cl_button,(80,360))
            screen.blit(best_popular_mall_button,(80,90))
            screen.blit(best_shop_button,(378,90))

        if not home_flag:
            screen.blit(re_button,(0,0))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        
        traceback.print_exc()
        pygame.quit()
        input()
