
# Contient toutes les fonctions (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame
import os


# CrÃƒÂ©e l'ÃƒÂ©cran -tremisabdoul
def Display():
    """Fonction Permettent l'affichage de l'ÃƒÂ©cran -tremisabdoul"""

    pygame.init()
    pygame.display.set_caption("Anoari")
    size = (1280, 720)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen


def Jump(Game):
    """Fonction de jump: [ Key: Space ] -tremisabdoul"""

    if Game.Player.SpeedY < 0:
        Game.Player.rect.y += Game.Player.SpeedY
        Game.Player.SpeedY += 0.33
    else:
        Game.Player.SpeedY = 0


def DeplacementX(Game):
    """Fonction de dÃƒÂ©placement [gauche/droite] :  [ Left: LEFT / Q ], [ Right: RIGHT / D ] -tremisabdoul"""

    Game.Player.MovementKey = False
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.MovementKey = True
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.MovementKey = True
        Game.Player.Move_Left()


def MousePriter(Screen, Game):
    """Fonction d'affichage: Mouse -tremisabdoul"""

    Game.Mouse.rect.center = pygame.mouse.get_pos()
    Screen.blit(Game.Mouse.image, Game.Mouse.rect)


def Printer(Screen, Game):
    """Fonction d'affichage: ElÃƒÂ©ments in-game -tremisabdoul"""

    # DÃƒÂ©placement des ÃƒÂ©lÃƒÂ©ments -tremisabdoul
    Game.Monster.rect.x -= Game.Position
    Game.Background.rect.x -= Game.Position

    # Affiche a l'ÃƒÂ©cran des ÃƒÂ©lÃƒÂ©ments -tremisabdoul
    Screen.fill((60, 60, 120))
    # Screen.blit(Game.Background.image, Game.Background.rect)
    Screen.blit(Game.Sol.image, Game.Sol.rect)
    Screen.blit(Game.Player.image, Game.Player.rect)
    Screen.blit(Game.Monster.image, Game.Monster.rect)
    for nb in Game.all_plateform:
        nb.rect.x -= Game.Position
        Screen.blit(nb.image, nb.rect)
        Draw_rect(Screen, nb)
    Game.Sol.rect.x += Game.Position
    Draw_rect(Screen, Game.Player)
    Draw_rect(Screen, Game.Monster)
    MousePriter(Screen, Game)


# Print: -tremisabdoul
def UIPrinter(Screen, police1, Game):
    """Fonction d'affichage: ElÃƒÂ©ments d'interface in-game -tremisabdoul"""

    # Permet de rÃƒÂ©cupÃƒÂ©rer le nombre de frames a la seconde -tremisabdoul -tremisabdoul
    frame = 1
    fps = frame / Game.Tickchecker
    fps = "FPS : " + str(round(fps))

    # CrÃƒÂ©e une couleur plus ou moins rouge en fonction des PV restants -tremisabdoul
    Color = (Game.Player.Pv / Game.Player.MaxPv) * 255
    LifeColor = [255, Color, Color]

    # Transforme les variables en composent graphique -tremisabdoul
    printfps = police1.render(str(fps), True, (255, 255, 255))

    opti = str(round(Game.Player.Pv))
    opti = str(str(opti) + " / " + str(Game.Player.MaxPv) + " PV")
    opti = police1.render(str(opti), True, LifeColor)

    opti1 = round((Game.Player.Pv / Game.Player.MaxPv) * 100)
    opti1 = opti1 * "|"
    opti1 = police1.render(str(opti1), True, LifeColor)

    y = 34
    for Entity in Game.Entities:
        print("\n", Entity.YVector, "=", Entity.LastY, "-", Entity.rect.y)
        Entity.YVectorblit = police1.render("Y Vector checker: " + str(Entity.YVector), True, (100, 100, 200))
        Screen.blit(Entity.YVectorblit, (100, y))
        y += 10

    # Affiche a l'ÃƒÂ©cran les ÃƒÂ©lÃƒÂ©ments suivents -tremisabdoul
    Screen.blit(printfps, (6, 34))
    Screen.blit(opti, (15 + Color / 50, 48 + Color / 50))
    Screen.blit(opti1, (15 + Color / 50, 60 + Color / 50))


def pauseblit(Screen, Game):
    """Fonction d'affichage: ElÃƒÂ©ments de pause -tremisabdoul"""

    # Screen.blit(Game.Background.image, Game.Background.rect)
    # Screen.blit(Game.UI.baselayer, (0, 0))  # << Prends bcp de perf -tremisabdoul
    Screen.blit(Game.UI.resumebutton, Game.UI.resumebuttonrect)
    Screen.blit(Game.UI.savebutton, Game.UI.savebuttonrect)
    Screen.blit(Game.UI.settingsbutton, Game.UI.settingsbuttonrect)
    Screen.blit(Game.UI.quitbutton, Game.UI.quitbuttonrect)


def pause(Game, Screen, time, police1):
    """ Loop de pause -tremisabdoul"""

    while Game.Pause:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True
                # FullScreen -tremisabdoul
                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()
                # Revenir en jeu -tremisabdoul
                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = False
                    Game.InGame = True
                    time.sleep(0.1)

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            # Elements clicables: -tremisabdoul
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Game.UI.resumebuttonrect.collidepoint(event.pos):
                    Data_Load(Game, Screen, police1)
                    Game.Pause = False
                    Game.InGame = True
                elif Game.UI.savebuttonrect.collidepoint(event.pos):
                    Data_Save(Game, Screen, police1)
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

        # Permet de rÃƒÂ©cupÃƒÂ©rer le nombre de frames a la seconde -tremisabdoul
        Game.Tickchecker = time.time()
        Game.Tickchecker -= tick

        # Affichage des elements graphiques -tremisabdoul
        Screen.fill((40, 40, 40))
        pauseblit(Screen, Game)
        MousePriter(Screen, Game)

        # Affichage du rendu graphique sur la fenÃƒÂ¨tre -tremisabdoul
        pygame.display.flip()

        # Compteur de FPS et lock de FPS -tremisabdoul
        while Game.Tickchecker < 0.017:
            Game.Tickchecker = time.time()
            Game.Tickchecker -= tick

        fps = 1 / Game.Tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))


# Loop de Jeu: -tremisabdoul
def inGame(Game, time, Screen, police1):
    """ Loop de Jeu -tremisabdoul"""

    while Game.InGame:
        """ ===== Frame Limiter ===== """
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = time.time()
        Game.Frame += 1
        """ Sert a rien ! """
        # Test de la barre de vie
        if Game .Player.Pv > 1:
            Game.Player.Pv -= 1
        else:
            Game.Player.Pv = Game.Player.MaxPv
        # CrÃ©e 16 plateformes dans un espace donnÃ© (random)
        if len(Game.all_plateform) < 16:
            NewPlatform(Game)
        """ ===== Movements ====="""
        Movements(Game, Screen)
        """ ===== Printers ===== """
        # Animation du joueur -tremisabdoul
        Animation(Game)
        # Elements de jeu -tremisabdoul
        Printer(Screen, Game)
        # Interface de jeu -tremisabdoul
        UIPrinter(Screen, police1, Game)
        # Sourie -tremisabdoul
        MousePriter(Screen, Game)
        # Met a jour l'affichage (Print tout ce qui est blit avant) -tremisabdoul
        pygame.display.flip()
        """ ===== Key Inputs ===== """
        InGameKeys(Game, Screen)
        """ ===== Frame Limiter ===== """
        FrameLimiter(Game, time, tick)


def LobbyBlit(Screen, Game):
    """Fonction d'affichage: ElÃƒÂ©ments du lobby"""
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

        # Permet de rÃƒÂ©cupÃƒÂ©rer le nombre de frames a la seconde -tremisabdoul
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

        # Permet de rÃƒÂ©cupÃƒÂ©rer le nombre de frames a la seconde -tremisabdoul
        tickchecker = time.time()
        tickchecker -= tick

        MousePriter(Screen, Game)

        Screen.fill((0, 0, 0))

        # Affichage du nÃƒÂ©cessaire pour le texte des Options -steven
        Texte('RÃƒÂ©solution : ', police2, (255, 255, 255), Screen, 100, 100)
        Texte('Volume : ', police2, (255, 255, 255), Screen, 100, 225)
        Texte('Controles : ', police2, (255, 255, 255), Screen, 100, 350)

        pygame.display.flip()

        while tickchecker < 0.017:
            tickchecker = time.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))


# Fonction du texte -steven
def Texte(text, police2, color, Screen, x, y):
    Texte_Contenu = police2.render(text, 1, color)
    Texte_Rect = (x, y)
    Screen.blit(Texte_Contenu, Texte_Rect)


# TKT -tremisabdoul
def Data_Save(Game, Screen, police1):
    Loading = 0
    FullLoading = 8

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    import csv

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    Datalist = {
        "Variable": "Value",
        # Info -tremisabdoul [0-2]
        "# MetaSave": "# Infos -tremisabdoul",
        "SaveName": "Save 1",
        "PlayerName": "Name",
        "GameType": "Rogue",
        "# Player[0]": "# Statistics -tremisabdoul",
        "Game.Player.Pv": Game.Player.Pv,
        "Game.Player.MaxPv": Game.Player.MaxPv,
        "Game.Player.Damage": Game.Player.Damage,
        "Game.Player.Speed": Game.Player.Speed,
        "Game.Player.SpeedY": Game.Player.SpeedY,
        "Game.Player.Level": Game.Player.Level,
        "Game.Player.Gold": Game.Player.Gold,
        "# Player[1]": "# Position -tremisabdoul",
        "Game.Player.rect.x": Game.Player.rect.x,
        "Game.Player.rect.y": Game.Player.rect.y,
        "Game.Player.rect.height": Game.Player.rect.height,
        "Game.Player.rect.width": Game.Player.rect.width,
        "Game.Player.LastY": Game.Player.LastY,
        "Game.Player.YVector": Game.Player.YVector,
        "Game.PositionPlayer": Game.PositionPlayer,
        "# Phisics": "# Actual Movement of Player -tremisabdoul",
        "Game.Player.Force.lastx": Game.Player.Force.lastx,
        "Game.Player.Base_Gravity": Game.Player.Base_Gravity,
        "Game.Monster.Base_Gravity": Game.Monster.Base_Gravity,
        "Game.Player.Force.x": Game.Player.Force.x
    }

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    text_file = open("save1.csv", "w+", newline="")

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    with text_file:
        Writer = csv.writer(text_file, quoting=0)
        Writer.writerows(Datalist.items())

        Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    text_file.close()

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    del csv

    LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)

    print("\nYour data has been saved!\n", Loading, "/", FullLoading)

    return 0


# TKT -tremisabdoul
def Data_Load(Game, Screen, police1):

    Loading = 0
    FullLoading = 63
    Replace = Game.PositionPlayer
    import csv

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    file = "save1.csv"
    CSV_file = csv.DictReader(open(file, 'r'))
    Load = {}

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for lines in CSV_file:
        Load[lines["Variable"]] = lines["Value"]
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Pv = int(Load["Game.Player.Pv"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.MaxPv = int(Load["Game.Player.MaxPv"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Damage = float(Load["Game.Player.Damage"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Speed = float(Load["Game.Player.Speed"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.SpeedY = float(Load["Game.Player.SpeedY"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Level = int(Load["Game.Player.Level"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Gold = int(Load["Game.Player.Gold"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.x = float(Load["Game.Player.rect.x"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.y = float(Load["Game.Player.rect.y"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.height = int(Load["Game.Player.rect.height"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.width = int(Load["Game.Player.rect.width"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.LastY = float(Load["Game.Player.LastY"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.YVector = float(Load["Game.Player.YVector"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.PositionPlayer = int(Load["Game.PositionPlayer"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Force.lastx = float(Load["Game.Player.Force.lastx"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Base_Gravity = int(Load["Game.Player.Base_Gravity"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Monster.Base_Gravity = int(Load["Game.Monster.Base_Gravity"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Force.x = float(Load["Game.Player.Force.x"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for mob in Game.all_Monster:
        mob.rect.x -= Game.PositionPlayer - Replace
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for plateform in Game.all_plateform:
        plateform.rect.x -= Game.PositionPlayer - Replace
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    print("\nYour data has been loaded!\n", Loading, "/", FullLoading)
    return 0


# TKT -tremisabdoul
def ReScale(Game, Screen):
    Game.DataX = pygame.Surface.get_width(Screen)
    Game.DataY = pygame.Surface.get_height(Screen)
    Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
    Game.Background.image = pygame.transform.scale(Game.Background.image,
                                                   (Game.Rescale(Game.Background.image.get_width(), "X"),
                                                    Game.Rescale(Game.Background.image.get_height(), "Y")))
    Game.Player.image = pygame.transform.scale(Game.Player.image,
                                               (Game.Rescale(Game.Player.image.get_width(), "X"),
                                                Game.Rescale(Game.Player.image.get_height(), "Y")))


# TKT -tremisabdoul
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


# TKT -tremisabdoul
def FallAnimation(Game):
    if Game.Player.Movement:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump2.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump2.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


# TKT -tremisabdoul
def JumpAnimation(Game):
    if Game.Player.Movement:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump1.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump1.png")
        Game.Player.image = pygame.transform.scale(Game.Player.image, (120, 120))


# TKT -tremisabdoul
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


# TKT -tremisabdoul
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


# TKT -tremisabdoul
def BackgroundScroll(Game):
    checker = Game.PositionPlayer % 1280
    if -10 < checker < 10:
        Game.Background.rect.midtop = 640 - checker, 0
        print("\n", Game.Background.rect.width / 3 + checker, "= 640 + ", checker)


def LoadingScreen(Message, Screen, police1, Ratio, Loading):
    import random
    Loading += 1
    Screen.fill((0, 0, 0))

    image = pygame.image.load("Assets/Visual/UI/Load.png")
    rect = image.get_rect()
    image = pygame.transform.scale(image, (int(Loading / Ratio * pygame.Surface.get_rect(Screen).width/2),
                                           int(pygame.Surface.get_rect(Screen).height/40)))
    rect = image.get_rect(center=rect.center)
    rect.center = pygame.Surface.get_rect(Screen).center
    Screen.blit(image, (rect.x, rect.y))

    Texte("Please Wait: " + str(Loading) + " of " + str(Ratio), police1,
          (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)),
          Screen, random.randint(450, pygame.Surface.get_rect(Screen).width-512),
          pygame.Surface.get_rect(Screen).height/4)

    Texte(Message, police1,
          (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)),
          Screen, random.randint(450, pygame.Surface.get_rect(Screen).width-512),
          pygame.Surface.get_rect(Screen).height/3)

    Texte(":)", police1,
          (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)),
          Screen, random.randint(510, pygame.Surface.get_rect(Screen).width-512),
          pygame.Surface.get_rect(Screen).height/2.5)

    pygame.display.flip()

    return Loading


def Draw_rect(Screen, Target):
    pygame.draw.lines(Screen, (200, 150, 100), True, (
        Target.rect.midbottom, Target.rect.midtop, Target.rect.topleft, Target.rect.bottomleft, Target.rect.bottomright,
        Target.rect.topright, Target.rect.topleft, Target.rect.midleft, Target.rect.midright, Target.rect.bottomright))


def NewPlatform(Game):
    from Scripts.Classes import Plateform
    Plateform = Plateform()
    Game.all_plateform.add(Plateform)
    Game.PlateformNumber += 1


Animations = [
    "\nEx of usage:\nGame.Player.image = Animations[a[b[c[d[e]]]]]\n"
    "\ta=Ty pe Of A (Animatons[0] = Animation Tips), \n"
    "\tb=Specific entity\n"
    "\tc=Animation, \n"
    "\td=Directon(0=Right/1=Left), \n"
    "\te=Frame\n",
    [  # Player
        [  # Mystique
            [  # Stand
                [  # Animations[1[0[0[0[x]]]]] (Stand Right)
                    pygame.image.load("Assets/Visual/Mystique/resp2.png"),
                    pygame.image.load("Assets/Visual/Mystique/resp1.png")
                ],
                [  # (Stand Left)
                    pygame.image.load("Assets/Visual/Mystique/Left/resp1.png"),
                    pygame.image.load("Assets/Visual/Mystique/Left/resp1.png")
                ]
            ],
            [  # Run
                [  # (Run Right)
                    pygame.image.load("Assets/Visual/Mystique/Run/Run1.png"),
                    pygame.image.load("Assets/Visual/Mystique/Run/Run2.png")
                ],
                [  # (Run Left)
                    pygame.image.load("Assets/Visual/Mystique/Left/Run/Run1.png"),
                    pygame.image.load("Assets/Visual/Mystique/Left/Run/Run2.png")
                ]
            ],
            [  # Jump
                [  # (Jump Right)
                    pygame.image.load("Assets/Visual/Mystique/Jump/Jump1.png")
                ],
                [  # (Jump Left)
                    pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump1.png")
                ]
            ],
            [  # Fall
                [  # (Fall Right)
                    pygame.image.load("Assets/Visual/Mystique/Jump/Jump2.png")
                ],
                [  # Animations[1[0[3[1[x]]]]] (Fall Left)
                    pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump2.png")
                ]
            ]
        ]
    ],
    [  # Monster
        [  # Slime
            [  # Stand
                [  # Animations[2[0[0[0[x]]]]] (Stand Right)
                    pygame.image.load("Assets/Visual/Entities/Monster/Slime/Stand1.png")
                ],
                [  # Animations[2[0[0[1[x]]]]] (Stand Left)
                    pygame.image.load("Assets/Visual/Entities/Monster/Slime/Left/Stand1.png")
                ]
            ]
        ]
    ]

]

print("\n", Animations[0], Animations[1])


def Movements(Game, Screen):
    # Fonction de dÃƒÂ©placement gauche / droite -tremisabdoul
    DeplacementX(Game)

    for Entity in Game.Entities:
        Entity.LastY = Entity.rect.y

    for Monster in Game.all_Monster:
        Monster.Life(Screen, Game)
        Collide = Game.Player.check_collisions(Game.Player, Game.all_Monster)
        if not Collide:
            if Monster.Direction:
                Monster.Move_Left(Game)
            else:
                Monster.Move_Right(Game)
        else:
            if Collide[0].rect.center[0] > Game.Player.rect.center[0]:
                Monster.Direction = 0
                Monster.Move_Right(Game)
            else:
                Monster.Direction = 1
                Monster.Move_Left(Game)

    # Fonction de Jump -tremisabdoul
    if Game.Player.SpeedY:
        Jump(Game)

    for Entity in Game.Entities:
        Game.Player.Force.Gravity(Game, Entity)
        Entity.YVector = Entity.LastY - Entity.rect.y

    # DÃƒÂ©placements de player -tremisabdoul
    # Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Position = Game.Player.Force.AccelerationFunctionX()
    Game.Position = round(Game.Position)
    Game.PositionPlayer += Game.Position
    print("\n", Game.PositionPlayer)

    BackgroundScroll(Game)


def InGameKeys(Game, Screen):
    # Check les input et instances -tremisabdoul
    for event in pygame.event.get():

        # Touches enfoncees -tremisabdoul
        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            # Active le Jump() -tremisabdoul
            if Game.pressed.get(pygame.K_SPACE) \
                    and Game.Player.check_collisions(Game.Player, Game.all_plateform) \
                    and Game.Player.YVector == 0:
                Game.Player.SpeedY = -20

            # Activation de Pause -tremisabdoul
            if Game.pressed.get(pygame.K_ESCAPE):
                Game.Pause = True
                Game.InGame = False

            # Changement entre Fullscreen / Window -steven
            if Game.pressed.get(pygame.K_F11):
                print("\n", pygame.display.Info())
                if Game.Fullscreen == 0:
                    Screen = pygame.display.set_mode((Game.UserData.DataX, Game.UserData.DataY), pygame.FULLSCREEN)
                    Game.Fullscreen = 1
                else:
                    pygame.display.set_mode((Game.DataX, Game.DataY), pygame.RESIZABLE)
                    pygame.display.toggle_fullscreen()
                    pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
                    Game.Fullscreen = 0

        # Touches relachees -tremisabdoul
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Permet le resize de l'ecran -tremisabdoul
        if event.type == pygame.VIDEORESIZE:
            ReScale(Game, Screen)

        # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
        if event.type == pygame.QUIT:
            Game.InGame = False
            Game.Lobby = False
            Game.Pause = Fafrom User.UserDatal1 import *
import pygame
import random as rd

"""=====  Game [1]  ====="""


class Game:

    # Fonction exÃ©cutÃ©e au dÃ©marrage de Game -tremisabdoul
    def __init__(self):
        # SaveSlot devient une sous-classe de Game -tremisabdoul
        self.Saves = SaveSlot()

        # UserData devient une sous-classe de Game -tremisabdoul
        self.UserData = UserData()
        self.DataY = self.UserData.UserGraphicInfo.current_h
        self.DataX = self.UserData.UserGraphicInfo.current_w

        # Contient toutes les touches prÃ©ssÃ©es -tremisabdoul
        self.pressed = {}

        # Variables GÃ©nÃ©rales -tremisabdoul
        self.InGame = False
        self.Option = False
        self.Running = True
        self.Pause = False
        self.Lobby = True
        self.Fullscreen = 0
        self.Tickchecker = 1
        self.ActualFrame = 0
        self.Frame = 0
        self.Position = 0
        self.PositionPlayer = 0
        self.PlateformNumber = 1

    def Rescale(self, value, XorY):
        if XorY == "X":
            return round((value / 1280) * self.DataX)
        elif XorY == "Y":
            return round((value / 720) * self.DataY)

    def init_suite(self):
        # Player devient une sous-classe de Game -tremisabdoul
        self.Player = Player()
        # Sol devient une sous-classe de Game -Steven
        self.Sol = Sol()
        # Mouse devient une sous-classe de Game -tremisabdoul
        self.Mouse = Mouse()
        # UI devient une sous-classe de Game -tremisabdoul
        self.UI = UI()
        # Monster devient une sous-classe de Game - steven
        self.Monster = Monster()
        self.Background = Background()
        self.Wall = Wall()

        # CrÃ©ation du groupe composÃ© de tous les monstres -Steven
        self.all_Monster = pygame.sprite.Group()
        self.all_Monster.add(self.Monster)

        # CrÃ©ation du groupe composÃ© de tous les joueurs -Steven
        self.all_Player = pygame.sprite.Group()
        self.all_Player.add(self.Player)

        self.Entities = pygame.sprite.Group()
        self.Entities.add(self.Monster)
        self.Entities.add(self.Player)

        # CrÃ©ation du groupe composÃ© de toutes les plateformes -Steven
        self.all_plateform = pygame.sprite.Group()
        self.all_plateform.add(self.Sol)


"""=====  Game.Player [2.0]  ====="""


class Player(pygame.sprite.Sprite, Game):

    # Fonction exÃ©cutÃ©e au dÃ©marrage de Player -tremisabdoul
    def __init__(self):
        super().__init__()

        self.pop = False

        # Force devient une sous-classe de Player et Game est chargÃ© en tant que super-classe -tremisabdoul
        self.Force = Force()
        self.Game = Game

        # Statistiques -tremisabdoul
        self.Pv = 50
        self.MaxPv = 100
        self.Damage = 10
        self.Speed = 2
        self.SpeedY = 0

        self.Level = 0
        self.Gold = 0

        # Statistique gagnÃ©e par niveau / points -steven
        self.Gain_Stat_Level = 5
        self.Point_Pv = 0
        self.Point_Damage = 0

        self.Weapon1 = Weapon()
        self.Weapon2 = Weapon()

        # DÃ©finit l'Ã©lÃ©ment visuel en tant que variable et la hitbox de Player -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

        # Position de Player -tremisabdoul
        self.rect.center = (430, 600)

        self.LastY = 0
        self.YVector = 0
        self.YVectorblit = 0
        self.Base_Gravity = 0

        self.Movement = 1  # Droite = 1 Gauche = -1

        # Valeurs max et min que Player peut atteindre (Bords de l'Ã©cran x) -tremisabdoul
        self.MinX = 20
        self.MaxX = 1200

        # Valeurs max et min que Player peut atteindre (Bords de l'Ã©cran y) -tremisabdoul
        self.MinY = -20
        self.MaxY = 740
        self.MovementKey = False

    #   def Check_Collisions(rectA, rectB):
    #       if rectB.right < rectA.left:
    #           # rectB est Ã  gauche
    #           return False
    #       if rectB.bottom < rectA.top:
    #           # rectB est au-dessus
    #           return False
    #       if rectB.left > rectA.right:
    #           # rectB est Ã  droite
    #           return False
    #       if rectB.top > rectA.bottom:
    #           # rectB est en-dessous
    #           return False

    # Fonction de collision -tremisabdoul

    @staticmethod
    def check_collisions(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_rect)

    # Fonction de mouvement (Droite) -tremisabdoul
    def Move_Right(self):
        self.Force.xm += self.Speed
        self.Movement = 1

    # Fonction de mouvement (Gauche) -tremisabdoul
    def Move_Left(self):
        self.Force.xm -= self.Speed
        self.Movement = 0

    # Fonction de gain de stat ( valeur placÃ©e arbitrairement lol ) - steven
    def Gain_Stats(self):
        self.MaxPv += self.Gain_Stat_Level + (4 * self.Point_Pv)
        self.Damage += self.Gain_Stat_Level + (2 * self.Point_Damage)

    # Fonction appliquÃ© que si l'utilisateur meurt
    def Death(self):
        self.all_Monster = pygame.sprite.Group()
        self.Player.Pv = self.Player.MaxPv


"""=====  Game.Player.Force [2.1]  ====="""


#  Contient les vecteurs physiques -tremisabdoul
class Force:

    # Fonction exÃ©cutÃ©e au demarÃ©e au lancement de Force - tremisabdoul
    def __init__(self):

        self.x = float(0)
        self.xm = float(0)
        self.StepX = float(0)
        self.lastx = float(0)
        self.lasty = float(0)

        self.Game = Game

    # Fonction permettant un mouvement fluide -tremisabdoul
    def AccelerationFunctionX(self):

        # Forces appliquÃ©s + ((Forces appliquÃ©s lors de la derniÃ¨re frame / 1.3) / 1.1) -tremisabdoul
        self.StepX = self.xm + self.x + ((self.lastx / 1.3) / 1.1)

        if round(self.StepX) == 0:
            self.StepX = 0
            self.lastx = 0
            self.x = 0
            self.xm = 0
            return 0

        else:
            self.lastx = self.StepX
            self.x = 0
            self.xm = 0
            return self.StepX

    # Faut se dire que la gravitÃ© a une force de 33 et que lorsque
    # Base_Gravity est a 0 c'est que la force appliquÃ©e par le sol est de -33
    def Gravity(self, Game0, Target):
        base = Target.rect.y
        if Target.Base_Gravity < 22:  # Si force de sol > 0
            Target.Base_Gravity += 0.44  # Diminution de la force "Sol" (Ratio 0.66)
            # print("Gravity: ", Target.Base_Gravity)
            Target.rect.y += Target.Base_Gravity
        else:
            Target.Base_Gravity = 22  # Force de sol = 0
            # print("Gravity: ", 22)
            Target.rect.y += 22

        # VÃ©rification des collisions entre Player et toutes les plateformes
        Collide = Game0.Player.check_collisions(Target, Game0.all_plateform)
        print("\n", base, Target.rect.y)
        for item in Collide:
            print("\n", Target.Base_Gravity)
            print("\nCollide ? ", bool(item),
                  "\nFall ? ", bool(Target.YVector),
                  "\nBottom Collide ? ", bool(Target.rect.bottom <= item.rect.top + Target.Base_Gravity + 2))

            if item and Target.YVector <= 1 and (Target.rect.bottom <= item.rect.top + Target.Base_Gravity + 2):
                Target.rect.y = base
                Replace = item.rect.top - (Target.rect.bottom - 1)  # Y reset (Premier pixel du rect de plateforme)
                Target.SpeedY = 0  # Cancel le saut
                Target.Base_Gravity = 0  # Reset la force du sol (-33)
                print("\nStand: ", Replace)
                Target.rect.y += Replace


"""=====  Game.Sol [3]  ====="""


class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.UserData = UserData()

        # DÃ©finit l'Ã©lÃ©ment visuel en tant que variable -steven
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la rÃ©solution indiquÃ©e -tremisabdoul
        self.image = pygame.transform.scale(self.image, (1280, 34))

        # DÃ©finit la hitbox de sol -steven
        self.rect = self.image.get_rect()

        # Position de la plateforme principale -steven
        self.rect.x = 0
        self.rect.y = 686


"""=====  Game.Plateform [4]  ====="""


class Plateform(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        # DÃ©finit l'Ã©lÃ©ment visuel en tant que variable -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la rÃ©solution indiquÃ©e -tremisabdoul
        self.image = pygame.transform.scale(self.image, (320, 20))

        # DÃ©finit la hitbox de sol -tremisabdoul
        self.rect = self.image.get_rect()

        import random as random
        # Position de la plateforme -tremisabdoul
        self.rect.x = random.randint(-20, 1900)
        self.rect.y = random.randint(100, 600)
        del random


"""=====  Game.Mouse [5]  ====="""


class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Rends la sourie windows invisible -tremisabdoul
        pygame.mouse.set_visible(False)

        # Definit l'image (emplacent la sourie) -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/UI/Mouse.png")
        self.image = pygame.transform.scale(self.image, (22, 22))

        # Cree la hit-box de l'image -tremisabdoul
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)


"""=====  Game.UI [6]  ====="""


# Interface -tremisabdoul
class UI:

    def __init__(self):
        super().__init__()

        """ CatÃ©gorie Pause """
        # Font grisÃ© (Ca prends full perf) -tremisabdoul
        self.baselayer = pygame.image.load("Assets/Visual/UI/baselayer.png")
        self.baselayer = pygame.transform.scale(self.baselayer, (1280, 720))

        # Boutton "REPRENDRE" -tremisabdoul
        self.resumebutton = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.resumebutton = pygame.transform.scale(self.resumebutton, (140, 30))
        self.resumebuttonrect = self.resumebutton.get_rect()
        self.resumebuttonrect.x = 640 - 70
        self.resumebuttonrect.y = 360 - 40

        # Boutton "SAUVEGARDER" -tremisabdoul
        self.savebutton = pygame.image.load("Assets/Visual/UI/bouton_SAUVEGARDER.png")
        self.savebutton = pygame.transform.scale(self.savebutton, (172, 30))
        self.savebuttonrect = self.savebutton.get_rect()
        self.savebuttonrect.x = 640 - 86
        self.savebuttonrect.y = 360

        # Boutton "PARAMÃˆTRE" -steven
        self.settingsbutton = pygame.image.load("Assets/Visual/UI/bouton_SETTINGS.png")
        self.settingsbutton = pygame.transform.scale(self.settingsbutton, (100, 30))
        self.settingsbuttonrect = self.settingsbutton.get_rect()
        self.settingsbuttonrect.x = 640 - 50
        self.settingsbuttonrect.y = 360 + 40

        # Boutton "QUITER" -tremisabdoul
        self.quitbutton = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.quitbutton = pygame.transform.scale(self.quitbutton, (100, 30))
        self.quitbuttonrect = self.quitbutton.get_rect()
        self.quitbuttonrect.x = 640 - 50
        self.quitbuttonrect.y = 360 + 80

        """ CatÃ©gorie Menu d'accueil """

        # IntÃ©gration de l'image qui apparaitrera du menu d'accueil -steven
        self.lobbybackground = pygame.image.load("Assets/Visual/background.jpg")
        self.lobbybackground = pygame.transform.scale(self.lobbybackground, (1280, 720))

        # IntÃ©gration du boutton "JOUER" -steven
        self.lobby_playbutton = pygame.image.load("Assets/Visual/UI/bouton_JOUER.png")
        self.lobby_playbutton = pygame.transform.scale(self.lobby_playbutton, (82, 30))
        self.lobby_playbuttonrect = self.lobby_playbutton.get_rect()
        self.lobby_playbuttonrect.x = 1000
        self.lobby_playbuttonrect.y = 360 - 30

        # IntÃ©gration du boutton "CHARGER" -steven
        self.lobby_loadbutton = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.lobby_loadbutton = pygame.transform.scale(self.lobby_loadbutton, (140, 30))
        self.lobby_loadbuttonrect = self.lobby_loadbutton.get_rect()
        self.lobby_loadbuttonrect.x = 1000 - 30
        self.lobby_loadbuttonrect.y = 360

        # IntÃ©gration du boutton "QUITTER" -Steven
        self.lobby_quitbutton = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.lobby_quitbutton = pygame.transform.scale(self.lobby_quitbutton, (100, 30))
        self.lobby_quitbuttonrect = self.lobby_quitbutton.get_rect()
        self.lobby_quitbuttonrect.x = 1000 - 60
        self.lobby_quitbuttonrect.y = 360 + 30


"""=====  Monstre [7]  ====="""


class Monster(pygame.sprite.Sprite, Game):

    # Fonction Ã©xÃ©cutÃ© au dÃ©marrage de Monster -steven
    def __init__(self):
        super().__init__()

        # Statistiques -steven
        self.Pv = 100
        self.MaxPv = 100
        self.DamageDealt = 10
        self.Speed = 3

        self.image = pygame.image.load("Assets/Visual/Entities/Monster/Slime/Stand1.png")

        self.rect = self.image.get_rect()

        self.rect.x = rd.randint(150, 1050)
        self.rect.y = 50
        self.LastY = 675

        self.YVector = 0
        self.YVectorblit = 0
        self.Base_Gravity = 0

        self.rect = self.image.get_rect(midtop=self.rect.midtop)

        # Barre de pv des monstres -tremisabdoul
        self.image0 = pygame.image.load("Assets/Visual/UI/100pv.png")
        self.image0 = pygame.transform.scale(self.image0, (200, 30))

        self.pvfontrect = self.image0.get_rect()
        self.pvfontrect = self.image0.get_rect(midbottom=self.pvfontrect.midbottom)
        self.pvfontrect.midbottom = self.rect.midtop
        self.pvfontrect.y += 10

        self.Direction = 1

    # Dessin concernant la barre de vie du monstre -steven / tremisabdoul
    def Life(self, Screen, Game):
        if self.Pv > 0:
            self.pvfontrect = self.image0.get_rect(midbottom=self.pvfontrect.midbottom)
            self.pvfontrect.midbottom = self.rect.midtop
            self.pvfontrect.y -= 7
            self.image0 = pygame.transform.scale(self.image0, (int(self.Pv / self.MaxPv * 64), 8))
            self.Pv -= 0.2
            Screen.blit(self.image0, (self.pvfontrect.x - Game.Position, self.pvfontrect.y))

    # DÃ©placement du monstre vers la droite -steven
    def Move_Right(self, Game):
        if Game.Player.check_collisions(self, Game.all_plateform):
            self.rect.x += self.Speed
        else:
            self.rect.x -= int(self.Speed * 1)
            self.Direction = 1

    # DÃ©placement du monstre vers la gauche -steven
    def Move_Left(self, Game):
        if Game.Player.check_collisions(self, Game.all_plateform):
            self.rect.x -= self.Speed
        else:
            self.rect.x += int(self.Speed * 1.5)
            self.Direction = 0

class Weapon:

    def __init__(self):

        # Type d'arme Ex: Mitraillette = 3
        self.MetaType = rd.randrange(1, 5, 1)

        # Arme en question Ex: Mitraillette.Poison = 3.4
        self.MetaWeapon = rd.randrange(1, 10, 1)

        # RarertÃ© Ex: Mitraillette.Poison.Rare = 3.4.2
        self.MetaClass = rd.randrange(1, 4, 1)

        # Donne l'ensemble des propiÃ©tÃ©es de l'arme  Ex: 3.4.2
        self.MetaName = [self.MetaType, self.MetaWeapon, self.MetaClass]

        self.Damage = rd.randrange(2, 9, 1)
        self.Speed = rd.randrange(41, 80, 1)/10
        self.CD = self.MetaWeapon * 3

        self.DamageBuff = 0
        self.SpeedBuff = 0
        self.CDR = 0
        self.tester = self.MetaClass

        while self.tester > 0:
            self.RandomTest = rd.randrange(1, 3, 1)
            self.tester -= 1
            if self.RandomTest == 1:
                self.DamageBuff += rd.randrange(1, 5, 1)
            if self.RandomTest == 2:
                self.SpeedBuff -= rd.randrange(1, 20, 1) / 10
            if self.RandomTest == 3:
                self.CDR += rd.randrange(1, 25, 1)
        del self.tester
        print("\nWeapon:", self.MetaName, "\nRarete", self.MetaClass,
              "\n\tDamage: ", self.Damage, "+",  self.DamageBuff, "\n\tSpeed: ", self.Speed, "+", self.SpeedBuff,
              "\n\tCD: ", self.CD, "* ( 100 / ( 100 +", "CDR = ", self.CDR, "))")


class Wall:
    def __init__(self):
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(midtop=self.rect.midtop)


class Background:

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Visual/UI/Background.png")
        # self.image = pygame.transform.scale(self.image, (3848, 686))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(midtop=self.rect.midtop)
        self.rect.midtop = (self.rect.width / 3, 0)
lse
            Game.running = False
            pygame.quit()
            quit()
            break


def FrameLimiter(Game, time, tick):
    # Permet d'avoir des frames regulieres -tremisabdoul
    Game.Tickchecker = time.time()
    Game.Tickchecker -= tick

    while Game.Tickchecker < 0.017:
        Game.Tickchecker = time.time()
        Game.Tickchecker -= tick
