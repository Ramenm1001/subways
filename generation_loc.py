from random import randint, sample
from Obstacles import Obstacle


def generate_next():
    num_barricades = randint(1, 2)
    return sample((1, 2, 3), num_barricades)


def get_sprite():
    return ""


def generate_speed():
    return randint(1, 5)


def add_random_obstacles(win, speed=None, sprite=None):
    if sprite is None:
        sprite = get_sprite()
    if speed is None:
        speed = generate_speed()
    obstacles_count = generate_next()
    for i in obstacles_count:
        Obstacle(speed, sprite, i, win, eval(f"line{i}"))
