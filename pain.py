import pygame


# Class Pain
class Pain(pygame.sprite.Sprite):

    # Constructeur
    def __init__(self, joueur):
        super().__init__()
        self.velocity = 3
        self.joueur = joueur
        self.image = pygame.image.load('assets/pain.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 90
        self.rect.y = joueur.rect.y + 30
        self.origin_image = self.image
        self.angle = 0

    def rotation(self):
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def supprimer(self):
        self.joueur.all_pain.remove(self)

    def mouvementDroit(self):
        self.rect.x += self.velocity
        self.rotation()

        for chasseur in self.joueur.jeu.check_collision(self, self.joueur.jeu.all_chasseur):
            self.supprimer()
            chasseur.degat(self.joueur.attack)

    # def mouvementGauche(self):
    #     self.rect.x -= self.velocity
    #     self.rotation()

        # Sortie de pain
        if self.rect.x > 1080 or self.rect.x < 0:
            self.supprimer()
            # print("Debug #2 - Pain supprimé")