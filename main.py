import pygame
import random

pygame.init()
pygame.display.set_caption('Sicuri 🐍')
width, height = 1080, 720
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)

square_size = 20
game_speed = 15


def generate_food():
    food_x = round(random.randrange(0, width - square_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y


def draw_food(size, food_x, food_y):
    pygame.draw.rect(display, color_green, [food_x, food_y, size, size])


def draw_snake(size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(display, color_white, [pixel[0], pixel[1], size, size])


def draw_score(score):
    font = pygame.font.SysFont("Inter", 50)
    text = font.render(f"Pontos: {score}", True, color_green)
    display.blit(text, [4, 4])


def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    if key == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    if key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    if key == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0

    return speed_x, speed_y


def run_game():
    end_game = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_size = 1
    snake_pixels = []

    food_x, food_y = generate_food()

    while not end_game:
        display.fill(color_black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                x_speed, y_speed = select_speed(event.key)

        draw_food(square_size, food_x, food_y)

        if x < 0 or x >= width or y < 0 or y >= height:
            end_game: True

        draw_score(snake_size - 1)

        x += x_speed
        y += y_speed

        snake_pixels.append([x, y])
        if len(snake_pixels) > snake_size:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1:]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(square_size, snake_pixels)

        pygame.display.update()

        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = generate_food()

        clock.tick(game_speed)


run_game()
