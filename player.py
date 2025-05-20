import pygame


class Player:
    def __init__(self, x, rail_index, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS):
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))  # Blue square as player
        self.rail_index = rail_index
        self.rails = RAIL_Y_POSITIONS
        self.trampolines = TRAMPOLINE_X_POS
        self.rect = self.image.get_rect(topleft=(x, self.rails[self.rail_index]))
        self.speed = 5
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.jumping = False
        self.jump_target_y = self.rect.y
        self.jump_speed = -5

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self.handle_input()
        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - self.rect.width))

        if self.jumping:
            # Smooth upward motion
            self.rect.y += self.jump_speed
            if self.rect.y <= self.jump_target_y:
                self.rect.y = self.jump_target_y
                self.jumping = False

        else:
            # Snap to rail only when not jumping
            self.rect.y = self.rails[self.rail_index] - self.rect.height
            self.check_trampoline_bounce()


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    

    def check_trampoline_bounce(self):
        if self.jumping or self.rail_index == len(self.rails) - 1 :
            return
        
        print(self.rail_index)
        player_mid_x = self.rect.centerx
        for tramp_x in self.trampolines:
            if tramp_x <= player_mid_x <= tramp_x + 50:
                self.jumping = True
                self.rail_index += 1  # We're moving to the rail above
                self.jump_target_y = self.rails[self.rail_index] - self.rect.height  # Align top of rect
                break

