
# Contient toutes les fonctions non-dépendentes d'une classe
# (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame


# Crée l'écran -tremisabdoul
def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    return screen


def resp_sorciere(Game):

    if not Game.Player.Force.x:
        return 0


def Jump(Game):
    Game.Player.rect.y += Game.Player.SpeedY
    Game.Player.SpeedY += 1.5


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
    Screen.blit(font, (0, 0))
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    printfps = police1.render(str(fps), True, (255, 255, 255))
    Screen.blit(printfps, (6, 34))


def OptiGraphic(Screen, police1, Game):
    Color = (Game.Player.Pv / Game.Player.MaxPv) * 255
    LifeColor = [255, Color, Color]
    opti = str(round(Game.Player.Pv))
    opti = str(str(opti) + " / " + str(Game.Player.MaxPv) + " PV")
    opti1 = round((Game.Player.Pv / Game.Player.MaxPv) * 100)
    opti1 = opti1 * "☺"
    opti = police1.render(str(opti), True, LifeColor)
    opti1 = police1.render(str(opti1), True, LifeColor)
    Screen.blit(opti, (15, 48))
    Screen.blit(opti1, (15, 60))

# map.maskimage.map_rgb(127, 127, 127, 255)
