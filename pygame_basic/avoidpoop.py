import pygame
from tkinter import messagebox
from random import *

class Enemy:
    def __init__(self):
        self.enemy = pygame.image.load("C:/Python/Test/pygame_basic/poop.png")
        self.enemy_size = self.enemy.get_rect().size
        self.enemy_width = self.enemy_size[0]
        self.enemy_height = self.enemy_size[1]
        self.enemy_x_position = randint(0,screen_w-self.enemy_width-1)
        self.enemy_y_position = -100
        self.move_speed = 0
        self.enemy_rect = self.enemy.get_rect()
    def set_x_position(self):
        self.enemy_x_position = randint(0,screen_w-self.enemy_width-1)
    def set_move_speed(self):
        self.move_speed = randint(20,45)/100



pygame.init() # 초기화 (반드시 필요함)

#화면 크기 설정
screen_w = 700 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h))

#화면 타이틀
pygame.display.set_caption("Avoid Poop Game")
p0=Enemy()
p1=Enemy()
p2=Enemy()
p3=Enemy()
p4=Enemy()
p5=Enemy()
p6=Enemy()
p7=Enemy()
p8=Enemy()
p9=Enemy()
clock = pygame.time.Clock()
background = pygame.image.load("C:/Python/Test/pygame_basic/background3.jpg")
charactor = pygame.image.load("C:/Python/Test/pygame_basic/smile.png")
c_size = charactor.get_rect().size
cw = c_size[0]
ch = c_size[1]
cxpo = (screen_w - cw)/2
cypo = screen_h - ch





x_to = 0
y_to = 0
mspeed = 0.1
count = 0
g_font = pygame.font.Font(None,20) # 폰트 정의



start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time = (pygame.time.get_ticks()- start_ticks)/500
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_to -= mspeed
        elif event.key == pygame.K_RIGHT:
            x_to += mspeed
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_to = 0

    cxpo += x_to * dt
    
    
    #화면 좌우로 나갔을 때 막기
    if cxpo < 0:
        cxpo = 0
    elif cxpo > screen_w-cw:
        cxpo = screen_w-cw
    
    c_rect = charactor.get_rect()
    c_rect.left = cxpo 
    c_rect.top = cypo
    
  
    if time>0.5:
        if p0.enemy_y_position<=0:
            #p0.set_x_position()
            p0.set_move_speed()
        elif p0.enemy_y_position>screen_h-p0.enemy_height:
            p0.enemy_y_position=0
            p0.set_x_position()
            p0.set_move_speed()
            count+=1       
    if time>1: 
        if p1.enemy_y_position<=0:
            #p1.set_x_position()
            p1.set_move_speed()
        elif p1.enemy_y_position>screen_h-p1.enemy_height:
            p1.enemy_y_position=0
            p1.set_x_position()
            p1.set_move_speed()
            count+=1
    if time>3: 
        if p2.enemy_y_position<=0:
            #p2.set_x_position()
            p2.set_move_speed()
        elif p2.enemy_y_position>screen_h-p2.enemy_height:
            p2.enemy_y_position=0
            p2.set_x_position()
            p2.set_move_speed()
            count+=1
    if time>4: 
        if p3.enemy_y_position<=0:
            #p3.set_x_position()
            p3.set_move_speed()
        elif p3.enemy_y_position>screen_h-p3.enemy_height:
            p3.enemy_y_position=0
            p3.set_x_position()
            p3.set_move_speed()
            count+=1
    if time>6: 
        if p4.enemy_y_position<=0:
            #p4.set_x_position()
            p4.set_move_speed()
        elif p4.enemy_y_position>screen_h-p4.enemy_height:
            p4.enemy_y_position=0
            p4.set_x_position()
            p4.set_move_speed()
            count+=1
    if time>8: 
        if p5.enemy_y_position<=0:
            #p5.set_x_position()
            p5.set_move_speed()
        elif p5.enemy_y_position>screen_h-p5.enemy_height:
            p5.enemy_y_position=0
            p5.set_x_position()
            p5.set_move_speed()
            count+=1
    if time>10: 
        if p6.enemy_y_position<=0:
            #p6.set_x_position()
            p6.set_move_speed()
        elif p6.enemy_y_position>screen_h-p6.enemy_height:
            p6.enemy_y_position=0
            p6.set_x_position()
            p6.set_move_speed()
            count+=1
    if time>15: 
        if p7.enemy_y_position<=0:
            #p7.set_x_position()
            p7.set_move_speed()
        elif p7.enemy_y_position>screen_h-p7.enemy_height:
            p7.enemy_y_position=0
            p7.set_x_position()
            p7.set_move_speed()
            count+=1
    if time>20: 
        if p8.enemy_y_position<=0:
            #p8.set_x_position()
            p8.set_move_speed()
        elif p8.enemy_y_position>screen_h-p8.enemy_height:
            p8.enemy_y_position=0
            p8.set_x_position()
            p8.set_move_speed()
            count+=1
    if time>25: 
        if p9.enemy_y_position<=0:
            #p9.set_x_position()
            p9.set_move_speed()
        elif p9.enemy_y_position>screen_h-p9.enemy_height:
            p9.enemy_y_position=0
            p9.set_x_position()
            p9.set_move_speed()
            count+=1        
        
    p0.enemy_y_position+=p0.move_speed*dt
    p0.enemy_rect.left = p0.enemy_x_position 
    p0.enemy_rect.top = p0.enemy_y_position 
    p1.enemy_y_position+=p1.move_speed*dt
    p1.enemy_rect.left = p1.enemy_x_position 
    p1.enemy_rect.top = p1.enemy_y_position 
    p2.enemy_y_position+=p2.move_speed*dt
    p2.enemy_rect.left = p2.enemy_x_position 
    p2.enemy_rect.top = p2.enemy_y_position 
    p3.enemy_y_position+=p3.move_speed*dt
    p3.enemy_rect.left = p3.enemy_x_position 
    p3.enemy_rect.top = p3.enemy_y_position 
    p4.enemy_y_position+=p4.move_speed*dt
    p4.enemy_rect.left = p4.enemy_x_position 
    p4.enemy_rect.top = p4.enemy_y_position 
    p5.enemy_y_position+=p5.move_speed*dt
    p5.enemy_rect.left = p5.enemy_x_position 
    p5.enemy_rect.top = p5.enemy_y_position 
    p6.enemy_y_position+=p6.move_speed*dt
    p6.enemy_rect.left = p6.enemy_x_position 
    p6.enemy_rect.top = p6.enemy_y_position 
    p7.enemy_y_position+=p7.move_speed*dt
    p7.enemy_rect.left = p7.enemy_x_position 
    p7.enemy_rect.top = p7.enemy_y_position 
    p8.enemy_y_position+=p8.move_speed*dt
    p8.enemy_rect.left = p8.enemy_x_position 
    p8.enemy_rect.top = p8.enemy_y_position 
    p9.enemy_y_position+=p9.move_speed*dt
    p9.enemy_rect.left = p9.enemy_x_position 
    p9.enemy_rect.top = p9.enemy_y_position 
    
    if c_rect.colliderect(p0.enemy_rect) or c_rect.colliderect(p1.enemy_rect) or c_rect.colliderect(p2.enemy_rect)\
        or c_rect.colliderect(p3.enemy_rect) or c_rect.colliderect(p4.enemy_rect) or c_rect.colliderect(p5.enemy_rect)\
        or c_rect.colliderect(p6.enemy_rect) or c_rect.colliderect(p7.enemy_rect) or c_rect.colliderect(p8.enemy_rect):
        messagebox.showinfo("알림","충돌했습니다. GAME OVER!\n점수는 {}점 입니다.".format(count))
        running = False
    
    avoided_poop = g_font.render("Score : "+str(count),True,(0,0,0))
    
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(charactor,(cxpo,cypo)) # 캐릭터 위치 잡기
    screen.blit(avoided_poop,(10,10)) 
    
    screen.blit(p0.enemy,(p0.enemy_x_position,p0.enemy_y_position))
    screen.blit(p1.enemy,(p1.enemy_x_position,p1.enemy_y_position)) 
    screen.blit(p2.enemy,(p2.enemy_x_position,p2.enemy_y_position))
    screen.blit(p3.enemy,(p3.enemy_x_position,p3.enemy_y_position))
    screen.blit(p4.enemy,(p4.enemy_x_position,p4.enemy_y_position))
    screen.blit(p5.enemy,(p5.enemy_x_position,p5.enemy_y_position))
    screen.blit(p6.enemy,(p6.enemy_x_position,p6.enemy_y_position))
    screen.blit(p7.enemy,(p7.enemy_x_position,p7.enemy_y_position))
    screen.blit(p8.enemy,(p8.enemy_x_position,p8.enemy_y_position))
    screen.blit(p9.enemy,(p9.enemy_x_position,p9.enemy_y_position))

    
  
    
    pygame.display.update() # 게임화면 계속 그려주기

pygame.quit()