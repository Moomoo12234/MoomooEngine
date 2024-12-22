import pygame
from pygame.math import Vector2
import math
pygame.init()

def look(pos1, pos2):
        dist = Vector2(pos2.x - pos1.x, pos2.y - pos1.y)
        return math.degrees(math.atan2(dist.x, dist.y))

def roundDecimals(num: float, decimals: int):
        if decimals == 0:
                decimals = 1
        
        return round(num * (10 ** decimals)) / (10 ** decimals)