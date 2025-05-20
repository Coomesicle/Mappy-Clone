import pygame

class Entity:
    def __init__(self, x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS, entity_type, color=(0, 0, 255)):
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.rail_index = rail_index
        self.rails = RAIL_Y_POSITIONS
        self.trampolines = TRAMPOLINE_X_POS

        self.rect = self.image.get_rect(topleft=(x, self.rails[self.rail_index]))
        self.speed = 5
        self.jumping = False
        self.falling = False
        self.jump_speed = -5

        # Entity Type
        self.entity_type = entity_type

    def move_horizontal(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))


    def update_movement(self):
        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))

        self.check_trampoline_bounce()

        if self.jumping:
            self.rect.y += self.jump_speed
            if self.rect.bottom + 30 < self.rails[-1]:
                self.jumping = False
                self.falling = True
        elif self.falling:
            self.rect.y -= self.jump_speed
            if self.rect.bottom > self.rails[0]:
                self.falling = False
                self.jumping = True

        else:
            # Snap to rail only when not jumping
            self.rect.y = self.rails[self.rail_index] - self.rect.height


    def check_trampoline_bounce(self):
        
        for tramp_x in self.trampolines:
            if tramp_x <= self.rect.centerx <= tramp_x + 50:
                if not self.falling and not self.jumping:
                    self.falling = True
                return
        closest = self.rail_index
        for i, height in enumerate(self.rails):
            if self.rect.y < height:
                closest = i
        self.rail_index = closest
        self.jumping = False
        self.falling = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
