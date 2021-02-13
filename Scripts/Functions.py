
# Contient toutes les fonctions (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame


# Crée l'écran -tremisabdoul
def Display():
    """Fonction Permettent l'affichage de l'écran"""

    pygame.init()
    pygame.display.set_caption("Anoari")
    size = width, height = 1280,720
    screen = pygame.display.set_mode((size))
    return screen


# Animation (resp_sorcière) -tremisabdoul
def resp_sorciere(time, Game, AnimationSorcer):
    """Fonction d'animation: resp_mystique"""

    while AnimationSorcer:

        if not Game.Player.Force.x:
            time.sleep(0.5)
            return 0

        else:
            time.sleep(0.5)
            return 0


# Fonction de jump: [ Key: Space ] -tremisabdoul
def Jump(Game):
    """Fonction de jump: [ Key: Space ]"""

    if Game.Player.SpeedY < 0:
        Game.Player.rect.y += Game.Player.SpeedY
        Game.Player.SpeedY += 0.66
    else:
        Game.Player.SpeedY = 0


# Déplacement du joueur (x) (Impossible aux limites de l'écran): Touche q / d et LEFT / RIGHT -tremisabdoul
def DeplacementX(Game):
    """Fonction de déplacement [gauche/droite] :  [ Left: LEFT / Q ], [ Right: RIGHT / D ]"""

    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.Move_Left()


# Print: -tremisabdoul
def MousePriter(Screen, Game):
    """Fonction d'affichage: Mouse"""

    Game.Mouse.rect.center = pygame.mouse.get_pos()
    Screen.blit(Game.Mouse.image, Game.Mouse.rect)


# Print: -tremisabdoul
def Printer(Screen, Game, font):
    """Fonction d'affichage: Eléments in-game"""

    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(font, (0, 0))
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    Game.Plateform.NewPlateform(Screen, 200, 700, 500)
    MousePriter(Screen, Game)
    Screen.blit(Game.Monster.image, Game.Monster.rect)


# Print: -tremisabdoul
def UIPrinter(Screen, police1, Game, tickchecker):
    """Fonction d'affichage: Eléments d'interface in-game"""

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


# Print: -tremisabdoul
def pauseblit(Screen, font, Game):
    """Fonction d'affichage: Eléments de pause"""

    Screen.blit(font, (0, 0))
    Screen.blit(Game.UI.baselayer, (0, 0))
    Screen.blit(Game.UI.resumebutton, Game.UI.resumebuttonrect)
    Screen.blit(Game.UI.savebutton, Game.UI.savebuttonrect)
    Screen.blit(Game.UI.settingsbutton, Game.UI.settingsbuttonrect)
    Screen.blit(Game.UI.quitbutton, Game.UI.quitbuttonrect)


# Loop de Pause: -tremisabdoul
def pause(Game, Screen, font, time, police1):
    """ Loop de pause """

    while Game.Pause:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()

                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = False
                    Game.InGame = True
                    time.sleep(0.1)

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Game.UI.resumebuttunrect.collidepoint(event.pos):
                    Game.Pause = False
                    Game.InGame = True
                elif Game.UI.quitbuttunrect.collidepoint(event.pos):
                    Game.Pause = False
                    Game.Lobby = True

            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        pauseblit(Screen, font, Game)
        MousePriter(Screen, Game)

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


# Loop de Jeu: -tremisabdoul
def inGame(Game, time, nbframe, Screen, font, police1, tickchecker):
    """ Loop de Jeu """

    while Game.InGame:
        """ Sert a rien ! """
        if Game.Player.Pv < 2:
            Game.Player.Pv = Game.Player.MaxPv
        else:
            Game.Player.Pv -= 1

        """ ===== __init__ Frame Limiter ===== """

        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        nbframe += 1

        """ ===== Key Inputs ===== """

        # Check les input et instances -tremisabdoul
        for event in pygame.event.get():

            # Touches enfoncées -tremisabdoul
            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                #Changement entre Fullscreen / Window -steven
                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()

                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = True
                    Game.InGame = False

            # Touches relachées -tremisabdoul
            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            # Active le Jump() -tremisabdoul
            if Game.pressed.get(pygame.K_SPACE) \
                    and Game.Player.check_collisions(Game.Player, Game.all_platform):
                Game.Player.SpeedY = -24

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.running = False
                pygame.quit()

        """ ===== Movements ===== """

        Game.Player.LastY = Game.Player.rect.y

        # Fonction de Jump -tremisabdoul
        if Game.Player.SpeedY:
            Jump(Game)

        # Fonction de déplacement gauche / droite -tremisabdoul
        DeplacementX(Game)

        # Déplacements de player -tremisabdoul
        Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
        Game.Player.rect.y += Game.Player.Force.Gravity(Game)

        """ ===== Printers ===== """

        # Print les elements In-Game du jeu  -tremisabdoul
        Printer(Screen, Game, font)

        """ ===== Monster Instruction ===== """

        for Monster in Game.all_Monster:
            Monster.Life(Screen)
            if not Game.Player.check_collisions(Game.Player, Game.all_Monster):
                Monster.Move_Left()

        # Print l'interface de jeu -tremisabdoul
        UIPrinter(Screen, police1, Game, tickchecker)

        MousePriter(Screen, Game)

        Game.Player.YVector = Game.Player.LastY - Game.Player.rect.y
        YVector = police1.render("Y Vector checker: " + str(Game.Player.YVector), True, (255, 255, 255))
        Screen.blit(YVector, (100, 34))

        # Met a jour l'affichage (rafraîchissement de l'écran) -tremisabdoul
        pygame.display.flip()

        """ ===== Frame Limiter ===== """

        # Permet d'avoir des frames régulières -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick


def LobbyBlit(Screen, Game):
    """Fonction d'affichage: Eléments du lobby"""
    Screen.blit(Game.UI.lobbybackground, (0, 0))
    Screen.blit(Game.UI.lobby_loadbutton, Game.UI.lobby_loadbuttonrect)
    Screen.blit(Game.UI.lobby_playbutton, Game.UI.lobby_playbuttonrect)
    Screen.blit(Game.UI.lobby_quitbutton, Game.UI.lobby_quitbuttonrect)


def Lobby(Game, Screen, time, police1):

    while Game.Lobby:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Game.UI.lobby_playbuttonrect.collidepoint(event.pos):
                    Game.InGame = True
                    Game.Lobby = False
                elif Game.UI.lobby_quitbuttonrect.collidepoint(event.pos):
                    Game.Running = False
                    pygame.quit()

            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        LobbyBlit(Screen, Game)
        MousePriter(Screen, Game)

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


