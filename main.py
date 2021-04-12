# -*- coding: utf-8 -*-

# 32 20 41 / 39 20 41
# main: Contient loop

# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Import -tremisabdoul
from Scripts.Functions import *
from Scripts.Classes import *

'''==================================='''

# Init -tremisabdoul
pygame.init()
Game = Game()
Music_Init()
Screen = Display()
Paterns(Game, NewWall, NewPlatform)
musicDANOARKIOUT(Game)

'''==================================='''

for item in pygame.colordict.THECOLORS.items():
    print(item)

# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Game.Running:
    """ ===== Loop ===== """
    # Loop du Lobby
    if Game.Lobby:
        Lobby(Game, Screen)

    # Loop de pause [Escape]
    if Game.Pause:
        pause(Game, Screen)

    # Loop de jeu
    if Game.InGame:
        musicDANOARKI(Game)
        inGame(Game, Screen)
        musicDANOARKIOUT(Game)

    if Game.Option:
        Option(Game, Screen)

    if Game.SaveMenu:
        SaveMenu(Game, Screen)
