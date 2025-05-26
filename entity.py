import pygame

class Entity:
    def __init__(self, x, rail_index, entity_type, game, color=(0, 0, 255)):
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

    def move_horizontal(self, dx):
        if (self.rect.centerx + dx > self.game.SCREEN_WIDTH or self.rect.centerx + dx < 0):
            return False
        self.rect.centerx += dx
        self.rect.x = max(0, min(self.rect.x, self.game.SCREEN_WIDTH - self.rect.width))
        return True


    def update_movement(self):
        self.rect.x = max(0, min(self.rect.x, self.game.SCREEN_WIDTH - self.rect.width))

        on_trampoline = self.check_trampoline_bounce()
        if on_trampoline:
            if self.jumping:
                self.rect.y += self.jump_speed
                if self.rect.bottom + 30 < self.game.rails[-1]:
                    self.jumping = False
                    self.falling = True
            elif self.falling:
                self.rect.y -= self.jump_speed
                if self.rect.bottom > self.game.rails[0]:
                    self.falling = False
                    self.jumping = True
        else:
            # Snap to rail only when not jumping
            self.rect.y = self.game.rails[self.rail_index] - self.rect.height


    def check_trampoline_bounce(self):
        if self.jumping or self.falling:
            return True
        
        for tramp_x in self.game.trampolines:
            if tramp_x <= self.rect.centerx <= tramp_x + 50:
                if not self.falling and not self.jumping:
                    self.falling = True
                    self.rect.centerx = tramp_x + 25
                return True
        return False
    
        
    def exit_trampoline(self):
        for i, rails_y in enumerate(self.game.rails):
            if rails_y - 100 <= self.rect.centery <= rails_y:
                self.rect.y = self.game.rails[i] - self.rect.height
                self.rail_index = i
        self.jumping = False
        self.falling = False
        self.rect.y = self.game.rails[self.rail_index] - self.rect.height

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    