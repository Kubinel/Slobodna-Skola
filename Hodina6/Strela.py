import pygame

class Strela():
    def __init__(self, x, y):
        self.strela = pygame.Rect(x, y, 10, 20)
    
    def vykresli(self, screen):
        pygame.draw.rect(screen, "green", self.ship)
    
    def pohyb(self):
        self.strela.y -= 8
        
