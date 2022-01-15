import pygame


# Class GestionSon
class GestionSon:

    # Constructeur
    def __init__(self):
        self.sons = {
            'debut': pygame.mixer.Sound('assets/sons/click.ogg'),
            'musique': pygame.mixer.Sound('assets/sons/musique.mp3'),
            'mort': pygame.mixer.Sound('assets/sons/trompette.mp3'),
            'chasseur': pygame.mixer.Sound('assets/sons/blaster.ogg'),
        }

    def play(self, nom):
        self.sons[nom].play()