from random import randint, sample
from Obstacles import Obstacle
from pygame.image import load as load_image

class LocationGenerate:
    def __init__(self, window, groups):
        self.lines = groups
        self.window = window

    def generate_next(self):
        num_barricades = randint(1, 2)
        return sample((1, 2, 3), num_barricades)

    def get_sprite(self):
        return load_image("")

    def generate_speed(self):
        return randint(1, 5)

    def add_random_obstacles(self, speed=None, sprite=None):
        if sprite is None:
            sprite = self.get_sprite()
        if speed is None:
            speed = self.generate_speed()
        obstacles_count = self.generate_next()
        for i in obstacles_count:
            Obstacle(speed, sprite, i, self.window, self.lines[i - 1])
