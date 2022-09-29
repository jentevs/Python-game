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

    # background

    run = True

    # loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # background color
        screen.fill((255, 255, 255))

        pygame.display.update()


if __name__ == "__main__" :
    startscherm()
    game()



