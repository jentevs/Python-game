import pygame

# intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1500, 800))

#title and icon
pygame.display.set_caption("Jumpysploinky")
icon = pygame.image.load('../Src/Img/NewPiskel1.png')
pygame.display.set_icon(icon)


#background

run = True

# loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #background color
    screen.fill((255,255,255))



    pygame.display.update()