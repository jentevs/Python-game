import pygame
from pygame import mixer

mixer.init()
def startscherm():
    mixer.music.load('../Src/Music/Main.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play(loops=True, fade_ms=500)
    pygame.init()

    run = True
    while run:
        screen = pygame.display.set_mode((1500, 800))
        for event in pygame.event.get():

            #maakt het mogelijk afte sluiten
            if event.type == pygame.QUIT:
                run = False


    print("een lijn")
    #hier heb je 3 keuzes
    #1. START
    #2. SETTINGS
    #3. STOP
    #je kan bij settings de grote van de gameWindow aanpassen en de geluid
    #start scherm liedje
    mixer.music.stop()

def game():
    #er moete een txt file worden gelezen
    #de settings die er zijn worden toegepast op de game
    #scherm grote, geluid
    volume_song = 0.5
    volume_fx = 0.35

    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/Falling_death.mp3'))
    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/gettingHitt.mp3'))
    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/pickUpSoundFx.mp3'))
    mixer.Channel(1).set_volume(volume_fx)
    mixer.Channel(0).set_volume(volume_song)
    mixer.Channel(0).play(mixer.Sound('../Src/Music/lvl1.mp3'), loops=True, fade_ms=1500)

    #mixer.music.play(loops=True, fade_ms=25)


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

                #jumpy links of rechts
                if event.key == pygame.K_LEFT:
                    jumpy_changeX =-0.8
                if event.key == pygame.K_RIGHT:
                    jumpy_changeX =0.8

                # jumpy op en neer
                if event.key == pygame.K_UP:
                    jumpy_changeY = -0.6
                    mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/Jump.mp3'))
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


if __name__ == "__main__":
    startscherm()
    game()
