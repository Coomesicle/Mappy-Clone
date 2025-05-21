import pygame
import random
from entity import Entity

class Enemy(Entity):
    def __init__(self, x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS):
        super().__init__(SCREEN_WIDTH-x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS, "enemy", color=(255, 0, 0))
        self.direction = 1

        

    def update(self, player):

        on_trampoline = self.check_trampoline_bounce()
        
        if on_trampoline and self.jumping:
            if abs(player.rect.centery - self.rect.centery) < 5:
                if self.rect.centerx < player.rect.centerx:
                    self.direction = 1
                elif self.rect.centerx > player.rect.centerx:
                    self.direction = -1
                self.move_horizontal(26 * self.direction)
                self.exit_trampoline()
                
        elif not self.falling:
            self.move_horizontal(self.speed * self.direction)
        self.update_movement()


