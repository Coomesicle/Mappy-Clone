import pygame
import random
from entity import Entity

class Enemy(Entity):
    def __init__(self, x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS):
        super().__init__(SCREEN_WIDTH-x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS, "enemy", color=(255, 0, 0))
        self.direction = 1
    def update(self, player):
        # Always move when not on trampoline
        if not self.falling and not self.jumping and self.direction is 0:
            if self.rect.centerx < player.rect.centerx:
                self.direction = 1
            elif self.rect.centerx > player.rect.centerx:
                self.direction = -1
        else:
            if abs(self.rect.centery - player.rect.x) < 40:
                if self.rect.x > player.rect.x:
                    self.direction = -1
                else:
                    self.direction = 1
            else:
                self.direction = 0

        self.move_horizontal(self.speed * self.direction)
        self.update_movement()
        

    def update(self, player):
        # Check if enemy is on a trampoline (more precise check)
        on_trampoline = self.falling or self.jumping
        
        # Only allow direction changes when properly on a trampoline
        if on_trampoline:
            # Move toward player when on trampoline
            if self.rect.centerx < player.rect.centerx:
                self.direction = 1
            elif self.rect.centerx > player.rect.centerx:
                self.direction = -1

        # Set initial direction if none is set
        elif self.direction == 0:
            if self.rect.centerx < player.rect.centerx:
                self.direction = 1
            else:
                self.direction = -1
        
        self.move_horizontal(self.speed * self.direction)
        self.update_movement()

