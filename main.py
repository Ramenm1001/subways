import pygame
from Obstacles import Obstacle
from player import Player
from generation_loc import add_random_obstacles

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

line1 = pygame.sprite.Group()
line2 = pygame.sprite.Group()
line3 = pygame.sprite.Group()
player = Player(win)

run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    line1.update()
    line2.update()
    line3.update()
    player.update()

    if not(line1 or line2 or line3):
        add_random_obstacles()

pygame.quit()