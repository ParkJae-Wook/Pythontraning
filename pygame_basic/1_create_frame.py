import pygame
from tkinter import messagebox

pygame.init() # 초기화 (반드시 필요함)

#화면 크기 설정
screen_w = 480 # 가로
screen_h = 640 # 세로
screen = pygame.display.set_mode((screen_w,screen_h))

#화면 타이틀
pygame.display.set_caption("JaeWook Game")

clock = pygame.time.Clock()

bgimage = pygame.image.load("C:/Python/Test/pygame_basic/background.png")
charactor = pygame.image.load("C:/Python/Test/pygame_basic/charactor.png")
c_size = charactor.get_rect().size
cw = c_size[0]
ch = c_size[1]
cxpo = (screen_w - cw)/2
cypo = screen_h - ch

enemy = pygame.image.load("C:/Python/Test/pygame_basic/enemy.png")
e_size = enemy.get_rect().size
ew = e_size[0]
eh = e_size[1]
expo = (screen_w - ew)/2
eypo = (screen_h - eh)/2

x_to = 0
y_to = 0
mspeed = 0.3

g_font = pygame.font.Font(None,40) # 폰트 정의

t_time = 10 # 시간 변수

start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True
while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_to -= mspeed
        elif event.key == pygame.K_RIGHT:
            x_to += mspeed
        elif event.key == pygame.K_UP:
            y_to -= mspeed
        elif event.key == pygame.K_DOWN:
            y_to += mspeed
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_to = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_to = 0

    cxpo += x_to * dt
    cypo += y_to * dt
    
    #화면 좌우로 나갔을 때 막기
    if cxpo < 0:
        cxpo = 0
    elif cxpo > screen_w-cw:
        cxpo = screen_w-cw
    
    #화면 위아래로 나갔을 때 막기   
    if cypo < 0:
        cypo = 0
    elif cypo > screen_h - ch:
        cypo = screen_h - ch
    
    c_rect = charactor.get_rect()
    c_rect.left = cxpo
    c_rect.top = cypo
    
    e_rect = enemy.get_rect()
    e_rect.left = expo
    e_rect.top = eypo
    
    if c_rect.colliderect(e_rect):
        messagebox.showinfo("알림","충돌했습니다. GAME OVER!")
        running = False
    
    screen.blit(bgimage,(0,0)) #배경 그리기
    screen.blit(charactor,(cxpo,cypo))
    screen.blit(enemy,(expo,eypo))
    
    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과시간은 ms 단위여서 s 단위로 바꾸기 위해 나눔
    
    timer = g_font.render(str(int(t_time - elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))
    
    # 만약 시간이 0 이하이면 게임 종료
    if t_time - elapsed_time <=0:
        messagebox.showinfo("알림","시간초과! GAME OVER!")
        running = False
    
    
    pygame.display.update() # 게임화면 계속 그려주기

pygame.quit()