# -*- coding: utf-8 -*-

# 32 20 41 / 39 20 41
# main: Contient loop

# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Importe les fichier Classes Functions pygame et time -tremisabdoul
from Scripts.Classes import *
from Scripts.Functions import *
import time
import pygame

'''==================================='''

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

# L'écran est stockée dans une variable -tremisabdoul
Screen = Display()

# Definit les éléments visuels en tant que variable -tremisabdoul
font = pygame.image.load("Assets/Visual/UI/BGPAINT.jpg")

Running = True

# Définit les polices -tremisabdoul
police1 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 10)

'''==================================='''

# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Running:

    """ ===== Loop ===== """
    #Loop du Lobby
    if Game.Lobby :
        Lobby(Game, Screen, font, time, police1)
    # Loop de pause [Escape]
    if Game.Pause:
        pause(Game, Screen, font, time, police1)

    # Loop de jeu
    if Game.InGame:
        inGame(Game, time, nbframe, Screen, font, police1, tickchecker)
