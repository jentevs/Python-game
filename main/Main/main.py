import sys
import pygame
from pygame import mixer
from pygame.locals import *
pygame.init()

VOLUME_MUSIC = 0.5
VOLUME_FX = 0.4
mixer.init()

def settings_menu():
    print("balls")

def startscherm():
    active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    mixer.music.load('../Src/Music/Main.mp3')
    mixer.music.set_volume(VOLUME_MUSIC)
    mixer.music.play(loops=True, fade_ms=500)
    pygame.display.set_icon(pygame.image.load('../Src/Img/NewPiskel1.png'))

    #dim of buttons
    start_pos = pygame.Rect(580,250, 390, 113)
    settings_pos = pygame.Rect(580,360, 390, 113)
    quit_pos = pygame.Rect(580,480, 390, 113)
    back_poss = pygame.Rect(1020,440, 69, 76)

    #dim of input txt
    sound_fx_txt = pygame.Rect(590,400, 389, 131)
    music_vol_txt = pygame.Rect(590,250, 389,131)

    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("Main Menu")


    run = True
    while run:

        for event in pygame.event.get():

            #maakt het mogelijk afte sluiten
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(pygame.image.load("../Src/Img/startscherm.png"), (0, 0))
        screen.blit(pygame.image.load("../Src/Img/buttonPlay.png"),(580,250))
        screen.blit(pygame.image.load("../Src/Img/buttonSetting.png"),(580,360))
        screen.blit(pygame.image.load("../Src/Img/buttonQuit.png"),(580,480))

        #buttons
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if start_pos.collidepoint(mouse_pos):
                run = False
            elif settings_pos.collidepoint(mouse_pos):

                while True:
                    #In de settings
                    screen.fill("black")
                    screen.blit(pygame.image.load("../Src/Img/startscherm.png"), (0, 0))
                    screen.blit(pygame.image.load("../Src/Img/volumeMusic.png"), (590,250))
                    screen.blit(pygame.image.load("../Src/Img/volumeFx.png"), (590,400))
                    screen.blit(pygame.image.load("../Src/Img/buttonBack.png"), (1020,440))

                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        #voor de txtbalk
                        if music_vol_txt.collidepoint(event.pos):
                            # Toggle the active variable.
                            active = not active
                        else:
                            active = False
                            # Change the current color of the input box.
                        color = color_active if active else color_inactive
                        if event.type == pygame.KEYDOWN:
                            if active:
                                if event.key == pygame.K_RETURN:
                                    print(text)
                                    text = ''
                                elif event.key == pygame.K_BACKSPACE:
                                    text = text[:-1]
                                else:
                                    text += event.unicode

                        #voor terug te gaan
                        if back_poss.collidepoint(mouse_pos):
                            break
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    pygame.display.update()
            elif quit_pos.collidepoint(mouse_pos):
                sys.exit()
        pygame.display.update()
    mixer.music.stop()

def game():
    # initialize the pygame
    pygame.init()
    #er moete een txt file worden gelezen
    #de settings die er zijn worden toegepast op de game
    volume_song = 0.5
    volume_fx = 0.35
    print("testeted;jhvfbjnkdd")
    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/Falling_death.mp3'))
    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/gettingHitt.mp3'))
    #mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/pickUpSoundFx.mp3'))
    mixer.Channel(1).set_volume(volume_fx)
    mixer.Channel(0).set_volume(volume_song)
    mixer.Channel(0).play(mixer.Sound('../Src/Music/lvl1.mp3'), loops=True, fade_ms=1500)

    #mixer.music.play(loops=True, fade_ms=25)




    #create the screen
    screen = pygame.display.set_mode((1500, 800))


    #title and icon
    pygame.display.set_caption("Jumpysploinky")
    icon = pygame.image.load('../Src/Img/NewPiskel1.png')
    pygame.display.set_icon(icon)

    #jumpy
    jumpy = pygame.image.load('../Src/Img/jumpy.png')
    Jumping = False
    x = 160
    y = 680
    width = 83
    height = 56
    snelheid = 5
    Count = 10




    # background
    background = pygame.image.load("../Src/Img/achtergrondWolken.png").convert()
    backgroundX = 0
    backgroundX2 = background.get_width()
    clock = pygame.time.Clock()
    voorgrond = pygame.image.load("../Src/Img/voorgrond.png")


    def func_jumpy(x, y):
        screen.blit(jumpy, (x, y))

    def func_background():
        screen.blit(background, (backgroundX, 0))
        screen.blit(background, (backgroundX2, 0))
        screen.blit(voorgrond, (0, 0))


    run = True
    speed = 30
    # loop
    while run:
        func_background()
        clock.tick(speed)
        backgroundX -= 1.4
        backgroundX2 -= 1.4
        if backgroundX < background.get_width() * -1:
            backgroundX = background.get_width()
        if backgroundX2 < background.get_width() * -1:
            backgroundX2 = background.get_width()



        pygame.time.delay(50)


        for event in pygame.event.get():

            #maakt het mogelijk afte sluiten
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > snelheid:
            x -= snelheid
        if keys[pygame.K_RIGHT] and x < 1500 - width - snelheid:
            x += snelheid
        #springen
        if not(Jumping):
            if keys[pygame.K_SPACE]:
                mixer.Channel(1).play(mixer.Sound('../Src/SoundFx/Jump.mp3'))
                Jumping = True

        else:
            if Count >= -10:
                negaftief = 1
                if Count < 0:
                    negaftief = -1

                y -= (Count ** 2) * 0.5 * negaftief
                Count -= 1
            else:
                Jumping = False
                Count = 10




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jumpy_changeX =0






        func_jumpy(x, y)
        pygame.display.update()


if __name__ == "__main__":
    startscherm()
    game()
