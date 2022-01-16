import pygame
from joueur import Joueur
from chasseur import Chasseur
from son import GestionSon


# Class Jeu
class Jeu:

    # Constructeur
    def __init__(self):
        self.jouer = False

        # Charger Joueur
        self.all_joueur = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.all_joueur.add(self.joueur)

        # Charger Chasseur
        self.all_chasseur = pygame.sprite.Group()

        # Son
        self.gestionson = GestionSon()

        # Score & Meilleur score
        self.score = 0
        self.meilleur_score = 0

        # Touche
        self.pressed = {}

    def debut(self):
        self.jouer = True
        self.spawn_chasseur()

    def fin_jeu(self):
        self.all_chasseur = pygame.sprite.Group()
        self.joueur.health = self.joueur.max_health
        self.jouer = False
        self.gestionson.play('mort')
        if self.meilleur_score < self.score:
            self.meilleur_score = self.score
        self.score = 0

    def ajout_score(self, points=1):
        self.score += points

    def update(self, window):
        # Application du score & Meilleur score
        police = pygame.font.SysFont("permanent marker", 16)
        score_text = police.render(f"Votre score : {self.score}", True, (0, 0, 0))
        meilleur_score_text = police.render(f"Meilleur score : {self.meilleur_score}", True, (0, 0, 0))
        window.blit(score_text, (20, 20))
        window.blit(meilleur_score_text, (20, 40))

        # Application du joueur
        window.blit(self.joueur.image, self.joueur.rect)

        # Vie du joueur
        self.joueur.update_barre_vie(window)

        # Application de pain
        self.joueur.all_pain.draw(window)

        # Application de chasseur
        self.all_chasseur.draw(window)

        # Recuperer les pains
        for pain in self.joueur.all_pain:
            pain.mouvementDroit()

        # Recuperer les chasseurs
        for chasseur in self.all_chasseur:
            chasseur.avancer()
            chasseur.update_barre_vie(window)

        # Deplacement Gauche - Droite
        if self.pressed.get(pygame.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < window.get_width():
            self.joueur.move_right()
            # jeu.joueur.image = pygame.image.load('assets/duck/canardDroite.png')
            # directionPain = "pain.mouvementDroit()"
        elif self.pressed.get(pygame.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()
            # jeu.joueur.image = pygame.image.load('assets/duck/canardGauche.png')
            # directionPain = "pain.mouvementGauche()"

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_chasseur(self):
        chasseur = Chasseur(self)
        self.all_chasseur.add(chasseur)
