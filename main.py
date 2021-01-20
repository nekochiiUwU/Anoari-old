# -*- coding: utf-8 -*-

# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Importe le fichier Classes Functions et time -tremisabdoul
from Scripts.Classes import *
from Scripts.Functions import *
import time
import pygame

# Execute les Classes -tremisabdoul
Game = Game()

x = 1

# Valeurs qui vont servir plus tard
# (faites gaffe les valeurs peuvent faire crash le jeu si vous en supprimez certeines) -tremisabdoul
frame = 0
nbframe = 0
fps = 0
event = 0
printpause = 0
printunpause = 0

Pause = False

# L'écran est stockée dans une variable -tremisabdoul
Screen = Display()

# Definit les éléments visuels en tant que variable -tremisabdoul
font = pygame.image.load("Assets/Visual/background_cave.png")

Running = True


# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Running:

    # Définit les polices
    police1 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 10)

    # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
    tick = time.time()
    nbframe += 1
    if nbframe % 10 == 0:
        nbframe10 = True
    else:
        nbframe10 = False

    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(font, (-400, -800))
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    printfps = police1.render(str(fps), 1, (255, 255, 255))
    Screen.blit(printfps, (6, 32))

    # Check les input et instances -tremisabdoul
    for event in pygame.event.get():
        InputConfig(Game, event)

    # Fonction de Jump
    if Game.Player.SpeedY:
        Jump(Game)

    # Fonction de déplacement gauche / droite
    DeplacementX(Game)

    # Opération éfféctuée toutes les 10 frames -tremisabdoul
    if not nbframe10 == 0:
        # Animation de respiration (sorcière) -tremisabdoul
        resp_sorciere(Game)

    # Debug des fps -tremisabdoul
    printfps = police1.render(str(fps), 1, (255, 255, 255))


    # Déplacement de player -tremisabdoul
    Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Player.rect.y += Game.Player.Force.Gravity(Game)

    # Met a jour l'affichage (rafraîchissement de l'écran) -tremisabdoul
    pygame.display.flip()

    # Permet d'avoir des frames régulières -tremisabdoul
    tickcheck = time.time()
    tickchecker = tick - tickcheck

    while tickchecker < 0.017:
        tickcheck = time.time()
        tickchecker = tickcheck - tick
    if not nbframe10 == 0:
        if frame < 10:
            timeframe = + tickchecker
            frame = + 1
            fps = frame / tickchecker
            fps = "FPS : " + str(round(fps))

        else:
            timeframe = tickchecker
            frame = 1
            fps = frame / tickchecker
            fps = "FPS : " + str(round(fps))
