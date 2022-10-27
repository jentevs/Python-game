import sys
import pygame
import random
from pygame import mixer
from pygame.locals import *
pygame.init()

VOLUME_MUSIC = 0.5
VOLUME_FX = 0.4
mixer.init()

def settings_menu():
    print("b")

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

    # score
    score = 0
    high_score = 0

    # player + possition
    player_height= 70
    player_width = 90
    player = pygame.transform.scale(pygame.image.load('../Src/Img/jumpy.png'), (player_width, player_height))
    player_x = 170
    player_y = 400


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
    player_speed = 3

    # create the screen
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('jumpy jumper')

    # background
    background = pygame.image.load("../Src/Img/achtergrondWolken.png").convert()
    backgroundX = 0
    backgroundX2 = background.get_width()

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
    MiniBean_x = random.randint(60, 1400 )
    MiniBean_y = random.randint(10, 500)

    #stiky top
    sticky_top = pygame.image.load('../Src/Img/sticky_top.png')
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
    mixer.music.load('../Src/Music/lvl1.mp3')
    mixer.music.set_volume(VOLUME_MUSIC)
    mixer.music.play(loops=True, fade_ms=500)


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
        backgroundX -= 1.4
        backgroundX2 -= 1.4
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
        score_tekst = font.render('High Score: ' + str(high_score), True, BLACK, BLUE_SKY)
        screen.blit(score_tekst, (SCREEN_WIDTH - 200, 20))
        high_score_tekst = font.render('Score: ' + str(score), True, BLACK, BLUE_SKY)
        screen.blit(high_score_tekst, (SCREEN_WIDTH - 150, 50))

        # game over
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
        else:
            for i in range(len(platforms)):
                platform = screen.blit(platform_candy, (platforms[i][0], platforms[i][1]))
                platform_list.append(platform)

            # when key is pressed
            if event.type == pygame.KEYDOWN:

                #Key left
                if event.key == pygame.K_LEFT and not game_over:
                    x_change = - player_speed
                    player =pygame.transform.scale(pygame.image.load('../Src/Img/left_jumpy.png'), (player_width, player_height))
                #Key right
                if event.key == pygame.K_RIGHT and not game_over:
                    x_change = player_speed
                    player =pygame.transform.scale(pygame.image.load('../Src/Img/right_jumpy.png'), (player_width, player_height))

            #Key not pressed anny more
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = - 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

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
        if player_x < -3:
            player_x = -3
        elif player_x > SCREEN_WIDTH - 50:
            player_x = SCREEN_WIDTH - 50
        # boundries top
        if player_y <= 10:
            player_y = 10

        if score > high_score:
            high_score = score

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    startscherm()
    game()
