import pygame
import sys
from game import Game

pygame.init()

xScreen = 800
yScreen = 600
RAIL_Y_POSITIONS = [550, 450, 350, 250, 150]
TRAMPOLINE_X_POSITIONS = [0, xScreen/2-25, xScreen-50]
HIGHSCORE = 0

screen = pygame.display.set_mode((xScreen, yScreen))
pygame.display.set_caption("Mappy Remake")
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
white = (255,255,255)


def launch():
    running = True
    gameStart = False
    start_button = pygame.Rect(325, 400, 150, 60)
    game = Game(xScreen, RAIL_Y_POSITIONS, TRAMPOLINE_X_POSITIONS)
    while running:
        screen.fill((30, 30, 30))  # Clear screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                   game.startGame()
                    
        if(game.gameOn()):
            currScore = game.update(screen)
            global HIGHSCORE
            HIGHSCORE = max(currScore, HIGHSCORE)
            game.draw(screen)
            game.printScore(screen, font)
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
    text2 = f"Highscore: {HIGHSCORE}"
    text_surface = font.render(text2, True, white)
    text_rect2 = text_surface.get_rect(center=(400,200))
    screen.blit(text_surface, text_rect2)

    # Game Button
    pygame.draw.rect(screen, (0,255,0), rectangle, border_radius=8)
    text_surf = font.render("Start", True, white)
    text_rect = text_surf.get_rect(center=rectangle.center)
    screen.blit(text_surf, text_rect)
    return



launch()