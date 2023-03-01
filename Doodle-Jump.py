import pygame
import random
pygame.init()

W = 720
H = 1000
sc = pygame.display.set_mode((W,H))
sc_rect = sc.get_rect()
pygame.display.set_caption(("igra"))
WHITE = (255,255,255)

player = pygame.image.load("Files/Hero.png")
player = pygame.transform.scale(player,(25,25))
player_rect = player.get_rect()
platforms = [[W-W//2,H-25,50,10],[W-W//4,H-100,50,10],[W-W//1.5,H-200,50,10],[W-W//3,H-500,50,10],[W-W//1.2,H-300,50,10],[W-W//1.1,H-400,50,10],[W-W//3.5,H-600,50,10]]
platforma = pygame.image.load("Files/Object.png")
platforma = pygame.transform.scale(platforma,(50,10))
platforma_rect = platforma.get_rect()

FPS = 90
clock  = pygame.time.Clock()
fps_count = 0

player_rect.centerx = sc_rect.centerx
jumpcheck = False
change_y = 0

# def addPlatforms(platform):
#     global platforma_rect
#     global player_rect
#     platforma_rect.x = random.randrange(platforma_rect.x,W-50,20)
#     platforma_rect.y = random.randrange(player_rect.y,H-15,10)
#     platforms.append([platforma_rect.x,platforma_rect.y,50,10])
#     return platform

#check collision with player
def check_collisions(rect_list,jumpcheck):
    global player_rect
    global change_y
    for i in range(len(rect_list)): #45,10 - ширина и высота платформы
        if rect_list[i].colliderect([player_rect.x,player_rect.y+25,25,10]) and jumpcheck == False and  change_y > 0:
            jumpcheck = True # игрок сделавший один период, то есть вверх и вниз возвращает True т.к. прыжок завершён
    return jumpcheck
#update player_rect
def update_player(possition_y):
    global jumpcheck
    global change_y
    jump_height = 9.5
    gravity = 0.25
    if jumpcheck:
        change_y =-jump_height #скорость изменения положения прыжка изначально равно отрицательному прыжку, то есть прыжку вверх
        jumpcheck = False
    possition_y += change_y #из-за изменения скорости изменяется и само положение игрока
    change_y += gravity #в это же время действует гравитация из-за которой скорость уменьшается, вследствие позиция принимает исходное положение
    return possition_y


def update_platforms(list,player_y,change):
    global player_rect
    if player_y < 100 and change < 0: #если положение игрока по y меньше 100 и скорость изменения меньше 0, то есть он находится в положении прыжка
        for i in range(len(list)):
            list[i][1] -= change #берём элемент списка, а именно y и уменьшаем его на change(скорость изменения положения игрока в прыжке) грубо говоря опускаем платформы
    else:
        pass
    for item in range(len(list)):
        if list[item][1] > H:#если y > , то создаю платформу выше экрана
            list[item] = [random.randint(10,400),random.randint(-50,-10),50,10]
    return list

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill(WHITE)
    clock.tick(FPS)
    platforms_list = []
    for i in range(len(platforms)):
        platform = sc.blit(platforma,platforms[i])
        platforms_list.append(platform)

    #control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x-=5
    if keys[pygame.K_RIGHT]:
        player_rect.x+=5

    sc.blit(player, (player_rect))
    player_rect.y = update_player(player_rect.y)
    jumpcheck = check_collisions(platforms_list,jumpcheck)
    platforms = update_platforms(platforms,player_rect.y,change_y)
    pygame.display.update()


#commit
        