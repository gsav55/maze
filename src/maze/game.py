import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

WALL = 0x000000
FLOOR = 0xFFFFFF
GOAL = 0xFF55FF
START = 0x55FFFF


assets = (Path(__file__).parent.parent / "assets").resolve()
mazebg = pygame.image.load((assets / "maze-01").resolve()).convert()


# 1280/40 = 32
# 720/40 = 18
# 32 x 18 grid of 40x40 boxes to make map

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(20, 20)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked the X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w:
                    player_pos.y -= 40
                case pygame.K_UP:
                    player_pos.y -= 40
                case pygame.K_s:
                    player_pos.y += 40
                case pygame.K_DOWN:
                    player_pos.y += 40
                case pygame.K_a:
                    player_pos.x -= 40
                case pygame.K_LEFT:
                    player_pos.x -= 40
                case pygame.K_d:
                    player_pos.x += 40
                case pygame.K_RIGHT:
                    player_pos.x += 40

    # Fill screen with a color to clear last frame
    screen.blit(mazebg, (0, 0))

    # Render game here!
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt

    if keys[pygame.K_s]:
        player_pos.y += 300 * dt

    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt

    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Flip() display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limit to 60 fps

pygame.quit()
