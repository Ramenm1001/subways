import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed, sprite, line, win, group_to_add, *group):
        super().__init__(*group)
        lines = {1: 0, 2: 100, 3: 200}
        self.sprite = sprite
        self.rect = pygame.Rect(500, lines[line], 400, 80)
        group_to_add.add(self)
        self.win = win
        self.speed = speed

    def draw(self):
        self.win.blit(self.sprite, (self.rect.x, self.rect.y))

    def update(self):
        self.rect = self.rect.move(self.speed, 0)
        if self.rect.x < 0:
            self.kill()
        self.draw()


