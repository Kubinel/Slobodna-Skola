import pygame
from random import randint

SIRKA = 600
VYSKA = 400

def restart(z, score, hrac):
    z -= 1
    if z <= 0:
        score = 0
        hrac = pygame.Rect(100, 100, 50, 50)
    minca.x = randint(0,SIRKA-30)
    minca.y = randint(0,VYSKA-30)
    nepriatel = pygame.Rect(
        randint(50, SIRKA - 50),
        randint(50, VYSKA - 50),
        50,
        50
    )
    
    return z, score, hrac, nepriatel

pygame.init()
screen = pygame.display.set_mode((SIRKA, VYSKA))
clock = pygame.time.Clock()

nepriatel = pygame.Rect(
    randint(50, SIRKA - 50),
    randint(50, VYSKA - 50),
    50,
    50
    )
hrac = pygame.Rect(100, 100, 50, 50)
minca = pygame.Rect(300, 200, 30, 30)

running = True

font = pygame.font.SysFont("arial", 30)
font2 = pygame.font.SysFont("arial", 30)

score = 0
zivoty = 3
rychlost_nepriatela = 3

while running:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_r]:
        score, hrac, nepriatel = restart(zivoty)

    if keys[pygame.K_RIGHT]:
        hrac.x += 5
        if hrac.x > SIRKA:
            hrac.x = 0
    if keys[pygame.K_LEFT]:
        hrac.x -= 5
        if hrac.x < 0:
            hrac.x = SIRKA
    if keys[pygame.K_UP]:
        hrac.y -= 5
        if hrac.y < 0:
            hrac.y = VYSKA
    if keys[pygame.K_DOWN]:
        hrac.y += 5
        if hrac.y > VYSKA:
            hrac.y = 0

    if hrac.colliderect(minca):
        score += 1
        minca.x = randint(0,SIRKA-30)
        minca.y = randint(0,VYSKA-30)
        
    if hrac.colliderect(nepriatel):
        zivoty, score, hrac, nepriatel = restart(zivoty, score, hrac)
        
    nepriatel.x += rychlost_nepriatela
    
    if nepriatel.x > SIRKA - 100:
        rychlost_nepriatela = -3
    if nepriatel.x < 50:
        rychlost_nepriatela = 3

    screen.fill("green")
    pygame.draw.rect(screen, "grey", nepriatel)
    pygame.draw.ellipse(screen, "yellow", minca)
    pygame.draw.rect(screen, "red", hrac)
    text = font.render("Skore: " + str(score), True, "white")
    text2 = font.render("Zivoty: " + str(zivoty), True, "white")
    screen.blit(text, (10,10))
    screen.blit(text2, (10,40))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
