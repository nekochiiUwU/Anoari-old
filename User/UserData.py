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
        self.Save1 = {
            "NameSave": "Save 1",
            "NamePlayer": "Name",
            "TypeGame": "Rogue",

            # Player
            # Statistiques Player -tremisabdoul
            "Game.Player.Pv": 50,
            "Game.Player.MaxPv": 100,
            "Game.Player.Damage": 10,
            "Game.Player.Speed": 3,
            "Game.Player.SpeedY": 0,
            "Game.Player.Level": 0,
            "Game.Player.Gold": 0,
            # Position de Player -tremisabdoul
            "Game.Player.rect": (50, 50),
            "Game.Player.LastY": 0,
            "Game.Player.YVector": 0,
            "Game.Player.Weapon1": None,
            "Game.Player.Weapon2": None,

            # Force
            # Mouvement Actuel de Player -tremisabdoul
            "Game.Force.lastx": 0,
            "Game.Force.Base_Gravity": 0,
            "Game.Force.x": 0


            }
        self.Save2 = {}
        self.Save3 = {}
        self.Save4 = {}
        self.Save5 = {}
        self.Save6 = {}
        self.Save7 = {}
        self.Save8 = {}
        self.Save9 = {}
