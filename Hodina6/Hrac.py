import pygame

class Hrac:
    def __init__(self, x, y):
        self.ship = pygame.Rect(x, y, 50, 50)
        
    def vykresli(self, screen):
        pygame.draw.rect(screen, "blue", self.ship)
        
    def pohyb(self, keys):
        if keys[pygame.K_LEFT]:
            self.ship.x -= 5
        if keys[pygame.K_RIGHT]:
            self.ship.x += 5
