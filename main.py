# -*- coding: utf-8 -*-

# import pygame
from Scripts.Classes import *

# Execute les Classes
Game = Game()


# Execute les Classes
def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    screen = pygame.display.set_mode((640, 480))
    return screen


# L'écran est stockée dans une variable
Screen = Display()

# Definit les éléments visuels en tant que variable
font = pygame.image.load("Assets/Visual/background_cave.png")
ground = pygame.image.load("Assets/Visual/ground.jpg")


Running = True

# Contient tout ce qui est fait pent que le jeu est run
while Running:

    # Affiche a l'écran des éléments
    Screen.blit(font, (-1000, -1000))
    Screen.blit(ground, (0, 400))
    Screen.blit(Game.Player.image, Game.Player.rect)

    # Debug des input clavier
    print(Game.pressed)

    # Déplacement du joueur (x)
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:

        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:

        Game.Player.Move_Left()

    # Met a jour l'affichage
    pygame.display.flip()

    # Check les input et instances
    for event in pygame.event.get():

        # Bouton croix en haut a droite (Fermer le Programme)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Touches enfoncées
        elif event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

        # Touches relachées
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False
