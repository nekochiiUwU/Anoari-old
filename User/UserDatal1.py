import pygame
# Slots de save:

"""
Liste d'infos dans les saves:

    1:
    2:
    3:
    4:
    5:
    6:
    7:
    8:
    9:
    10:
    ...

"""


class UserData:

    def __init__(self):
        self.UserGraphicInfo = pygame.display.Info()
        self.DataX = self.UserGraphicInfo.current_w
        self.DataY = self.UserGraphicInfo.current_h
        self.DataResolution = (self.DataX, self.DataY)
        print(self.UserGraphicInfo)


class SaveSlot:

    def __init__(self):
        self.Save1 = [

            # Info -tremisabdoul [0-2]
            "Save 1",  # NameSave
            "Name",  # NamePlayer
            "Rogue", # TypeGame


            # Player
            # Statistiques Player -tremisabdoul [3-9]
            50,  # Game.Player.Pv
            100, #"Game.Player.MaxPv
            10,  #"Game.Player.Damage
            3,  # Game.Player.Speed
            0,  # Game.Player.SpeedY
            0,  # Game.Player.Level
            0,  # Game.Player.Gold

            # Position de Player -tremisabdoul [10-14]
            (50, 50 , 75, 120),  # Game.Player.rect
            0,  # Game.Player.LastY
            0,  # Game.Player.YVector
            None,  # Game.Player.Weapon1
            None,  # Game.Player.Weapon2


            # Force
            # Mouvement Actuel de Player -tremisabdoul [15-17]
            0,  # Game.Force.lastx
            0,  # Game.Force.Base_Gravity
            0  # Game.Force.x


            ]
        self.Save2 = {}
        self.Save3 = {}
        self.Save4 = {}
        self.Save5 = {}
        self.Save6 = {}
        self.Save7 = {}
        self.Save8 = {}
        self.Save9 = {}
