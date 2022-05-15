import pygame
from main import win

class Player(pygame.sprite.Sprite):
    def __init__(self, win):
        self.line = 2
        self.win = win
        self.frames = []
        self.sheet = pygame.image.load('sprites/player.png')
        self.cut_sheet(self.sheet, 5, 2)
        self.cur_frame = 0
        self.dict = {1: (100, 100), 2: (100, 300), 3: (100, 500)}
        self.rect.x, self.rect.y = self.dict[self.line]
        self.image = self.frames[self.cur_frame]


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // columns,
                                self.sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.line != 1:
                self.line -= 1
        elif keys[pygame.K_d]:
            if self.line != 3:
                self.line -= 1
        self.rect = pygame.Rect(0, 0, self.dict[self.line])
        self.draw()

    def draw(self):
        self.win.blit(self.image, (self.rect.x, self.rect.y))
