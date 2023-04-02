#Pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Define the game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game')

# Define the player's position and speed
player_x = 400
player_y = 500
player_speed = 5

# Define the enemy's position and speed
enemy_x = random.randint(0, WINDOW_WIDTH)
enemy_y = 0
enemy_speed = 3

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - 50:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > WINDOW_HEIGHT:
        enemy_x = random.randint(0, WINDOW_WIDTH)
        enemy_y = 0

    # Check for collisions
    if abs(player_x - enemy_x) < 50 and abs(player_y - enemy_y) < 50:
        running = False

    # Clear the screen and draw the game objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), (enemy_x, enemy_y, 50, 50))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
