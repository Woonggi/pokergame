import pygame

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
running = True;

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

print('hello')