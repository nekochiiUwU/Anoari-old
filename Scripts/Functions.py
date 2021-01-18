
# Contient toutes les fonctions non-dépendentes d'une classe
# (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame


# Crée l'écran -tremisabdoul
def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    screen = pygame.display.set_mode((1280, 780), pygame.FULLSCREEN)
    return screen


def resp_sorciere(Game):

    if not Game.Player.Force.x:

        if Game.Player.Actual_image == 1:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
            Game.Player.Actual_image = 2
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 2:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame3.png")
            Game.Player.Actual_image = 3
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 3:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame4.png")
            Game.Player.Actual_image = 4
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 4:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame5.png")
            Game.Player.Actual_image = 5
            Game.Player.rect.y -= 1

        elif Game.Player.Actual_image == 5:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame6.png")
            Game.Player.Actual_image = 6
            Game.Player.rect.y -= 1

        elif Game.Player.Actual_image == 6:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame1.png")
            Game.Player.Actual_image = 1
            Game.Player.rect.y -= 1


def Jump(Game):
    Game.Player.rect.y += Game.Player.SpeedY
    Game.Player.SpeedY += 10