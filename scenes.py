import pygame
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
import sys, array

from . import window

class SceneManager():
    def __init__(self, game: window.Window, scenes: array):#, transition):
        self.game = game

        self.scene = 0
        self.scenes = scenes

        #self.transition = transition(self.game)

    def set_scene(self, scene):
        self.scene = scene

    def update_scene(self):
        self.scenes[self.scene]._update()

    def draw_scene(self):
        self.scenes[self.scene]._draw()

class Scene():
    def __init__(self, game: window.Window, bg_col: tuple):
        self.game = game

        self.bg_col = bg_col

    def update(self):
        pass

    def draw(self):
        pass

    def _draw(self):
        self.game.screen.fill(self.bg_col)
        self.draw()

    def _update(self):
        self.update()