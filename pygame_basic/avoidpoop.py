import pygame,os,math
from tkinter import messagebox
from random import *

pygame.init() # 초기화 (반드시 필요함)

#화면 크기 설정
screen_w = 700 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h))

#화면 타이틀
pygame.display.set_caption("Avoid Poop Game")

#프레임 코드 파일 및 이미지 파일 경로
frame_path = os.path.dirname(__file__)
image_path = os.path.join(frame_path,"images")

#시간표시를 위한 변수
clock = pygame.time.Clock()

#배경 삽입
background = pygame.image.load(os.path.join(image_path,"background3.jpg"))

#게임 캐릭터 이미지 삽입 및 초기 값 설정
charactor = pygame.image.load(os.path.join(image_path,"smile.png"))
c_size = charactor.get_rect().size
cw = c_size[0]
ch = c_size[1]
cxpo = (screen_w - cw)/2
cypo = screen_h - ch
c_radius = ch/2 #원 모양으로 충돌하기 위해 필요한 반지름 값
x_to = 0 #캐릭터가 좌우로 움직일때 쓰일 변수
mspeed = 0.1 #움직이는 속도

#피할 똥 이미지 삽입 및 초기 값 설정    
enemy = pygame.image.load(os.path.join(image_path,"poop.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_radius = enemy_height/2 #원 모양으로 충돌하기 위해 필요한 반지름 값
enemy_y_position = -100
poops=[] #여러개의 똥을 위한 리스트 생성
count = 0 #스코어 계산을 위한 변수

g_font = pygame.font.Font(None,25) # 폰트 정의

start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True
while running:
    dt = clock.tick(30) #프레임 정의
    
    #종료 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #게임 내 시간
    time =int((pygame.time.get_ticks()- start_ticks)/1000) #ms단위를  초 단위로 하기 위해 1000을 나눔
    
    #방향키 입력시 움직임 표시
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_to -= mspeed
        elif event.key == pygame.K_RIGHT:
            x_to += mspeed
    
    #키 입력 해제시 멈춤            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_to = 0

    #게임 캐릭터 움직임 정의
    cxpo += x_to * dt
    
    #적 이미지들이 초기 생성 될 당시에 사용 될 변수들
    enemy_x_position = randint(0,screen_w-enemy_width-1)
    move_speed = randint(10,45)/100
  
    #화면 좌우로 나갔을 때 막기
    if cxpo < 0:
        cxpo = 0
    elif cxpo > screen_w-cw:
        cxpo = screen_w-cw
    
    #시간이 지남에 따라 내려오는 적의 갯수 변화를 위한 분기
    if time>60 and len(poops)<30:   poops.append([enemy_x_position,enemy_y_position,move_speed])
    elif time>50 and len(poops)<26: poops.append([enemy_x_position,enemy_y_position,move_speed])
    elif time>40 and len(poops)<22: poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>30 and len(poops)<19: poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>20 and len(poops)<16: poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>10 and len(poops)<13: poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>6 and len(poops)<11:  poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>4 and len(poops)<9:   poops.append([enemy_x_position,enemy_y_position,move_speed]) 
    elif time>2 and len(poops)<5:   poops.append([enemy_x_position,enemy_y_position,move_speed])     
    elif time>1 and len(poops)<2:   poops.append([enemy_x_position,enemy_y_position,move_speed]) 
              
    #적(똥) 이동값 갱신
    poops = [[p[0],p[1]+p[2]*dt,p[2]] for p in poops]   
   
   #적(똥) 위치값 리셋과 충돌 동시에 처리
    for i in range(len(poops)):
        #충돌 설정
        c_center = (cxpo+c_radius,cypo+c_radius)
        e_center = (poops[i][0]+enemy_radius,poops[i][1]+enemy_radius)
        distance = math.sqrt((c_center[0]-e_center[0])**2+(c_center[1]-e_center[1])**2)
        if distance < c_radius+enemy_radius:
            messagebox.showinfo("알림","충돌했습니다. GAME OVER!\n점수는 {}점 입니다.".format(count))
            running = False
            break
        
        #적(똥)이 바닥에 닿으면 위치값 초기화 및 스코어 증가
        if poops[i][1]>screen_h:
            poops[i]=[randint(0,screen_w-enemy_width-1),enemy_y_position,randint(10,45)/100]
            count+=1
        
    avoided_poop = g_font.render("Score : "+str(count),True,(0,0,0)) #스코어 띄우기 위한 폰트 지정
    timer = g_font.render(str(int(time))+'"',True,(0,0,0)) #경과시간 띄우기
    
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(charactor,(cxpo,cypo)) # 캐릭터 그리기
    screen.blit(avoided_poop,(10,10)) #스코어 그리기
    screen.blit(timer,(screen_w-50,10)) #경과시간 그리기
   
    #적(똥) 그리기
    for x,y,s in poops:
        screen.blit(enemy,(x,y))
    
    pygame.display.update() # 게임화면 계속 그려주기

pygame.quit()