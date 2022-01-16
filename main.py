import pygame
import math
import webbrowser
from pain import Pain
from joueur import Joueur
from jeu import Jeu

pygame.init()
jeu = Jeu()
joueur = Joueur(jeu)
pain = Pain(joueur)

# TODO * Ajouter un boutton pour allumer/atteindre la musique, pareil pour les bruitages
# TODO * Ajouter des difficultés

# Logo
logo = pygame.image.load('assets/logo.png')
logo = pygame.transform.scale(logo, (500, 500))

# Generation de fenetre
pygame.display.set_caption("nioK Game | Par Sacha")
pygame.display.set_icon(logo)
window = pygame.display.set_mode((1080, 720))

# Musique
temps_musique = 253
while temps_musique > 0:
    temps_musique -= 1
else:
    jeu.gestionson.play('musique')
    temps_musique = 253


# Background
background = pygame.image.load('assets/bgthird.png')

# Transformation logo
logo_rect = logo.get_rect()
logo_rect.x = math.ceil(window.get_width() / 4)
logo_rect.y = 20

# Bouton debut
bouton_debut = pygame.image.load('assets/play.png')
bouton_debut = pygame.transform.scale(bouton_debut, (100, 100))
bouton_debut_rect = bouton_debut.get_rect()
bouton_debut_rect.x = math.ceil(window.get_width() / 2.3)
bouton_debut_rect.y = math.ceil(window.get_height() / 1.75)

# Bouton GitHub
github = pygame.image.load('assets/github.png')
github = pygame.transform.scale(github, (100, 100))
github_rect = bouton_debut.get_rect()
github_rect.x = math.ceil(window.get_width() / 4)
github_rect.y = math.ceil(window.get_height() / 1.3)

# Run
running = True

# Boucle de jeu
while running:

    # Application de l'arriere plan
    window.blit(background, (0, 0))

    # Si Jeu is_playing
    if jeu.jouer:
        jeu.update(window)
    else:
        window.blit(logo, logo_rect)
        window.blit(bouton_debut, bouton_debut_rect)
        window.blit(github, github_rect)

    # Refresh
    pygame.display.flip()

    for event in pygame.event.get():
        # Fenetre fermée
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Touche pressée
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            # Touche espace (Pain)
            if event.key == pygame.K_SPACE:
                jeu.joueur.launch_pain()

        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_debut_rect.collidepoint(event.pos):
                if not jeu.jouer:
                    jeu.debut()
                    jeu.gestionson.play('debut')
            elif github_rect.collidepoint(event.pos):
                if not jeu.jouer:
                    webbrowser.open('https://github.com/SachaTheDuck/nioKGame', new=2)
