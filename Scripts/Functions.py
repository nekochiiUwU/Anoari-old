
# Contient toutes les fonctions (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame
import os


# Crée l'écran -tremisabdoul
def Display():
    """Fonction Permettent l'affichage de l'écran"""

    pygame.init()
    pygame.display.set_caption("Anoari")
    size = (1280, 720)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen


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

    Game.Player.MovementKey = False
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.MovementKey = True
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.MovementKey = True
        Game.Player.Move_Left()


# Print: -tremisabdoul
def MousePriter(Screen, Game):
    """Fonction d'affichage: Mouse"""

    Game.Mouse.rect.center = pygame.mouse.get_pos()
    Screen.blit(Game.Mouse.image, Game.Mouse.rect)


# Print: -tremisabdoul
def Printer(Screen, Game):
    """Fonction d'affichage: Eléments in-game"""
    Game.Plateform.rect.x -= Game.Position
    Game.Monster.rect.x -= Game.Position
    Game.Background.rect.x -= Game.Position

    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(Game.Background.image, Game.Background.rect)
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Plateform.image, Game.Plateform.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    Screen.blit(Game.Monster.image, Game.Monster.rect)
    MousePriter(Screen, Game)


# Print: -tremisabdoul
def UIPrinter(Screen, police1, Game):
    """Fonction d'affichage: Eléments d'interface in-game"""

    # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
    frame = 1
    fps = frame / Game.Tickchecker
    fps = "FPS : " + str(round(fps))

    # Transforme une variable en composent graphique -tremisabdoul
    printfps = police1.render(str(fps), True, (255, 255, 255))

    Screen.blit(printfps, (6, 34))

    Color = (Game.Player.Pv / Game.Player.MaxPv) * 255
    LifeColor = [255, Color, Color]

    opti = str(round(Game.Player.Pv))
    opti = str(str(opti) + " / " + str(Game.Player.MaxPv) + " PV")
    opti = police1.render(str(opti), True, LifeColor)

    opti1 = round((Game.Player.Pv / Game.Player.MaxPv) * 75)
    opti1 = opti1 * "♫"
    opti1 = police1.render(str(opti1), True, LifeColor)

    Screen.blit(opti, (15 + Color / 50, 48 + Color / 50))
    Screen.blit(opti1, (15 + Color / 50, 60 + Color / 50))


# Print: -tremisabdoul
def pauseblit(Screen, Game):
    """Fonction d'affichage: Eléments de pause"""

    Screen.blit(Game.Background.image, Game.Background.rect)
    # Screen.blit(Game.UI.baselayer, (0, 0))
    Screen.blit(Game.UI.resumebutton, Game.UI.resumebuttonrect)
    Screen.blit(Game.UI.savebutton, Game.UI.savebuttonrect)
    Screen.blit(Game.UI.settingsbutton, Game.UI.settingsbuttonrect)
    Screen.blit(Game.UI.quitbutton, Game.UI.quitbuttonrect)


# Loop de Pause: -tremisabdoul
def pause(Game, Screen, time, police1):
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
                if Game.UI.resumebuttonrect.collidepoint(event.pos):
                    Data_Load(Game)
                    Game.Pause = False
                    Game.InGame = True
                elif Game.UI.savebuttonrect.collidepoint(event.pos):
                    Data_Save(Game)
                elif Game.UI.settingsbuttonrect.collidepoint(event.pos):
                    Game.Pause = False
                    Game.Option = True
                elif Game.UI.quitbuttonrect.collidepoint(event.pos):
                    Game.Pause = False
                    Game.Lobby = True

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.Pause = False
                Game.running = False
                pygame.quit()

        # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
        Game.Tickchecker = time.time()
        Game.Tickchecker -= tick

        pauseblit(Screen, Game)
        MousePriter(Screen, Game)

        while Game.Tickchecker < 0.017:
            Game.Tickchecker = time.time()
            Game.Tickchecker -= tick

        fps = 1 / Game.Tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


# Loop de Jeu: -tremisabdoul
def inGame(Game, time, Screen, police1):
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

        Game.Frame += 1

        """ ===== Key Inputs ===== """

        # Check les input et instances -tremisabdoul
        for event in pygame.event.get():

            # Touches enfoncées -tremisabdoul
            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                # Active le Jump() -tremisabdoul
                if Game.pressed.get(pygame.K_SPACE) \
                        and Game.Player.check_collisions(Game.Player, Game.all_platform):
                    Game.Player.SpeedY = -24

                # Activation de Pause -tremisabdoul
                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = True
                    Game.InGame = False

                # Changement entre Fullscreen / Window -steven
                if Game.pressed.get(pygame.K_F11):
                    print(pygame.display.Info())
                    if Game.Fullscreen == 0:
                        Screen = pygame.display.set_mode((Game.UserData.DataX, Game.UserData.DataY), pygame.FULLSCREEN)
                        Game.Fullscreen = 1
                    else:
                        pygame.display.set_mode((Game.DataX, Game.DataY), pygame.RESIZABLE)
                        pygame.display.toggle_fullscreen()
                        pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 60)
                        Game.Fullscreen = 0

            # Touches relachées -tremisabdoul
            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            #  -tremisabdoul
            if event.type == pygame.VIDEORESIZE:
                ReScale(Game, Screen)

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

        """ ===== Movements ===== """

        Game.Player.LastY = Game.Player.rect.y

        # Fonction de Jump -tremisabdoul
        if Game.Player.SpeedY:
            Jump(Game)

        # Fonction de déplacement gauche / droite -tremisabdoul
        DeplacementX(Game)

        Game.Player.rect.y += Game.Player.Force.Gravity(Game, Game.Player)

        # Déplacements de player -tremisabdoul
        #Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
        Game.Position = round(Game.Player.Force.AccelerationFunctionX())
        Game.PositonPlayer -= Game.Position

        Animation(Game)

        BackgroundScroll(Game)
        """ ===== Printers ===== """

        # Print les elements In-Game du jeu  -tremisabdoul
        Printer(Screen, Game)

        """ ===== Monster Instruction ===== """

        for Monster in Game.all_Monster:
            Monster.Life(Screen, Game)
            if not Game.Player.check_collisions(Game.Player, Game.all_Monster):
                Monster.Move_Left()

        # Print l'interface de jeu -tremisabdoul
        UIPrinter(Screen, police1, Game)

        MousePriter(Screen, Game)

        Game.Player.YVector = Game.Player.LastY - Game.Player.rect.y
        YVector = police1.render("Y Vector checker: " + str(Game.Player.YVector), True, (141, 100, 200))
        Screen.blit(YVector, (100, 34))

        # Met a jour l'affichage (rafraîchissement de l'écran) -tremisabdoul
        pygame.display.flip()

        """ ===== Frame Limiter ===== """

        # Permet d'avoir des frames régulières -tremisabdoul
        Game.Tickchecker = time.time()
        Game.Tickchecker -= tick

        while Game.Tickchecker < 0.017:
            Game.Tickchecker = time.time()
            Game.Tickchecker -= tick


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

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

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


def Option(Game, Screen, time, police1, police2):
    while Game.Option:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = True
                    Game.Option = False

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

        # Permet de récupérer le nombre de frames a la seconde -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        MousePriter(Screen, Game)

        Screen.fill((0, 0, 0))

        # Affichage du nécessaire pour le texte des Options -steven
        White = (255, 255, 255)
        Texte('Résolution : ', police2, White, Screen, 100, 100)
        Texte('Volume : ', police2, White, Screen, 100, 225)
        Texte('Contrôle : ', police2, White, Screen, 100, 350)

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


# Fonction du texte -steven
def Texte(text, police2, color, Screen, x, y):
    Texte_Contenu = police2.render(text, 1, color)
    Texte_Rect = (x, y)
    Screen.blit(Texte_Contenu, Texte_Rect)


# TKT -tremisabdoul
def Data_Save(Game):

    import csv

    Datalist = {
        # Info -tremisabdoul [0-2]
        "# MetaSave": "Infos -tremisabdoul",
        "SaveName": "Save 1",  # NameSave
        "PlayerName": "Name",  # NamePlayer
        "GameType": "Rogue",  # TypeGame
        "# Player[0]": "Statistics -tremisabdoul",
        "Game.Player.Pv": Game.Player.Pv,  # Game.Player.Pv
        "Game.Player.MaxPv": Game.Player.MaxPv,  # "Game.Player.MaxPv
        "Game.Player.Damage": Game.Player.Damage,  # "Game.Player.Damage
        "Game.Player.Speed": Game.Player.Speed,  # Game.Player.Speed
        "Game.Player.SpeedY": Game.Player.SpeedY,  # Game.Player.SpeedY
        "Game.Player.Level": Game.Player.Level,  # Game.Player.Level
        "Game.Player.Gold": Game.Player.Gold,  # Game.Player.Gold
        "# Player[1]": "Position -tremisabdoul",
        "Game.Player.rect": Game.Player.rect,  # Game.Player.rect
        "Game.Player.LastY": Game.Player.LastY,  # Game.Player.LastY
        "Game.Player.YVector": Game.Player.YVector,  # Game.Player.YVector
        "Game.Player.Weapon1": Game.Player.Weapon1,  # Game.Player.Weapon1
        "Game.Player.Weapon2": Game.Player.Weapon2,  # Game.Player.Weapon2
        "# Phisics": "Actual Movement of Player -tremisabdoul",
        "Game.Player.Force.lastx": Game.Player.Force.lastx,  # Game.Force.lastx
        "Game.Player.Force.Base_Gravity": Game.Player.Force.Base_Gravity,  # Game.Force.Base_Gravity
        "Game.Player.Force.x": Game.Player.Force.x  # Game.Force.x
    }

    text_file = open("save1.csv", "w+", newline="\n")

    with text_file:
        Writer = csv.writer(text_file, quoting=2)
        Writer.writerows(Datalist.items())

    text_file.close()

    print("Your Data has been\b saved\b! : \n",text_file, "\n\n")


def Data_Load(Game):
    text_file = open("save1.csv", "r")

    list = []
    for line in text_file:
        stripped_line = line.strip()
        list.append(stripped_line)

    for item in range(len(list)):
        try:
            list[item] = int(list[item])
        except:
            if type(list[item]) == 'str':
                try:
                    list[item] = float(list[item])
                except:
                    if type(list[item]) == 'str':
                        try:
                            list[item] = tuple(list[item])
                        except:
                            if type(list[item]) == 'str':
                                list[item] = str(list[item])
        print(type(list[item]), " (", list[item], ")")

    Game.Saves.ActualSave = list
    print(list)
    text_file.close()


def ReScale(Game, Screen):
    Game.DataX = pygame.Surface.get_width(Screen)
    Game.DataY = pygame.Surface.get_height(Screen)
    Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
    Game.font = pygame.transform.scale(Game.font,
                                       (Game.Rescale(Game.font.get_width(), "X"),
                                        Game.Rescale(Game.font.get_height(), "Y")))
    Game.Player.image = pygame.transform.scale(Game.Player.image,
                                               (Game.Rescale(Game.Player.image.get_width(), "X"),
                                                Game.Rescale(Game.Player.image.get_height(), "Y")))


def Animation(Game):
    if Game.Player.YVector:
        if Game.Player.YVector < 0:
            FallAnimation(Game)
        else:
            JumpAnimation(Game)
    elif Game.Player.MovementKey:
        RunAnimation(Game)
    else:
        StandAnimation(Game)


def FallAnimation(Game):
    if Game.Player.Movement:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump2.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump2.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


def JumpAnimation(Game):
    if Game.Player.Movement:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump1.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump1.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


def RunAnimation(Game):
    if Game.Player.Movement:
        if Game.Frame % 10 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Run/Run1.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Run/Run2.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        if Game.Frame % 10 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Run/Run1.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Run/Run2.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


def StandAnimation(Game):
    if Game.Player.Movement:
        if Game.Frame % 10 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp2.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        if Game.Frame % 10 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/resp2.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/resp1.png")
                Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


def BackgroundScroll(Game):
    checker = Game.PositonPlayer % 1280
    if -10 < checker < 10:
        Game.Background.rect.midtop = (640 + checker, 0)
