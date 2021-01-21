
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
    Game.Player.SpeedY += 5


def DeplacementX(Game):

    # Déplacement du joueur (x) (Impossible aux limites de l'écran): Touche q / d et LEFT / RIGHT -tremisabdoul
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.Move_Left()


def Printer(Screen, Game, font, police1, fps):
    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(font, (-400, -800))
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    printfps = police1.render(str(fps), True, (255, 255, 255))
    Screen.blit(printfps, (6, 32))


def OptiGraphic(Screen, police1,Game):
    opti = Game.Player.Pv
    opti1 = "..."
    opti = police1.render(str(opti), True, (255, 255, 255))
    opti1 = police1.render(str(opti1), True, (255, 255, 255))
    Screen.blit(opti, (15, 44))
    Screen.blit(opti1, (15, 58))
