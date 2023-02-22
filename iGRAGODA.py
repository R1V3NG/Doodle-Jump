import pygame
pygame.init()
W = 1280
H = 720
sc = pygame.display.set_mode((W, H)) #get_rect тоже серфейс
pygame.display.set_caption("Класс Rect")
sc_rect = sc.get_rect()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
FPS = 90        # число кадров в секунду
clock = pygame.time.Clock()

hero = pygame.image.load("Files/Hero.png")
hero = pygame.transform.scale(hero,(50,50))
hero_rect = hero.get_rect()


ground = pygame.image.load("Files/Ground.png")
ground = pygame.transform.scale(ground,(1280,100))
ground_rect = ground.get_rect()
ground_rect.bottom = sc_rect.bottom

hero_rect.bottom = ground_rect.top

item = pygame.image.load("Files/Object.png")
item = pygame.transform.scale(item,(100,100))
item_rect = item.get_rect()
item_rect.bottom = ground_rect.top
item_rect.x = ground_rect.bottomright[0]//2

jump = 25
move = jump+1
fps_count  = 0
pygame.display.update()
screen = sc.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: 
        if hero_rect.bottomright != item_rect.bottomleft:
            hero_rect.x +=5
        else:
            hero_rect.x+=5
            item_rect.x+=5
    if keys[pygame.K_LEFT]: 
        if hero_rect.bottomleft != item_rect.bottomright:
            hero_rect.x -=5
        else:
            hero_rect.x-=5
            item_rect.x-=5

    if keys[pygame.K_SPACE]:
        if hero_rect.bottom == ground_rect.top:
            move = -jump
        #если координаты совпадают то прыгаем и фикс бага с прыжком выше граунда
        if hero_rect.bottom == item_rect.top and hero_rect.topleft < item_rect.topright and hero_rect.topright > item_rect.topleft:
            move = -jump
    if move <= jump: 
        if hero_rect.bottom + move < ground_rect.top:
            hero_rect.bottom+=move
            if move < jump:
                move+=1
        else:
            hero_rect.bottom = ground_rect.top
            move = jump+1
    # фикс бага с прыжком над землей
    if hero_rect.colliderect(item_rect):
        if hero_rect.bottom >= item_rect.top:
            hero_rect.bottom = item_rect.top

                
    #print(hero_rect.bottom,item_rect.top)
        

    clock.tick(FPS)
    sc.fill(WHITE)
    sc.blit(item,item_rect)
    sc.blit(ground,ground_rect)
    sc.blit(hero,hero_rect)
    pygame.display.update()