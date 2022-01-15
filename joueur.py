import pygame
from pain import Pain


# Class Joueur
class Joueur(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_pain = pygame.sprite.Group()
        self.image = pygame.image.load('assets/duck/canardDroite.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 439

    def degat(self, montant):
        if self.health - montant > montant:
            self.health -= montant
        else:
            self.jeu.fin_jeu()

    def update_barre_vie(self, surface):
        pygame.draw.rect(surface, (73, 73, 73), [self.rect.x + 18, self.rect.y - 5, self.max_health, 8])
        pygame.draw.rect(surface, (0, 255, 201), [self.rect.x + 18, self.rect.y - 5, self.health, 8])

    def launch_pain(self):
        # Instance de la class Pain
        pain = Pain(self)
        self.all_pain.add(pain)

    def move_right(self):
        if not self.jeu.check_collision(self, self.jeu.all_chasseur):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity
