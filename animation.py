import pygame
from pygame.math import Vector2
pygame.init()

from .spritesheet import *

class Animation(pygame.sprite.Sprite):
    def __init__(self, game, scene, spritesheet, pos, sprite_size):
        super().__init__()
        self.game = game
        self.scene = scene

        self.spritesheet = Spritesheet(spritesheet)
        self.size = pygame.image.load(spritesheet).convert()
        self.size = self.size.get_rect()
        self.size = Vector2(self.size.width, self.size.height)
        self.sprite_size = Vector2(sprite_size)
        self.sprite_pos = Vector2()
        self.pos = pos

        self.image = self.spritesheet.image_at((self.sprite_pos.x, self.sprite_pos.y, self.sprite_size.x, self.sprite_size.y), (8, 20, 30))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.playing = False
        self.played = False

        self.tag = "animation"
    def play(self):
        self.playing = True
        self.sprite_pos = Vector2()


    def update(self):
        if self.playing:
            if self.sprite_pos.x == self.size.x - self.sprite_size.x:
                if self.sprite_pos.y == self.size.y - self.sprite_size.y:
                    self.playing = False
                    self.played = True
                else:
                    self.sprite_pos.x = 0
                    self.sprite_pos.y += self.sprite_size.y
            else:
                self.sprite_pos.x += self.sprite_size.x

        elif self.played:
            self.scene.sprites.remove(self)

        self.image = self.spritesheet.image_at((self.sprite_pos.x, self.sprite_pos.y, self.sprite_size.x, self.sprite_size.y))
        self.image.set_colorkey((8, 20, 30))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
