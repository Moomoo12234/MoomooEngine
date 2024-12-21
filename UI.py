import pygame
from pygame.math import Vector2
pygame.init()
import sys

from .colors import *

class Button(pygame.sprite.Sprite):
    def __init__(self, game, scene, pos, size, on_click, highlight = False):
        super().__init__()
        self.game = game
        self.scene = scene
        self.pos = Vector2(pos)
        self.on_click = on_click

        self.hover = False

        self.o_image = pygame.transform.scale(pygame.image.load("pixel.png"), (size))
        self.image = self.o_image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        mouse = pygame.mouse.get_pressed()
        if self.hover and mouse[0]:
            self.on_click(self)

class ProgressBar():
    def __init__(self, game, scene, pos, size, num, max_num, fcol = WHITE, bcol = (255 / 2, 255 / 2, 255 / 2)):
        super().__init__()
        self.game = game
        self.scene = scene

        self.pos = Vector2(pos)
        self.num = num
        self.max_num = max_num
        self.size = Vector2(size)
        self.fcol = fcol
        self.bcol = bcol

        self.o_image = pygame.transform.scale(pygame.image.load(self.game.path + "\\assets\\pixel.png").convert(), (self.size.x, self.size.y))
        self.fimage = self.o_image
        self.fimage.fill(self.fcol)
        self.bimage = self.o_image
        self.bimage.fill(self.bcol)
        self.brect = self.bimage.get_rect()
        self.frect = self.fimage.get_rect()
        self.frect.topleft = self.pos
        self.brect.topleft = self.pos

    def update(self):
        self.frect.width = self.size.x / self.max_num * self.num
        self.frect.normalize()
        self.fimage = pygame.transform.scale(self.o_image, (self.frect.width, self.frect.height))
        self.fimage.fill(self.fcol)
        self.frect = self.fimage.get_rect()
        self.frect.topleft = self.pos

    def draw(self):
        self.game.screen.blit(self.bimage, self.brect)
        self.game.screen.blit(self.fimage, self.frect)

class Text(pygame.font.Font):                                   #adds button functionality if set to "btn"
    def __init__(self, game, scene, pos: int, size: int, text: str, font: str, tag: str, on_click = None, juice: bool = True, juice_sound = None, col: tuple = (255, 255, 255)):
        super().__init__(font, size)
        self.game = game
        self.scene = scene

        self.size = Vector2(size)
        self.pos = Vector2(pos)
        self.text = text
        self.tag = tag
        self.juice = juice
        self.juice_sound = juice_sound
        self.col = col
        self.on_click = on_click

        self.o_font_surf = self.render(self.text, False, self.col)
        self.font_surf = self.o_font_surf
        self.rect = self.font_surf.get_rect()

        self.rect.center = self.pos

        self.hover = False
        self.scaled = False

    def set_text(self, text):
        self.o_font_surf = self.render(text, False, self.col)
        self.font_surf = self.o_font_surf
        self.rect = self.font_surf.get_rect()
        self.rect.center = self.pos

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        mouse = pygame.mouse.get_pressed()
        if self.hover and mouse[0]:
            self.on_click()

    def draw(self):
        if self.juice and self.tag == "btn":
            if self.hover and not self.scaled:
                self.font_surf = pygame.transform.scale(self.o_font_surf, (self.o_font_surf.get_width() * 1.5, self.o_font_surf.get_height() * 1.5))
                self.font_surf = pygame.transform.rotate(self.font_surf, -5)
                self.rect = self.font_surf.get_rect()
                self.rect.center = self.pos
                self.scaled = True
                self.juice_sound.play()
            if not self.hover and self.scaled:
                self.font_surf = self.o_font_surf
                self.rect = self.font_surf.get_rect()
                self.rect.center = self.pos
                self.scaled = False
                self.juice_sound.play()

        self.game.screen.blit(self.font_surf, self.rect)