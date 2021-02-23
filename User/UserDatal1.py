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
            ]
        self.Save2 = {}
        self.Save3 = {}
        self.Save4 = {}
        self.Save5 = {}
        self.Save6 = {}
        self.Save7 = {}
        self.Save8 = {}
        self.Save9 = {}
