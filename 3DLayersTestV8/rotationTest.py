import pygame,sys

win = pygame.display.set_mode((800,800))

clock = pygame.time.Clock()

img = pygame.image.load("tank3.png").convert()
angle = 0
run = True
while run:
    clock.tick(60)

    angle += 1
    
    mx, my = pygame.mouse.get_pos()

    win.fill((255,255,255))

    img_copy = pygame.transform.rotate(img,angle)
    win.blit(img_copy,(mx - img_copy.get_width()//2,my - img_copy.get_height()//2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()