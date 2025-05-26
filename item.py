import pygame
import random

class Item:
    def __init__(self, game):
        self.game = game
        self.rail_index = random.randint(0, 4)
        options = [random.randint(50, game.trampolines[1]-25), random.randint(game.trampolines[1]+25, game.SCREEN_WIDTH-50)]
        self.x = random.choice(options)

        self.image = pygame.Surface((30, 30))
        self.image.fill((0,255,0))

        self.rect = self.image.get_rect(midbottom=(self.x, game.rails[self.rail_index]))

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)