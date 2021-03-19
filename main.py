# -*- coding: utf-8 -*-

# 32 20 41 / 39 20 41
# main: Contient loop

# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Importe les fichier Classes Functions pygame et time -tremisabdoul
from Scripts.Functions import *
from Scripts.Classes import *
import time
'''==================================='''

pygame.init()


# Execute les Classes -tremisabdoul
Game = Game()
Game.init_suite()

# Valeurs qui vont servir plus tard
# (faites gaffe les valeurs peuvent faire crash le jeu si vous en supprimez certeines) -tremisabdoul
x = 0
frame = 0
nbframe = 0

# L'écran est stockée dans une variable -tremisabdoul
Screen = Display()

# Définit les polices -tremisabdoul
police1 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 10)

police2 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 20)

Paterns(Game)
eval('print("Game.Paterns = [", str(Game.Paterns), "]")')
for item in range(len(Game.Paterns)):
    Game.Paterns[item] = Game.Paterns[item].split(":")
    print("\nID", item, ": ", Game.Paterns[item])
    for underitem in Game.Paterns[item]:
        print("\tID", id(underitem), ": ", underitem)
'''==================================='''

# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Game.Running:
    """ ===== Loop ===== """
    # Loop du Lobby
    if Game.Lobby:
        Lobby(Game, Screen, time, police1)
    # Loop de pause [Escape]
    if Game.Pause:
        pause(Game, Screen, time, police1)

    # Loop de jeu
    if Game.InGame:
        inGame(Game, time, Screen, police1)

    if Game.Option:
        Option(Game, Screen, time, police1, police2)
