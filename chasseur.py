import pygame
import random


# Class Chasseur
class Chasseur(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 60
        self.max_health = 60
        self.attack = 0.2
        self.image = pygame.image.load('assets/chasseur.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 200)
        self.rect.y = 410
        self.velocity = 1

    def degat(self, montant):
        self.health -= montant

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 200)
            self.health = 80
            self.jeu.gestionson.play('chasseur')
            self.jeu.ajout_score()

    def update_barre_vie(self, surface):
        pygame.draw.rect(surface, (73, 73, 73), [self.rect.x + 18, self.rect.y - 10, self.max_health, 8])
        pygame.draw.rect(surface, (0, 255, 201), [self.rect.x + 18, self.rect.y - 10, self.health, 8])

    def avancer(self):
        if not self.jeu.check_collision(self, self.jeu.all_joueur):
            self.rect.x -= self.velocity
        else:
            self.jeu.joueur.degat(self.attack)
