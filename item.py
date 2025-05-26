import pygame
from game import Game

class Game(Item):
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.game = game

        self.rail_index = rail_index

        self.rect = self.image.get_rect(topleft=(x, game.rails[self.rail_index]))
        self.speed = 5
        self.jumping = False
        self.falling = False
        self.jump_speed = -5

        # Entity Type
        self.entity_type = entity_type