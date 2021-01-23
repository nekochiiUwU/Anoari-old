# -*- coding: utf-8 -*-
# 32 20 41 / 39 20 41
# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Importe les fichier Classes Functions pygame et time -tremisabdoul
from Scripts.Classes import *
from Scripts.Functions import *
import time
import pygame

pygame.init()

# Execute les Classes -tremisabdoul
Game = Game()


# Valeurs qui vont servir plus tard
# (faites gaffe les valeurs peuvent faire crash le jeu si vous en supprimez certeines) -tremisabdoul
x = 0
frame = 0
nbframe = 0
fps = 0
event = 0
printpause = 0
printunpause = 0
tickchecker = 1
Pause = False

# L'écran est stockée dans une variable -tremisabdoul
Screen = Display()

# Definit les éléments visuels en tant que variable -tremisabdoul
font = pygame.image.load("Assets/Visual/UI/RambardePAINT.png")
font = pygame.transform.scale(font, (1500, 720))

Running = True

# Définit les polices -tremisabdoul
police1 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 10)

# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Running:
    print(Game.Player.image, "\n", Game.Player.rect)
    if Game.Player.Pv < 2:
        Game.Player.Pv = Game.Player.MaxPv
    else:
        Game.Player.Pv -= 1

    # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
    tick = time.time()

    nbframe += 1

    Printer(Screen, Game, font)
    OptiGraphic(Screen, police1, Game, tickchecker)

    # Check les input et instances -tremisabdoul
    for event in pygame.event.get():
        # Touches enfoncées -tremisabdoul
        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

        # Touches relachées -tremisabdoul
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Active le Jump() -tremisabdoul
        if Game.pressed.get(pygame.K_SPACE) \
                and Game.Player.check_collisions(Game.Player, Game.all_platform):
            Game.Player.SpeedY = -24

        # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Touche Echap (Fermer le Programme) -tremisabdoul
        if Game.pressed.get(pygame.K_ESCAPE):
            running = False
            pygame.quit()

        if Game.pressed.get(pygame.K_p):
            Pause = True
            Running = False

    # Fonction de Jump -tremisabdoul
    if Game.Player.SpeedY:
        Jump(Game)

    # Fonction de déplacement gauche / droite -tremisabdoul
    DeplacementX(Game)

    # Déplacements de player -tremisabdoul
    Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Player.rect.y += Game.Player.Force.Gravity(Game)

    # Met a jour l'affichage (rafraîchissement de l'écran) -tremisabdoul
    pygame.display.flip()

    # Permet d'avoir des frames régulières -tremisabdoul
    tickchecker = time.time()
    tickchecker -= tick

    while tickchecker < 0.017:
        tickchecker = time.time()
        tickchecker -= tick
