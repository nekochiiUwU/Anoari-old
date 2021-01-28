
# Contient toutes les fonctions non-dépendentes d'une classe
# (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame


# Crée l'écran -tremisabdoul
def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    return screen


def resp_sorciere(time, Game, AnimationSorcer):

    while AnimationSorcer:

        if not Game.Player.Force.x:
            time.sleep(0.5)
            return 0

        else:
            time.sleep(0.5)
            return 0


def Jump(Game):
    if Game.Player.SpeedY < 0:
        Game.Player.rect.y += Game.Player.SpeedY
        Game.Player.SpeedY += 0.66
    else:
        Game.Player.SpeedY = 0


def DeplacementX(Game):

    # Déplacement du joueur (x) (Impossible aux limites de l'écran): Touche q / d et LEFT / RIGHT -tremisabdoul
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.Move_Left()


def Printer(Screen, Game, font):
    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(font, (0, 0))
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    Screen.blit(Game.Mouse.image, pygame.mouse.get_pos())
    Game.Plateform.NewPlateform(Screen, 200, 700, 500)


def UIPrinter(Screen, police1, Game, tickchecker):

    # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
    frame = 1
    fps = frame / tickchecker
    fps = "FPS : " + str(round(fps))

    # Transforme une variable en composent graphique -tremisabdoul
    printfps = police1.render(str(fps), True, (255, 255, 255))

    Screen.blit(printfps, (6, 34))

    Color = (Game.Player.Pv / Game.Player.MaxPv) * 255
    LifeColor = [255, Color, Color]

    opti = str(round(Game.Player.Pv))
    opti = str(str(opti) + " / " + str(Game.Player.MaxPv) + " PV")
    opti = police1.render(str(opti), True, LifeColor)

    opti1 = round((Game.Player.Pv / Game.Player.MaxPv) * 100)
    opti1 = opti1 * "♫"
    opti1 = police1.render(str(opti1), True, LifeColor)

    Screen.blit(opti, (15 + Color / 50, 48 + Color / 50))
    Screen.blit(opti1, (15 + Color / 50, 60 + Color / 50))


# map.maskimage.map_rgb(127, 127, 127, 255)

def pause(Game, Screen, font, time, police1):

    while 0 == 0:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_ESCAPE):
                    time.sleep(0.1)
                    return False

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        pauseblit(Screen, font, Game)

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


def pauseblit(Screen, font, Game):

    Screen.blit(font, (0, 0))
    Screen.blit(Game.UI.baselayer, (0, 0))
    Screen.blit(Game.UI.playbuttun, Game.UI.playbuttunrect)
    Screen.blit(Game.UI.quitbuttun, Game.UI.quitbuttunrect)
    Screen.blit(Game.UI.resumebuttun, Game.UI.resumebuttunrect)
    Screen.blit(Game.UI.savebuttun, Game.UI.savebuttunrect)
    Screen.blit(Game.Mouse.image, pygame.mouse.get_pos())
