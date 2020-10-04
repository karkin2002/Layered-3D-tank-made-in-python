import pygame

winWidth = 400 
winHeight = 400

win = pygame.display.set_mode((winWidth,winHeight))
clock = pygame.time.Clock()
num = ""
tankList = []
rotate = 0
rotateSpeed = 2
mx = 100
my = 100

for i in range(10):
    tankList.append(pygame.image.load('tank{}.png'.format(i)))

add = 0
pygame.mouse.set_visible(False)
run = True
while run:
    pList = []
    clock.tick(60)
    mx, my = pygame.mouse.get_pos()
    win.fill((34,139,34))

    mousePos = pygame.mouse.get_pos()
    mousePress = pygame.mouse.get_pressed()
    
    heightElevation = 0
    for eachImage in tankList:
        img_copy = pygame.transform.rotate(eachImage,rotate)
        win.blit(img_copy,((mx - img_copy.get_width()//2)-heightElevation,(my - img_copy.get_height()//2)-heightElevation))
        heightElevation += 1
    

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rotate += rotateSpeed
    if keys[pygame.K_RIGHT]:
        rotate -= rotateSpeed
    
    if rotate > 360:
        rotate = 0
    elif rotate < 0:
        rotate = 360

    print(rotate)
    pygame.display.update()