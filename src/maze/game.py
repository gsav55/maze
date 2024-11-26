import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# 1280/100 = 12.8
# 729/100 = 7.2
# 12 x 7 grid of 100x100 boxes to make map
#
grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,0,1,0,0,1],
    [1,0,0,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1],
]

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(2,1)

for row in grid:
    for 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked the X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with a color to clear last frame
    screen.fill("purple")

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
