import pygame

pygame.init()

screen = pygame.display.set_mode((700, 350))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Jess Hansen")
background = pygame.image.load('ground.png')
resized_background = pygame.transform.smoothscale(background, [10000, 100])
screen.blit(resized_background, (0, 157))
clock = pygame.time.Clock()
white = (200, 200, 200)
screen.fill(white)
quit_game = False
llama_x = 100
llama_y = 200
llama_vel = 20
Y_GRAVITY = 2
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
jumping = False


while not quit_game:
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

    llama_position = pygame.Rect(llama_x, llama_y, 45, 45)
    llama_jump = pygame.transform.scale(pygame.image.load('Llama.png'), (45, 45))
    screen.fill(white)
    screen.blit(llama_jump, llama_position)
    screen.blit(resized_background, (0, 186))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
