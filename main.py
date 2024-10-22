# -*- coding: utf-8 -*-

from Scripts.Functions import *
from Scripts.Classes import *
from Data.Weapons import *

'''==================================='''

pygame.init()
Game = Game()
ImportOptions(Game)
Music_Init(Game)
Screen = Display()
Paterns(Game)
musicDANOARKIOUT(Game)
Game.DataWeapon = DataWeapons(Game)
Game.DataWeapon.New(Game, Game.Player.Weapon1)


'''==================================='''

#for item in pygame.colordict.THECOLORS.items():
    #print(item)

while Game.Running:

    """ ===== Loop ===== """

    if Game.Lobby:
        Lobby(Game, Screen)

    if Game.Pause:
        Pause(Game, Screen)

    if Game.InGame:
        musicDANOARKI(Game)
        inGame(Game, Screen)
        musicDANOARKIOUT(Game)

    if Game.Option:
        Option(Game, Screen)

    if Game.SaveMenu:
        SaveMenu(Game, Screen)
