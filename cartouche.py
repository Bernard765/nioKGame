import pygame
import random


# Class Cartouche
class Cartouche(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self, cartoucheEvent):
        super().__init__()
        self.image = pygame.image.load('assets/balle.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(10, 900)
        self.rect.y = - random.randint(0, 200)
        self.cartoucheEvent = cartoucheEvent

    def supprimer(self):
        self.cartoucheEvent.all_cartouche.remove(self)
        if len(self.cartoucheEvent.all_cartouche) == 0:
            self.cartoucheEvent.reset_pourcentage()
            self.cartoucheEvent.tomber = False
            self.cartoucheEvent.jeu.spawn_chasseur()
            self.cartoucheEvent.jeu.spawn_chasseur()
            self.cartoucheEvent.jeu.ajout_score(3)

    def tombe(self):
        self.rect.y += self.velocity
        if self.rect.y >= 400:
            self.supprimer()

        if self.cartoucheEvent.jeu.check_collision(self, self.cartoucheEvent.jeu.all_joueur):
            self.supprimer()
            self.cartoucheEvent.jeu.joueur.degat(20)
