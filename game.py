import random
import pygame
import sys
from player import Player
from entity import Entity
from enemy import Enemy
from item import Item

class Game:
    def __init__(self, SCREEN_WIDTH, RAIL_Y_POSITIONS, TRAMPOLINE_X_POS):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.rails = RAIL_Y_POSITIONS
        self.trampolines = TRAMPOLINE_X_POS
        self.item = False
        self.items = []
        self.gameStart = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def startGame(self):
        self.player1 = Player(700, 0, self)
        self.enemy1 = Enemy(700, 0, self)
        self.gameStart = True

    def update(self, screen):
        if self.player1.alive:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            self.player1.update()
            
            self.enemy1.update(self.player1)

            if not self.item:
                newItem = Item(self)
                self.items.append(newItem)
                self.item = True
            else:
                if self.check_collision(self.player1, self.items[-1]):
                    self.items.clear()
                    self.item = False
                    self.player1.points += 20

            return self.player1.points
        else:
            self.gameStart = False
            return 0

    def draw(self, surface):
        self.draw_rails(surface)
        self.player1.draw(surface)
        self.enemy1.draw(surface)

        for i in self.items:
            i.draw(surface)

    def draw_rails(self, surface):
        lineColor = (100, 100, 100)
        trampolineColor = (140, 45, 20)
        for i, y in enumerate(self.rails):
            if i == 0:
                # Draw trampolines at specified x positions
                for x in self.trampolines:
                    pygame.draw.line(surface, trampolineColor, (x, y), (x + 50, y), 4)

            # Draw the rest of the rail line
            pygame.draw.line(surface, lineColor, (50, y), (self.SCREEN_WIDTH/2 - 25, y), 4)
            pygame.draw.line(surface, lineColor, (self.SCREEN_WIDTH/2 + 25, y), (self.SCREEN_WIDTH - 50, y), 4)

    def printScore(self, surface, font):
        text = f"Score: {self.player1.points}"
        text_surface = font.render(text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.topright = (self.SCREEN_WIDTH - 10, 10)  # 10px from right and top

        surface.blit(text_surface, text_rect)

    def gameOn(self):
        return self.gameStart

    def check_collision(self, obj1, obj2):
        if obj1.rect.centerx - 15 <= obj2.rect.centerx <= obj1.rect.centerx + 15 and obj1.rail_index == obj2.rail_index:
            return True
        return False