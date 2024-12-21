import pygame
from pygame.math import Vector2
pygame.init()

from .colors import *

class Transition():
    def __init__(self, game):
        self.game = game

        self.o_img = pygame.transform.scale(pygame.image.load(self.game.path + "\\assets\\pixel.png").convert(), (1, self.game.res.y))
        self.o_img.fill(WHITE)
        self.img = self.o_img
        self.rect = self.img.get_rect()
        self.ended = False
        self.speed = 1

    def update(self, on_middle, *args):
        print("jjj")
        while self.rect.width < self.game.res.x:
            self.rect.width += self.speed
            self.img = pygame.transform.scale(self.o_img, (self.rect.width, self.rect.height))
            print(self.img.get_rect())

        on_middle(*args)

        while self.rect.width > 1:
            self.rect.width -= self.speed
            self.img = pygame.transform.scale(self.o_img, (self.rect.width, self.rect.height))
            print(self.img.get_rect())

        self.ended = True

    def draw(self):
        self.game.screen.blit(self.img, self.rect)

class MusicManager():
    def __init__(self, game, tracks):
        self.game = game
        self.tracks = tracks
        self.track = 0
        self.song = self.tracks[self.track]
        self.song.play()
        self.song.set_volume(self.game.music_volume)

        self.song_start = pygame.time.get_ticks() / 1000
        self.song_end = self.song_start + self.song.get_length()
        self.song_buffer = 5000

    def next_song(self):
        if not self.track == len(self.tracks):
            self.track += 1
            self.song = self.tracks[self.track]
            self.song.play()
            self.song.set_volume(self.game.music_volume)

        else:
            self.track = 0
            self.song = self.tracks[self.track]
            self.song.play()
            self.song.set_volume(self.game.music_volume)


        self.song_start = pygame.time.get_ticks() / 1000
        self.song_end = self.song_start + self.song.get_length()

    def update(self):
        time = pygame.time.get_ticks()
        if (time - self.song_buffer) / 1000 >= self.song_end:
            self.next_song()