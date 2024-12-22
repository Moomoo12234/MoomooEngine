import pygame
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
import sys, array


from .colors import *
from .managers import *
from . import scenes

class Window():
    def __init__(self, path: str, res: tuple, fpsLimit: int = 60):
        self.path = path
        self.res = Vector2(res)
        self.window = pygame.display.set_mode(self.res)
        self.screen = pygame.Surface(self.res)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.bg = BLACK
        self.fpsLimit = fpsLimit

        self.music_volume = 0.1
        self.volume = 0.1

        self.scenes = []
        self.scene_manager = scenes.SceneManager(self, self.scenes)#, Transition)
        self.music_manager = None
        self.bloom = 3.0

        self.fullscreen = False

    def update(self):
        self.scene_manager.update_scene()
        if self.music_manager:
            self.music_manager.update()

    def draw(self):
        self.screen.fill(self.bg)
        self.scene_manager.draw_scene()
        self.window.blit(self.screen, self.screen.get_rect())

    def run(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_f:
                        if not self.fullscreen:
                            self.window = pygame.display.set_mode((self.res.x, self.res.y), pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN)
                        else:
                            self.window = pygame.display.set_mode((self.res.x, self.res.y), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
                        self.fullscreen = not self.fullscreen
            self.draw()

            self.update()

            pygame.display.flip()

            self.clock.tick(self.fpsLimit)