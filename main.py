import pygame
import sys
from player import Player
from entity import Entity
from enemy import Enemy

pygame.init()

xScreen = 800
yScreen = 600
RAIL_Y_POSITIONS = [550, 450, 350, 250, 150]
TRAMPOLINE_X_POSITIONS = [0, xScreen/2-25, xScreen-50]

screen = pygame.display.set_mode((xScreen, yScreen))
pygame.display.set_caption("Mappy Remake")
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
white = (255,255,255)


def launch():
    running = True
    gameStart = False
    start_button = pygame.Rect(325, 400, 150, 60)
    while running:
        screen.fill((30, 30, 30))  # Clear screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    gameStart = True
                    
        if(gameStart):
            startGame()
        else:
            start_screen(start_button)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()



def start_screen(rectangle):
    # Text
    text = font.render("Mappy", True, white)
    text_rect = text.get_rect(center=(400, 80))
    screen.blit(text, text_rect)

    # Leaderboard

    # Game Button
    pygame.draw.rect(screen, (0,255,0), rectangle, border_radius=8)
    text_surf = font.render("Start", True, white)
    text_rect = text_surf.get_rect(center=rectangle.center)
    screen.blit(text_surf, text_rect)
    return

def startGame():
    player1 = Player(700, 0, xScreen, RAIL_Y_POSITIONS, TRAMPOLINE_X_POSITIONS)
    enemy1 = Enemy(700, 0, xScreen, RAIL_Y_POSITIONS, TRAMPOLINE_X_POSITIONS)
    running = True

    while running:
        screen.fill((0, 0, 0))  # Clear screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        draw_rails(screen)
        player1.update()
        player1.draw(screen)
        
        enemy1.update(player1)
        enemy1.draw(screen)

        pygame.display.flip()
        clock.tick(60)

def draw_rails(surface):
    lineColor = (100, 100, 100)
    trampolineColor = (140, 45, 20)
    for i, y in enumerate(RAIL_Y_POSITIONS):
        if i == 0:
            # Draw trampolines at specified x positions
            for x in TRAMPOLINE_X_POSITIONS:
                pygame.draw.line(surface, trampolineColor, (x, y), (x + 50, y), 4)

        # Draw the rest of the rail line
        pygame.draw.line(surface, lineColor, (50, y), (xScreen/2 - 25, y), 4)
        pygame.draw.line(surface, lineColor, (xScreen/2 + 25, y), (xScreen - 50, y), 4)



launch()