import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (350, 250), 50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
