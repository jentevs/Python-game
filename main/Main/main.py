import pygame
def startscherm():
    print("een lijn")
    #hier heb je 3 keuzes
    #1. START
    #2. SETTINGS
    #3. STOP
    #je kan bij settings de grote van de gameWindow aanpassen en de geluid
    #start scherm liedje

def game():
    #er moete een txt file worden gelezen
    #de settings die er zijn worden toegepast op de game
    #scherm grote, geluid
    #Eerste lvl Liedje

    # initialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((1500, 800))


    # title and icon
    pygame.display.set_caption("Jumpysploinky")
    icon = pygame.image.load('../Src/Img/NewPiskel1.png')
    pygame.display.set_icon(icon)

    #jumpy
    jumpy = pygame.image.load('../Src/Img/jumpy.png')
    jumpyX = 300
    jumpyY = 300
    jumpy_changeX = 0
    jumpy_changeY = 0
    # background
    background = pygame.image.load("../Src/Img/achtergrond.png")

    def func_jumpy(x, y):
        screen.blit(jumpy, (x, y))

    def func_background():
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))



    run = True

    # loop
    while run:
        func_background()

        for event in pygame.event.get():

            #maakt het mogelijk afte sluiten
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                #jumpy op de X as
                if event.key == pygame.K_LEFT:
                    jumpy_changeX =-0.8
                if event.key == pygame.K_RIGHT:
                    jumpy_changeX =0.8

                # jumpy op de Y as
                if event.key == pygame.K_UP:
                    jumpy_changeY = -0.6
                if event.key == pygame.K_DOWN:
                    jumpy_changeY = 0.6

                #jumpy springt

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                jumpy_changeX =0
                jumpy_changeY =0

    jumpyX += jumpy_changeX
    jumpyY += jumpy_changeY
    func_jumpy(jumpyX, jumpyY)

    pygame.display.update()


if __name__ == "__main__" :
    startscherm()
    game()