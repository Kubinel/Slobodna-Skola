import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))

x = 100
y = 100

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x = x + 5
    if keys[pygame.K_LEFT]:
        x = x - 5
    if keys[pygame.K_UP]:
        y = y - 5
    if keys[pygame.K_DOWN]:
        y = y + 5

    screen.fill("green")
    pygame.draw.rect(screen, "red", (x,y,50,50))
    pygame.display.flip()

pygame.quit()
