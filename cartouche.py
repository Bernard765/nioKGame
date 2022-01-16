import pygame
import math


# Class PluieDeCartouche
class PluieDeCartouche:

    # Chargement
    def __init__(self):
        self.pourcentage = 0

    def ajout_pourcentage(self):
        self.pourcentage += 1

    def update_barre_cartouche(self, surface):
        pygame.draw.rect(surface, (73, 73, 73), [0, surface.get_height() - 20, surface.get_width(), 12])
        pygame.draw.rect(surface, (253, 216, 53), [0, surface.get_height() -20 , math.ceil(math.ceil(surface.get_width() / 100) * self.pourcentage), 12])