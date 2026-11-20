import Hrac
import Strela
import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

hrac = Hrac.Hrac(275, 325)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    
    keys = pygame.key.get_pressed()
    hrac.pohyb(keys)
    
    hrac.vykresli(screen)
    pygame.display.flip()
    clock.tick(60)
    
