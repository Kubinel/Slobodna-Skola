import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

hrac = pygame.Rect(100, 100, 50, 50)
minca = pygame.Rect(300, 200, 30, 30)

running = True

font = pygame.font.SysFont("arial", 30)

score = 0

while running:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        hrac.x += 5
    if keys[pygame.K_LEFT]:
        hrac.x -= 5
    if keys[pygame.K_UP]:
        hrac.y -= 5
    if keys[pygame.K_DOWN]:
        hrac.y += 5

    if hrac.colliderect(minca):
        score += 1
        minca.x = randint(0,570)
        minca.y = randint(0,370)

    screen.fill("green")
    pygame.draw.ellipse(screen, "yellow", minca)
    pygame.draw.rect(screen, "red", hrac)
    text = font.render("Skore: " + str(score), True, "white")
    screen.blit(text, (10,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
