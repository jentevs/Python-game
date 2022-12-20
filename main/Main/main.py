import sys
import pygame
import random
from pygame import mixer
from pygame.locals import *
pygame.init()

VOLUME_MUSIC = 0.5
VOLUME_FX = 0.4
mixer.init()
def startscherm(volume_music= VOLUME_MUSIC):
    active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    mixer.music.load('../Src/SoundFx/Jump.mp3')
    mixer.music.load('../Src/Music/Main.mp3')

    mixer.music.set_volume(volume_music)
    mixer.music.play(loops=True, fade_ms=500)
    pygame.display.set_icon(pygame.image.load('../Src/Img/NewPiskel1.png'))

    #dimentions of buttons
    start_pos = pygame.Rect(580,250, 390, 113)
    settings_pos = pygame.Rect(580,360, 390, 113)
    btntut_but = pygame.Rect(580,480, 390, 113)
    quit_pos = pygame.Rect(580,570, 390, 113)
    back_poss = pygame.Rect(1020,440, 69, 76)
    btn1 = pygame.Rect(590,300, 82, 80)
    btn2 = pygame.Rect(670,300, 82, 80)
    btn3 = pygame.Rect(750,300, 82, 80)
    btn4 = pygame.Rect(830,300, 82, 80)
    btn5 = pygame.Rect(910,300, 82, 80)

    btn1f = pygame.Rect(590,450, 82, 80)
    btn2f = pygame.Rect(670,450, 82, 80)
    btn3f = pygame.Rect(750,450, 82, 80)
    btn4f = pygame.Rect(830,450, 82, 80)
    btn5f = pygame.Rect(910,450, 82, 80)


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
        screen.blit(pygame.image.load("../Src/Img/tutkey.png"),(580,465))
        screen.blit(pygame.image.load("../Src/Img/buttonQuit.png"),(580,570))

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
                    screen.blit(pygame.image.load("../Src/Img/1.png"), (590,300))
                    screen.blit(pygame.image.load("../Src/Img/2.png"), (670,300))
                    screen.blit(pygame.image.load("../Src/Img/3.png"), (750,300))
                    screen.blit(pygame.image.load("../Src/Img/4.png"), (830,300))
                    screen.blit(pygame.image.load("../Src/Img/5.png"), (910,300))
                    screen.blit(pygame.image.load("../Src/Img/volumeFx.png"), (590,400))
                    screen.blit(pygame.image.load("../Src/Img/1f.png"), (590,450))
                    screen.blit(pygame.image.load("../Src/Img/2f.png"), (670,450))
                    screen.blit(pygame.image.load("../Src/Img/3f.png"), (750,450))
                    screen.blit(pygame.image.load("../Src/Img/4f.png"), (830,450))
                    screen.blit(pygame.image.load("../Src/Img/5f.png"), (910,450))

                    screen.blit(pygame.image.load("../Src/Img/buttonBack.png"), (1020,440))

                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        #volume kiezen voor muziek
                        if btn1.collidepoint(mouse_pos):
                            VOLUME_MUSIC = 0.2
                            mixer.music.set_volume(0.2)
                        if btn2.collidepoint(mouse_pos):
                            VOLUME_MUSIC = 0.4
                            mixer.music.set_volume(0.4)
                        if btn3.collidepoint(mouse_pos):
                            VOLUME_MUSIC = 0.6
                            mixer.music.set_volume(0.6)
                        if btn4.collidepoint(mouse_pos):
                            VOLUME_MUSIC = 0.8
                            mixer.music.set_volume(0.8)
                        if btn5.collidepoint(mouse_pos):
                            VOLUME_MUSIC = 1.0
                            mixer.music.set_volume(1.0)

                        #volume van de fx
                        if btn1f.collidepoint(mouse_pos):
                            VOLUME_FX = 0.2
                        if btn2f.collidepoint(mouse_pos):
                            VOLUME_FX = 0.4
                        if btn3f.collidepoint(mouse_pos):
                            VOLUME_FX = 0.6
                        if btn4f.collidepoint(mouse_pos):
                            VOLUME_FX = 0.8
                        if btn5f.collidepoint(mouse_pos):
                            VOLUME_FX = 1.0
                        #voor terug te gaan
                        if back_poss.collidepoint(mouse_pos):
                            break

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    pygame.display.update()
            elif btntut_but.collidepoint(mouse_pos):
                while True:
                    #In de settings
                    screen.fill("black")
                    screen.blit(pygame.image.load("../Src/Img/handleidingKeys.png"), (0,0))
                    screen.blit(pygame.image.load("../Src/Img/buttonBack.png"), (1020,440))

                    if event.type == MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

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
    #######################################################################################
    #                                  VARIABLE                                           #
    #######################################################################################

    #speedzz
    speed_BG = 100
    timer = pygame.time.Clock()

    # fonts and colors
    font = pygame.font.Font('freesansbold.ttf', 20)
    BLACK = (0, 0, 0)
    BLUE_SKY = (174, 251, 255)
    COOKIE_BROWN =(201, 133, 94)
    GRAY_AUTUMN = (222,222,222)

    # score
    score = 0
    high_score = 0
    level_2_min = 2
    level_2_max = 5
    BACK_SCORE = BLUE_SKY


    # player + possition
    player_height= 70
    player_width = 90
    player = pygame.transform.scale(pygame.image.load('../Src/Img/jumpy.png'), (player_width, player_height))
    player_x = 170
    player_y = 400
    player_speed_left = 6
    player_speed_right = 6
    player_rust_left = 0
    player_rust_right = 0

    #platformen x-as, y-as, breedte platform, dikte platform
    platform_candy = pygame.image.load("../Src/Img/platform.png")
    platforms = [[600, 480, 70, 10],
                 [500, 350, 70, 10], [175, 260, 70, 10],
                 [85, 480, 70, 10], [800, 150, 70, 10]]

    # jump and movement up down
    jump = False
    y_change = 0

    # movement left right <- ->, and speed off the movement
    x_change = 0
    player_speed = 6

    # create the screen
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('jumpy jumper')

    # background
    background = pygame.image.load("../Src/Img/achtergrondWolken.png").convert()
    backgroundX = 0
    backgroundX2 = background.get_width()
    backgroundSpeed= 1.4

    #speed of background clouds
    clock = pygame.time.Clock()
    speed = 30

    #forground landscape
    voorgrond = pygame.image.load("../Src/Img/voorgrond.png")

    # game_over
    game_over = False
    game_over_screen = pygame.image.load("../Src/Img/game_Over_Screen.png")

    #Mini beans
    step = 5
    MiniBean_height= 30
    MiniBean_Width = 50
    MiniBean = pygame.transform.scale(pygame.image.load('../Src/Img/MiniBean.png'), (MiniBean_Width, MiniBean_height))
    MiniBean_x = random.randint(100, 1300 )
    MiniBean_y = random.randint(20, 300)

    #stiky top
    sticky_top = pygame.image.load('../Src/Img/sticky_top.png')

    # wolken
    wolk = pygame.image.load('../Src/Img/wolkje.png')
    wolk_x= 1100
    wolk_y = 50
    #######################################################################################
    #                                  FUNCTIONS                                          #
    #######################################################################################


    #checks if player X and Y coordinats collide with platform
    def FUNC_collisionCheck(platform_list, jump, player_x, player_y, y_change):
        for i in range(len(platform_list)):
            if platform_list[i].colliderect([player_x, player_y + 30, 50, 5]) and jump == False and y_change > 0:
                jump = True
        return jump, player_x, player_y, y_change

    #makes players jump
    def FUNC_playerMovement(player_y, jump, y_change):
        jump_height = 12
        gravity = .4
        if jump:
            y_change = -jump_height
            jump = False
        player_y += y_change
        y_change += gravity
        return player_y, jump, y_change

    # platform
    def FUNC_platforms(platforms, player_y, y_change):
        if player_y < 250 and y_change < 0:
            for i in range(len(platform_list)):
                platforms[i][1] -= y_change
            else:
                pass
            for item in range(len(platform_list)):
                # bodem scherm
                if platforms[item][1] > 500:
                    # nieuwe platformen  x-as, y-as, breedte platform, dikte platform
                    platforms[item] = [random.randint(200, 1400), random.randint(20, 60), 70, 10]

        return platforms

    # background and forground
    def FUNC_background():
        screen.blit(background, (backgroundX, 0))
        screen.blit(background, (backgroundX2, 0))
        screen.blit(voorgrond, (0, 0))

    def FUNC_MiniBeans(MiniBean_x, MiniBean_y, player_x, player_y, MiniBean_Width, MiniBean_height, player_height, player_width):
        if(player_x - MiniBean_x)<= MiniBean_Width and (MiniBean_x - player_x )<=player_width:
            if(player_y-MiniBean_y)<= MiniBean_height and (MiniBean_y -player_y)<=player_height:

                return True
        return False

    #play the musc
    #mixer.music.load('../Src/Music/lvl1.mp3')
    #mixer.music.set_volume()
    #mixer.music.play(loops=True, fade_ms=500)


    #game loop
    running = True
    while running:
        #when you want to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        platform_list = []

        # background
        FUNC_background()
        #moving background
        clock.tick(speed)
        backgroundX -= backgroundSpeed
        backgroundX2 -= backgroundSpeed
        if backgroundX < background.get_width() * -1:
            backgroundX = background.get_width()
        if backgroundX2 < background.get_width() * -1:
            backgroundX2 = background.get_width()
        timer.tick(speed_BG)

        if(FUNC_MiniBeans(MiniBean_x, MiniBean_y, player_x, player_y, MiniBean_Width, MiniBean_height, player_height, player_width )):
            MiniBean_x = random.randint(60, 1400)
            MiniBean_y = random.randint(10, 500)
            score += 1


        #blits
        screen.blit(MiniBean, (MiniBean_x, MiniBean_y))
        screen.blit(player, (player_x, player_y))
        screen.blit(sticky_top, (0,0))
        #score ---> tekst op scherm
        score_tekst = font.render('High Score: ' + str(high_score), True, BLACK, BACK_SCORE)
        screen.blit(score_tekst, (SCREEN_WIDTH - 200, 20))
        high_score_tekst = font.render('Score: ' + str(score), True, BLACK, BACK_SCORE)
        screen.blit(high_score_tekst, (SCREEN_WIDTH - 150, 50))

        # game over reset
        if game_over:
            screen.blit(game_over_screen, (0, 0))
            score_tekst = font.render('High Score: ' + str(high_score), True, BLACK, COOKIE_BROWN)
            screen.blit(score_tekst, (SCREEN_WIDTH - 780, 500))
            high_score_tekst = font.render('Score: ' + str(score), True, BLACK, COOKIE_BROWN)
            screen.blit(high_score_tekst, (SCREEN_WIDTH - 730, 530))

            # when key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game_over == True:
                    game_over = False
                    score = 0
                    player_x = 170
                    player_y = 400

                    platforms = [[600, 480, 70, 10],
                                 [500, 350, 70, 10], [175, 260, 70, 10],
                                 [85, 480, 70, 10], [800, 150, 70, 10]]
                    BACK_SCORE = BLUE_SKY
                    background = pygame.image.load("../Src/Img/achtergrondWolken.png").convert()
                    player_speed_left = 6
                    player_speed_right = 6
                    player_rust_right = 0

        else:
            for i in range(len(platforms)):
                platform = screen.blit(platform_candy, (platforms[i][0], platforms[i][1]))
                platform_list.append(platform)

            # when key is pressed
            if event.type == pygame.KEYDOWN:

                # teleport
                if event.key == pygame.K_DOWN and not game_over:
                    player_x = 1100
                    player_y = 100

                #Key left
                if event.key == pygame.K_LEFT and not game_over:
                    x_change = - player_speed_left
                    player =pygame.transform.scale(pygame.image.load('../Src/Img/left_jumpy.png'), (player_width, player_height))
                #Key right
                if event.key == pygame.K_RIGHT and not game_over:
                    x_change = player_speed_right
                    player =pygame.transform.scale(pygame.image.load('../Src/Img/right_jumpy.png'), (player_width, player_height))


            #Key not pressed anny more
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = - player_rust_left
                if event.key == pygame.K_RIGHT:
                    x_change = player_rust_right

        jump, player_x, player_y, y_change = FUNC_collisionCheck(platform_list, jump, player_x, player_y, y_change)
        player_x += x_change

        if player_y < SCREEN_WIDTH - 50:
            player_y, jump, y_change = FUNC_playerMovement(player_y, jump, y_change)
        else:
            game_over = True
            y_change = 0
            x_change = 0

        # updates platformen
        platforms = FUNC_platforms(platforms, player_y, y_change)

        # boundries left and rechts
        if player_x < -3 :
            player_x = SCREEN_WIDTH - 50
        elif player_x > SCREEN_WIDTH - 50:
            player_x = -3
        # boundries top
        if player_y <= 10:
            player_y = 10

        if score > high_score:
            high_score = score

        #verschillende niv
        if score >= level_2_min and score < level_2_max:
            # wind herfst
            #img en blits
            background = pygame.image.load("../Src/Img/achtergrondHerfst.png").convert()
            screen.blit(wolk, (wolk_x, wolk_y))

            #wind harde waaien dus achtergrond sneller
            backgroundSpeed = 2.8

            # wanneer er geen links of rechts geduwt word (word weg geduwt door de wind)
            player_rust_right = -5

            # tegen wind in en met wind mee
            player_speed_left = 20
            player_speed_right = 2

            #achtergrond kleur score en high score
            BACK_SCORE = GRAY_AUTUMN

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    startscherm()
    game()
