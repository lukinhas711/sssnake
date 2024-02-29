import pygame
import random

pygame.init()
pygame.display.set_caption('Ssssnake 🐍')
width, height = 1080, 720
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)

square_size = 20
game_speed = 15

def run_game():
    end_game = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_size = 1
    snake_foods = []

    while not end_game:
        display.fill(color_black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True



run_game()