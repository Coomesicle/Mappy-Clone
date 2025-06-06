import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, x, rail_index, game):
        super().__init__(x, rail_index, "player", game, color=(0, 0, 255))
        self.lives = 3
        self.alive = True
        self.points = 0

    def handle_input(self):
        if self.falling:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.jumping:
                if self.move_horizontal(-26):
                    self.exit_trampoline()
            else:
                self.move_horizontal(-self.speed)
        if keys[pygame.K_RIGHT]:
            if self.jumping:
                if self.move_horizontal(26):
                    self.exit_trampoline()
            else:
                self.move_horizontal(self.speed)

    def update(self):
        if not self.alive:
            return
        self.handle_input()
        self.update_movement()

    def kill(self):
        self.alive = False



