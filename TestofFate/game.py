import time
from pygame import mixer
import pygame
import sys
import random
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(" TEST OF FATE ")

BG = pygame.image.load("assets/rsz_menu.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# sprinter function


def sprint(string):
    for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)
# Phase-1 : Intro


def phase1():
    font = pygame.font.Font('fonts/Trajan Pro.ttf', 24)
    backgroundImage = pygame.image.load('bgf1.jpg')
    char1_var = "character/zmb_right.png"
    mixer.music.load("sound/intro.mp3")
    mixer.music.play(-1)

    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()

    messages = [' They say, "We are all bounded by fate." ',
                'But fortune favours the brave as we all know.',
                'You are trapped in a dungeon with your nemesis. ',
                'Do you have what it takes to be the brave person and reach for the sky?',
                'Get set go to tear the shackles of darkness apart.',
                '...........'

                ]

    snip = font.render('', True, 'white')
    counter = 0
    active_message = 0
    message = messages[active_message]
    speed = 1
    done = False

    run = True

    while run:
        charac1 = pygame.image.load(char1_var)
        player1 = pygame.image.load("character/char1.png")
        player2 = pygame.image.load("character/char2.png")
        screen.blit(backgroundImage, (0, 0))
        screen.blit(charac1, (555, 250))

        timer.tick(60)
        pygame.draw.rect(screen, 'black', [0, 550, 1275, 150])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if active_message == len(messages) - 1:
                return 0

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1

                    if active_message % 2 == 0:
                        char1_var = "character/zmb_left.png"
                    elif active_message % 2 != 0:
                        char1_var = "character/zmb_right.png"

                    message = messages[active_message]
                    counter = 0

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (10, 580))
        screen.blit(player1, (100, 280))
        screen.blit(player2, (1000, 280))
        pygame.display.flip()

    pygame.quit()

# phase-2


def phase2():
    mixer.music.load("sound/gameplay.mp3")
    mixer.music.play(-1)
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font('fonts/Trajan Pro.ttf', 50)
    bg_p2 = pygame.image.load("einstein/bg_ph2.jpg")
    font_goal = pygame.font.Font('fonts/Trajan Pro.ttf', 20)

    # player red
    r1 = (random.randint(0, 10000000000)) % 2
    r2 = (random.randint(0, 10000000000)) % 2
    r3 = (random.randint(0, 10000000000)) % 2
    r4 = (random.randint(0, 10000000000)) % 2
    r5 = (random.randint(0, 10000000000)) % 2
    red_x = 20
    red_y = 80

    if r1 == 0 :
        red_text1 = "Down"
    else:
        red_text1 = "Up"
    if r2 == 0 :
        red_text2 = "Down"
    else:
        red_text2 = "Up"
    if r3 == 0 :
        red_text3 = "Down"
    else:
        red_text3 = "Up"
    if r4 == 0 :
        red_text4 = "Down"
    else:
        red_text4 = "Up"

    if r5 == 0 :
        red_text5 = "Down"
    else:
        red_text5 = "Up"

    goal_color = 'orange'
    red_goal = font_goal.render("RED GOAL : ", True, goal_color)
    r_txt1 = font_goal.render(red_text1, True, goal_color)
    r_txt2 = font_goal.render(red_text2, True, goal_color)
    r_txt3 = font_goal.render(red_text3, True, goal_color)
    r_txt4 = font_goal.render(red_text4, True, goal_color)
    r_txt5 = font_goal.render(red_text5, True, goal_color)

    # player blue
    b1 = (random.randint(0, 10000000000)) % 2
    b2 = (random.randint(0, 10000000000)) % 2
    b3 = (random.randint(0, 10000000000)) % 2
    b4 = (random.randint(0, 10000000000)) % 2
    b5 = (random.randint(0, 10000000000)) % 2
    blue_x = 20
    blue_y = 110

    if b1 == 0:
        blue_text1 = "Down"
    else:
        blue_text1 = "Up"
    if b2 == 0:
        blue_text2 = "Down"
    else:
        blue_text2 = "Up"
    if b3 == 0:
        blue_text3 = "Down"
    else:
        blue_text3 = "Up"
    if b4 == 0:
        blue_text4 = "Down"
    else:
        blue_text4 = "Up"
    if b5 == 0:
        blue_text5 = "Down"
    else:
        blue_text5 = "Up"

    bl_gl = 'cyan'
    blue_goal = font_goal.render("BlUE GOAL : ", True, bl_gl)
    b_txt1 = font_goal.render(blue_text1, True,  bl_gl)
    b_txt2 = font_goal.render(blue_text2, True,  bl_gl)
    b_txt3 = font_goal.render(blue_text3, True,  bl_gl)
    b_txt4 = font_goal.render(blue_text4, True,  bl_gl)
    b_txt5 = font_goal.render(blue_text5, True,  bl_gl)

    # warning message
    warn_mess = pygame.font.Font('fonts/Trajan Pro.ttf', 24)
    warn = warn_mess.render(" Beware! As soon as the game commences the winning pattern will disappear.", True, 'red')

    # Einstein
    stat1 = "einstein/down.png"
    v1 = 0
    stat2 = "einstein/up.png"
    v2 = 1
    stat3 = "einstein/up.png"
    v3 = 1
    stat4 = "einstein/down.png"
    v4 = 0
    stat5 = "einstein/down.png"
    v5 = 0

    surf1 = pygame.image.load(stat1)
    surf2 = pygame.image.load(stat2)
    surf3 = pygame.image.load(stat3)
    surf4 = pygame.image.load(stat4)
    surf5 = pygame.image.load(stat5)

    # dice
    dice1 = pygame.image.load("dice/dice.png")
    dice_button1 = pygame.Rect(20, 400, 180, 160)
    dice2 = pygame.image.load("dice/dice.png")
    dice_button2 = pygame.Rect(270, 400, 180, 160)
    dice3 = pygame.image.load("dice/dice.png")
    dice_button3 = pygame.Rect(520, 400, 180, 160)
    dice4 = pygame.image.load("dice/dice.png")
    dice_button4 = pygame.Rect(770, 400, 180, 160)
    dice5 = pygame.image.load("dice/dice.png")
    dice_button5 = pygame.Rect(1020, 400, 180, 160)

    # Dice turn name
    d_name1 = "Start"
    d_turn1 = font.render(d_name1, True, 'white')
    d_name2 = "Start"
    d_turn2 = font.render(d_name2, True, 'white')
    d_name3 = "Start"
    d_turn3 = font.render(d_name3, True, 'white')
    d_name4 = "Start"
    d_turn4 = font.render(d_name4, True, 'white')
    d_name5 = "Start"
    d_turn5 = font.render(d_name5, True, 'white')

    # now turn text
    turn = "Start"
    turn_color = 'magenta'
    turn_text = font.render(turn, True, turn_color)
    cl1 = cl2 = cl3 = cl4 = cl5 = 0

    button1 = pygame.Rect(20, 200, 200, 160)
    button2 = pygame.Rect(270, 200, 200, 160)
    button3 = pygame.Rect(520, 200, 200, 160)
    button4 = pygame.Rect(770, 200, 200, 160)
    button5 = pygame.Rect(1020, 200, 200, 160)

    st = True
    while st:

        timer.tick(60)
        win_bg = pygame.image.load("assets/Background.png")
        win_message = font.render("You Won !!", True, 'white')
        # screen.fill('pink')
        screen.blit(bg_p2, (0, 0))

        if v1 == r1 and v2 == r2 and v3 == r3 and v4 == r4 and v5 == r5:
            SCREEN.fill("black")
            phase3()

        elif v1 == b1 and v2 == b2 and v3 == b3 and v4 == b4 and v5 == b5 :
            SCREEN.fill("black")
            phase4()

        for events in pygame.event.get():

            dice1 = pygame.image.load("dice/dice.png")
            dice2 = pygame.image.load("dice/dice.png")
            dice3 = pygame.image.load("dice/dice.png")
            dice4 = pygame.image.load("dice/dice.png")
            dice5 = pygame.image.load("dice/dice.png")
            surf1 = pygame.image.load(stat1)
            surf2 = pygame.image.load(stat2)
            surf3 = pygame.image.load(stat3)
            surf4 = pygame.image.load(stat4)
            surf5 = pygame.image.load(stat5)
            d_turn1 = font.render(d_name1, True, 'white')
            d_turn2 = font.render(d_name2, True, 'white')
            d_turn3 = font.render(d_name3, True, 'white')
            d_turn4 = font.render(d_name4, True, 'white')
            d_turn5 = font.render(d_name5, True, 'white')
            turn_text = font.render(turn, True, turn_color)

            if events.type == pygame.KEYDOWN:

                # Dice keyboard control

                if events.key == pygame.K_RETURN:
                    t1 = random.randint(0, 1000000000)
                    t2 = random.randint(0, 1000000000)
                    t3 = random.randint(0, 1000000000)
                    t4 = random.randint(0, 1000000000)
                    t5 = random.randint(0, 1000000000)
                    red_x = 2000
                    blue_x = 2000

                    # dice music
                    dice_sound = mixer.Sound("sound/dice.mpeg")
                    dice_sound.play()

                    if t1 % 2 == 0:
                        dice1 = pygame.image.load("dice/red.png")
                        d_name1 = "RED"
                        cl1 = 0

                    elif t1 % 2 != 0:
                        dice1 = pygame.image.load("dice/blue.png")
                        d_name1 = "BLUE"
                        cl1 = 1

                    if t2 % 2 == 0:
                        dice2 = pygame.image.load("dice/red.png")
                        d_name2 = "RED"
                        cl2 = 0

                    elif t2 % 2 != 0:
                        dice2 = pygame.image.load("dice/blue.png")
                        d_name2 = "BLUE"
                        cl2 = 1

                    if t3 % 2 == 0:
                        dice3 = pygame.image.load("dice/red.png")
                        d_name3 = "RED"
                        cl3 = 0

                    elif t3 % 2 != 0:
                        dice3 = pygame.image.load("dice/blue.png")
                        d_name3 = "BLUE"
                        cl3 = 1

                    if t4 % 2 == 0:
                        dice4 = pygame.image.load("dice/red.png")
                        d_name4 = "RED"
                        cl4 = 0

                    elif t4 % 2 != 0:
                        dice4 = pygame.image.load("dice/blue.png")
                        d_name4 = "BLUE"
                        cl4 = 1

                    if t5 % 2 == 0:
                        dice5 = pygame.image.load("dice/red.png")
                        d_name5 = "RED"
                        cl5 = 0

                    elif t5 % 2 != 0:
                        dice5 = pygame.image.load("dice/blue.png")
                        d_name5 = "BLUE"
                        cl5 = 1
                    if cl5+cl1+cl4+cl3+cl2 > 2:
                        turn = "TURN : BLUE"
                        turn_color = 'blue'
                        blue_sound = mixer.Sound("sound/blue.mp3")
                        blue_sound.play()
                    else:
                        turn = "TURN : RED"
                        turn_color = 'red'
                        red_sound = mixer.Sound("sound/red.mp3")
                        red_sound.play()

            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if cl5 + cl1 + cl4 + cl3 + cl2 > 2:
                    if button1.collidepoint(events.pos) and v1 == 0 and cl1 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat1 = "einstein/up.png"
                        v1 = 1
                        pygame.display.update()
                    elif button1.collidepoint(events.pos) and v1 == 1 and cl1 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat1 = "einstein/down.png"
                        v1 = 0
                        pygame.display.update()
                    elif button2.collidepoint(events.pos) and v2 == 0 and cl2 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat2 = "einstein/up.png"
                        v2 = 1
                        pygame.display.update()
                    elif button2.collidepoint(events.pos) and v2 == 1 and cl2 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat2 = "einstein/down.png"
                        v2 = 0
                        pygame.display.update()

                    elif button3.collidepoint(events.pos) and v3 == 0 and cl3 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat3 = "einstein/up.png"
                        v3 = 1
                        pygame.display.update()
                    elif button3.collidepoint(events.pos) and v3 == 1 and cl3 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat3 = "einstein/down.png"
                        v3 = 0
                        pygame.display.update()

                    elif button4.collidepoint(events.pos) and v4 == 0 and cl4 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat4 = "einstein/up.png"
                        v4 = 1
                        pygame.display.update()
                    elif button4.collidepoint(events.pos) and v4 == 1 and cl4 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat4 = "einstein/down.png"
                        v4 = 0
                        pygame.display.update()
                    elif button5.collidepoint(events.pos) and v5 == 0 and cl5 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat5 = "einstein/up.png"
                        v5 = 1
                        pygame.display.update()
                    elif button5.collidepoint(events.pos) and v5 == 1 and cl5 == 0:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat5 = "einstein/down.png"
                        v5 = 0
                        pygame.display.update()
                else:
                    if button1.collidepoint(events.pos) and v1 == 0 and cl1 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat1 = "einstein/up.png"
                        v1 = 1
                        pygame.display.update()
                    elif button1.collidepoint(events.pos) and v1 == 1 and cl1 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat1 = "einstein/down.png"
                        v1 = 0
                        pygame.display.update()
                    elif button2.collidepoint(events.pos) and v2 == 0 and cl2 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat2 = "einstein/up.png"
                        v2 = 1
                        pygame.display.update()
                    elif button2.collidepoint(events.pos) and v2 == 1 and cl2 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat2 = "einstein/down.png"
                        v2 = 0
                        pygame.display.update()

                    elif button3.collidepoint(events.pos) and v3 == 0 and cl3 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat3 = "einstein/up.png"
                        v3 = 1
                        pygame.display.update()
                    elif button3.collidepoint(events.pos) and v3 == 1 and cl3 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat3 = "einstein/down.png"
                        v3 = 0
                        pygame.display.update()

                    elif button4.collidepoint(events.pos) and v4 == 0 and cl4 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat4 = "einstein/up.png"
                        v4 = 1
                        pygame.display.update()
                    elif button4.collidepoint(events.pos) and v4 == 1 and cl4 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat4 = "einstein/down.png"
                        v4 = 0
                        pygame.display.update()
                    elif button5.collidepoint(events.pos) and v5 == 0 and cl5 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat5 = "einstein/up.png"
                        v5 = 1
                        pygame.display.update()
                    elif button5.collidepoint(events.pos) and v5 == 1 and cl5 == 1:
                        turn_sound = mixer.Sound("sound/turn_head.mp3")
                        turn_sound.play()
                        stat5 = "einstein/down.png"
                        v5 = 0
                        pygame.display.update()

        # dice mouse control
        #             elif dice_button.collidepoint(events.pos):
        #                 t = random.randint( 0 , 1000000000 )
        #                 if t % 2 == 0:
        #                     dice = pygame.image.load("dice/red.png")
        #
        #                 elif t % 2 != 0:
        #                     dice = pygame.image.load("dice/blue.png")

        # pygame.draw.rect(screen, (110, 110, 110), button1)
        # pygame.draw.rect(screen, (110, 110, 110), button2)
        # pygame.draw.rect(screen, (110, 110, 110), button3)
        # pygame.draw.rect(screen, (110, 110, 110), button4)
        # pygame.draw.rect(screen, (110, 110, 110), button5)
        screen.blit(surf1, (button1.x, button1.y))
        screen.blit(surf2, (button2.x, button2.y))
        screen.blit(surf3, (button3.x, button3.y))
        screen.blit(surf4, (button4.x, button4.y))
        screen.blit(surf5, (button5.x, button5.y))
        screen.blit(dice1, (dice_button1.x, dice_button1.y))
        screen.blit(dice2, (dice_button2.x, dice_button2.y))
        screen.blit(dice3, (dice_button3.x, dice_button3.y))
        screen.blit(dice4, (dice_button4.x, dice_button4.y))
        screen.blit(dice5, (dice_button5.x, dice_button5.y))
        screen.blit(d_turn1, (60, 600))
        screen.blit(d_turn2, (310, 600))
        screen.blit(d_turn3, (560, 600))
        screen.blit(d_turn4, (810, 600))
        screen.blit(d_turn5, (1060, 600))
        screen.blit(turn_text, (900, 100))

        # Goal Red
        screen.blit(red_goal, (red_x, red_y))
        screen.blit(r_txt1, (red_x+160, red_y))
        screen.blit(r_txt2, (red_x+260, red_y))
        screen.blit(r_txt3, (red_x+360, red_y))
        screen.blit(r_txt4, (red_x+460, red_y))
        screen.blit(r_txt5, (red_x+560, red_y))

        # Goal Blue
        screen.blit(blue_goal, (blue_x, blue_y))
        screen.blit(b_txt1, (blue_x + 160, blue_y))
        screen.blit(b_txt2, (blue_x + 260, blue_y))
        screen.blit(b_txt3, (blue_x + 360, blue_y))
        screen.blit(b_txt4, (blue_x + 460, blue_y))
        screen.blit(b_txt5, (blue_x + 560, blue_y))

        # Warning
        screen.blit(warn, (blue_x + 30 , 20))

        pygame.display.update()
    pygame.quit()




# phase -3 : game1 winner
def phase3():
    mixer.music.load("sound/gameplay.mp3")
    mixer.music.play(-1)
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720))
    while True:
        timer.tick(60)
        win_clr = 'orange'
        winn_txt = pygame.font.Font("fonts/Trajan Pro.ttf", 50)
        winner_text = winn_txt.render(" Congrats RED Team ", True, win_clr)
        game1_winner = pygame.image.load("bg/rsz_win.jpg")
        char_win = pygame.image.load("character/win_char_bg.png")
        chat1 = pygame.image.load("character/conv111.png")
        chat2 = pygame.image.load("character/conv22.png")
        charac1 = pygame.image.load("character/zmb_right.png")
        screen.blit(game1_winner, (0, 0))
        screen.blit(char_win, (700, 500))
        screen.blit(winner_text, (330, 20))
        screen.blit(chat1, (670, 400))
        screen.blit(chat2, (160, 320))
        screen.blit(charac1, (200, 450))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

# blue win


def phase4():
    mixer.music.load("sound/gameplay.mp3")
    mixer.music.play(-1)
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720))
    while True:
        timer.tick(60)
        win_clr = 'orange'
        winn_txt = pygame.font.Font("fonts/Trajan Pro.ttf", 50)
        winner_text = winn_txt.render(" Congrats BLUE Team ", True, win_clr)
        game1_winner = pygame.image.load("bg/rsz_win.jpg")
        char_win = pygame.image.load("character/win_char_bg.png")
        chat1 = pygame.image.load("character/conv111.png")
        chat2 = pygame.image.load("character/conv22.png")
        charac1 = pygame.image.load("character/zmb_right.png")
        screen.blit(game1_winner, (0, 0))
        screen.blit(char_win, (700, 500))
        screen.blit(winner_text, (330, 20))
        screen.blit(chat1, (670, 400))
        screen.blit(chat2, (160, 320))
        screen.blit(charac1, (200, 450))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


def play():
    while True:
        phase1()
        phase2()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="START", font=get_font(70), base_color="red", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="GAMEPLAY", font=get_font(75), base_color="red", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="red", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
