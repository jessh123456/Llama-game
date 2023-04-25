import pygame

pygame.init()

screen = pygame.display.set_mode((700, 350))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - by Jess Hansen")
white = (200, 200, 200)
screen.fill(white)
pygame.display.update()
quit_game = False

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


pygame.quit()
quit()
