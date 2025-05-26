import pygame
import random

class Game:
    def __init__(self, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.rails = RAIL_Y_POSITIONS
        self.trampolines = TRAMPOLINE_X_POS

    def getCurrGame(self):
        return self
    
class Item:
    def __init__(self, x):
        se
        