import pygame
import random

pygame.init()
pygame.display.set_caption('Cobrinha')
width, height = 1200, 900
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)

square_size = 20
game_speed = 15

# loop
def run_game():
    end_game = False

    while not end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True



# interface
# score
# snake
# food

# logic to end game
# self collision
# wall collision

# user interactions
# close
# keyboard


run_game()