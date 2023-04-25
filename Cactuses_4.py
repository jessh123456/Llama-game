import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((700, 350))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Jess Hansen")
background = pygame.image.load('ground.png')
resized_background = pygame.transform.smoothscale(background, [700, 100])
screen.blit(resized_background, (0, 157))
clock = pygame.time.Clock()
white = (200, 200, 200)
screen.fill(white)
quit_game = False
llama_x = 100
llama_y = 200
cactus_x = 700
new_cactus = 700
new_2_cactus = 700
new_3_cactus = 700
new_4_cactus = 700
cactus_appearance = random.randrange(200, 500)
cactus_y = 200
llama_vel = 20
cactus_move = 7
Y_GRAVITY = 2
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False
llama_2_running = pygame.transform.scale(pygame.image.load('Llama3.png'), (45, 45))
llama_1_running = pygame.transform.scale(pygame.image.load('Llama2.png'), (45, 45))
llama_jump = pygame.transform.scale(pygame.image.load('Llama.png'), (45, 45))
cactus = pygame.transform.scale(pygame.image.load('cactus.png'), (45, 45))
counter = 0
first_time = True
run = False
run_2 = False
run_3 = False
run_4 = False
run_5 = False


while not quit_game:
    llama_position = pygame.Rect(llama_x, llama_y, 45, 45)
    cactus_position = pygame.Rect(cactus_x, cactus_y, 45, 45)
    cactus_2_position = pygame.Rect(new_cactus, cactus_y, 45, 45)
    cactus_3_position = pygame.Rect(new_2_cactus, cactus_y, 45, 45)
    cactus_4_position = pygame.Rect(new_3_cactus, cactus_y, 45, 45)
    cactus_5_position = pygame.Rect(new_4_cactus, cactus_y, 45, 45)
    screen.fill(white)

    if not jumping:
        counter += 1
        selection = counter // 2 % 2
        if selection == 0:
            screen.blit(llama_1_running, llama_position)
        elif selection == 1:
            screen.blit(llama_2_running, llama_position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping = True  # So jump happens only when space bar is pressed
        cactus_start = True

    if jumping:
        llama_y -= Y_VELOCITY  # Makes Llama move up by 20px
        Y_VELOCITY -= Y_GRAVITY  # Reduces velocity by 1px

        if Y_VELOCITY < -JUMP_HEIGHT:  # When Y_VELOCITY is under -20
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT  # Rests Y_VELOCITY to 20
        screen.blit(llama_jump, llama_position)

    screen.blit(resized_background, (0, 187))
    screen.blit(cactus, cactus_position)
    screen.blit(cactus, cactus_2_position)
    screen.blit(cactus, cactus_3_position)
    screen.blit(cactus, cactus_4_position)
    screen.blit(cactus, cactus_5_position)
    clock.tick(30)
    if first_time:
        cactus_x -= cactus_move
        screen.blit(cactus, cactus_position)
        pygame.display.update()
        if cactus_x <= 0:
            first_time = False
            cactus_x = 700

    if cactus_x < cactus_appearance:
        run = True
    if run:
        new_cactus -= cactus_move
        screen.blit(cactus, cactus_2_position)
        pygame.display.update()
        cactus_appearance = random.randrange(100, 500)
        if new_cactus <= 0:
            new_cactus = 700
            run = False

    if new_cactus < cactus_appearance:
        run_2 = True
    if run_2:
        new_2_cactus -= cactus_move
        screen.blit(cactus, cactus_3_position)
        pygame.display.update()
        cactus_appearance = random.randrange(100, 500)
        if new_2_cactus <= 0:
            new_2_cactus = 700
            run_2 = False

    if new_2_cactus < cactus_appearance:
        run_3 = True
    if run_3:
        new_3_cactus -= cactus_move
        screen.blit(cactus, cactus_4_position)
        pygame.display.update()
        cactus_appearance = random.randrange(100, 500)
        if new_3_cactus <= 0:
            new_3_cactus = 700
            run_3 = False

    if new_3_cactus < cactus_appearance:
        run_4 = True
    if run_4:
        new_4_cactus -= cactus_move
        screen.blit(cactus, cactus_5_position)
        pygame.display.update()
        cactus_appearance = random.randrange(100, 500)
        if new_4_cactus <= 0:
            new_4_cactus = 700
            run_4 = False

    if new_4_cactus < cactus_appearance:
        run_5 = True
    if run_5:
        cactus_x -= cactus_move
        screen.blit(cactus, cactus_position)
        pygame.display.update()
        cactus_appearance = random.randrange(100, 500)
        if cactus_x <= 0:
            cactus_x = 700
            run_5 = False

pygame.quit()
quit()
