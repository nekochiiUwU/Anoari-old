# Contient toutes les fonctions (pour ne pas envahir les autres fichiers) -tremisabdoul
import os
from Scripts.Printers import *

print("/Scripts/Functions: Loading")

""" ===  Init  === """


def Display():
    """CrÃ©ation de la fenÃ¨tre -tremisabdoul"""

    pygame.init()
    pygame.display.set_caption("Anoari")
    size = (1280, 720)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen


def Paterns(Game):
    """Initialisation: Paterns -tremisabdoul"""
    Load = []
    PaternsFile = open('Data/Paterns.txt', 'r')

    for line in PaternsFile:
        line = line.strip()
        Load.append(line)
    Load = "".join(Load)
    Load = Load.split(",")
    Game.Paterns = Load
    Game.Paterns.pop(0)

    for Patern in range(len(Game.Paterns)):

        Game.Paterns[Patern] = Game.Paterns[Patern].split(":")

        for item in range(len(Game.Paterns[Patern])):
            if 2 <= item <= 6:
                Game.Paterns[Patern][item] = ",".join(Game.Paterns[Patern][item])
                Game.Paterns[Patern][item] = Game.Paterns[Patern][item].split(",")

    Game.Grid = {"xTiles": len(Game.Paterns[0][2]),
                 "yTiles": len(Game.Paterns[0]),
                 "width": 250,
                 "height": 150,
                 "x": 0,
                 "y": 0}

    for _ in range(10):
        from Scripts.Classes import Patern
        Patern = Patern()
        Patern.Init(Game, NewWall, NewPlatform, SpawnMonster)
        Game.ApplyedPatens.add(Patern)


""" ===  Loops  === """


def Lobby(Game, Screen):
    """Loop d'ecran d'acceuil -steven"""

    while Game.Lobby:
        """ ===== Frame Limiter ===== """
        Game.Tick = Game.time()
        Game.Frame += 1
        FrameLimiter(Game, Screen)

        """ ===== Key Inputs ===== """
        LobbyKeys(Game)

        """ ===== Printer ===== """
        LobbyPrinter(Screen, Game)

        """ ===== Button Movement ===== """
        Game.UI.Lobby.TitleMenuButtonDeplacement(Game)


def inGame(Game, Screen):
    """ Loop de Jeu -tremisabdoul"""

    while Game.InGame:
        """ ===== Frame Limiter ===== """
        Game.Tick = Game.time()
        Game.Frame += 1
        """ ===== Movements ===== """
        Movements(Game)
        """ ===== Camera ===== """
        SmoothCamera(Game)
        """ ===== Key Inputs ===== """
        InGameKeys(Game, Screen)
        """ ===== Printer ===== """
        Printer(Screen, Game)
        """ ===== Frame Limiter ===== """
        FrameLimiter(Game, Screen)


def Pause(Game, Screen):
    """ Loop de pause -tremisabdoul"""

    while Game.Pause:
        """ ===== Frame Limiter ===== """
        Game.Tick = Game.time()
        Game.Frame += 1
        FrameLimiter(Game, Screen)

        """ ===== Key Inputs ===== """
        PauseKeys(Game)

        """ ===== Printer ===== """
        PausePrinter(Screen, Game)


def Option(Game, Screen):
    """Loop des options -steven"""
    ImportOptions(Game)

    while Game.Option:
        """ ===== Frame Limiter ===== """
        Game.Tick = Game.time()
        Game.Frame += 1
        FrameLimiter(Game, Screen)

        """ ===== Key Inputs ===== """
        OptionKeys(Game)

        """ ===== Key Interaction ===== """
        OptionInterations(Game, Screen)

        """ ===== Printer ===== """
        OptionPrinter(Game, Screen)


def SaveMenu(Game, Screen):
    """Loop de menu de save -steven"""

    """ ===== Utility List ===== """
    SavePos = [("SaveButton1", pygame.Rect(200, 100, 500, 100)),
               ("SaveButton2", pygame.Rect(200, 300, 500, 100)),
               ("SaveButton3", pygame.Rect(200, 500, 500, 100))]
    State = ["Save/save1.csv", "Save/save2.csv", "Save/save3.csv"]

    while Game.SaveMenu:
        """ ===== Frame Limiter ===== """
        Game.Tick = Game.time()
        Game.Frame += 1
        FrameLimiter(Game, Screen)

        """ ===== Key Inputs ===== """
        SaveMenuKeys(Game, Screen, SavePos, State)

        """ ===== Printer ===== """
        SaveMenuPrinter(Game, Screen, SavePos, State)


""" ===  Movement  === """


def Movements(Game):
    """Contiens tout les mouvements ingame -tremisabdoul"""
    global booleanjump

    DeplacementX(Game)

    for Entity in Game.Entities:
        Entity.LastY = Entity.rect.y

    for Monster in Game.all_Monster:
        Collide = Game.check_collisions(Game.Player, Game.all_Monster)
        Skip = False
        for item in Monster.Special:
            if item == 'fly':
                Skip = True
        if -69 < Monster.rect.x < 1279 or Skip:
            if not Collide:
                if Monster.Direction:
                    Monster.Move_Left(Game)
                else:
                    Monster.Move_Right(Game)
            elif Collide:
                if Collide[0].rect.center[0] > Game.Player.rect.center[0]:
                    Monster.Direction = 0
                    Monster.Move_Right(Game)
                else:
                    Monster.Direction = 1
                    Monster.Move_Left(Game)

                if Monster.OnCD == True:
                    if (pygame.time.get_ticks() - Game.Timing ) / 1000 > 2:
                        Monster.OnCD = False
                        Game.Timing = 0
                else:
                    Game.Player.Get_Hit(Game.Monster.DamageDealt, Game)
                    Game.Timing = pygame.time.get_ticks()
                    Monster.OnCD = True

    if Game.pressed.get(Game.Keys[0][2]) \
            and Game.check_collisions(Game.Player, Game.all_plateform) \
            and Game.Player.YVector == 0:
        Game.Player.SpeedY = -5
        booleanjump = 1
        Jump(Game)

    elif Game.Player.SpeedY:
        Jump(Game)

    for Entity in Game.Entities:
        if -69 < Entity.rect.x < 1279:
            Game.Player.Force.Gravity(Game, Entity)
            Entity.YVector = Entity.LastY - Entity.rect.y

    Game.Position = Game.Player.Force.AccelerationFunctionX()
    for Target in Game.Entities:
        Collide = Game.check_collisions(Target, Game.all_wall)

        if Target == Game.Player:
            Target.rect.x += Game.Position

        for Wall in Collide:

            if not Wall.rect.bottomleft < Target.rect.midtop < Wall.rect.topright:

                if Target == Game.Player:
                    if Wall.rect.center < Target.rect.center:
                        if Game.Position < 0:
                            Game.Position = -Game.Position
                    elif Wall.rect.center > Target.rect.center:
                        if Game.Position > 0:
                            Game.Position = -Game.Position

                elif Target in Game.AcrossWall:
                    if Wall.rect.center < Target.rect.center:
                        Target.rect.x -= Wall.rect.right - (Target.rect.left - 33)
                        Target.Direction = 1
                    elif Wall.rect.center > Target.rect.center:
                        Target.rect.x -= Wall.rect.left - (Target.rect.right + 33)
                        Target.Direction = 0

                else:
                    if Wall.rect.center < Target.rect.center:
                        Target.rect.x += Wall.rect.right - (Target.rect.left - 33)
                        Target.Direction = 0
                    elif Wall.rect.center > Target.rect.center:
                        Target.rect.x += Wall.rect.left - (Target.rect.right + 33)
                        Target.Direction = 1

            else:
                if Target == Game.Player:
                    Target.Base_Gravity = Wall.rect.bottom - Target.rect.top
                    if Target.Base_Gravity < -11:
                        Target.Base_Gravity = -11
                    Game.Player.SpeedY = 0

        if Target == Game.Player:
            Target.rect.x += Game.Position

    Game.Position = round(Game.Position)

    Game.PositionPlayer += Game.Position

    BackgroundScroll(Game)

    if Game.PositionPlayer > 10000:
        print("Check Fin du niveau atteint = True")


def Jump(Game):
    """Saut: [ Key: Space ] -tremisabdoul"""
    global booleanjump
    if Game.Player.SpeedY > -17 and Game.pressed.get(Game.Keys[0][2]) and booleanjump:
        Game.Player.SpeedY -= 3.4
        Game.Player.rect.y += Game.Player.SpeedY
    else:
        booleanjump = 0
        if Game.Player.SpeedY < 0:
            Game.Player.rect.y += Game.Player.SpeedY
            Game.Player.SpeedY += 0.4
        else:
            Game.Player.SpeedY = 0


def DeplacementX(Game):
    """Deplacement X:  [Gauche: LEFT / Q ], [Droite: RIGHT / D] -tremisabdoul"""

    Game.Player.MovementKey = False

    if Game.pressed.get(Game.Keys[2][2]) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.MovementKey = True
        Game.Player.Move_Right(Game)

    if Game.pressed.get(Game.Keys[1][2]) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.MovementKey = True
        Game.Player.Move_Left(Game)


""" ===  Limiter  === """


def FrameLimiter(Game, Screen):
    """Limiteur de FPS -tremisabdoul"""
    Game.Tickchecker = Game.time()
    Game.Tickchecker -= Game.Tick
    if Game.ShowHitbox:

        start = Game.time()
        Test = Game.time() - start

        TestL1 = str(round((Game.Tickchecker - Test) / 0.00017)) + "    % of 60 FPS: Framerate without Test"
        TestL2 = str(round(Game.Tickchecker / 0.00017)) + "    % of 60 FPS: Framerate"
        TestL3 = str(round(Test / 0.00017)) + "    % of 60 FPS : Test"
        Pos = " \t Position =" + str(Game.PositionPlayer) + " Px" + " \t End = 10.000"

        Texte(Game.police1, TestL1, (255, 255, 255), Screen, (1000, 20))
        Texte(Game.police1, TestL2, (255, 255, 255), Screen, (1000, 40))
        Texte(Game.police1, TestL3, (255, 255, 255), Screen, (1000, 60))
        Texte(Game.police1, Pos, (255, 255, 255), Screen, (10, 700))

    pygame.display.flip()

    while Game.Tickchecker < 0.017:
        Game.Tickchecker = Game.time()
        Game.Tickchecker -= Game.Tick


""" ===  Input  === """


def LobbyKeys(Game):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            if Game.pressed.get(pygame.K_F11):
                pygame.display.toggle_fullscreen()

        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Game.pressed[str(event.button)] = True

            if Game.UI.Lobby.playbuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.InGame = True
                Game.Lobby = False
            elif Game.UI.Lobby.loadbuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Lobby = False
                Game.SaveMenu = True
                Game.SaveValue = 1
            elif Game.UI.Lobby.quitbuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Running = False
                pygame.quit()

        elif event.type == pygame.MOUSEBUTTONUP:
            Game.pressed[str(event.button)] = False

        if event.type == pygame.QUIT:
            Game.InGame = False
            Game.Option = False
            Game.Pause = False
            Game.SaveMenu = False
            Game.Lobby = False
            Game.Running = False
            pygame.quit()


def InGameKeys(Game, Screen):
    """Check des input et instances -tremisabdoul"""

    for event in pygame.event.get():

        # Touches enfoncees -tremisabdoul
        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

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

            if Game.pressed.get(pygame.K_F10):
                pygame.image.save(Screen, "screenshot.jpg")

        # Touches relachees -tremisabdoul
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Boutons souris enfonces -nekochii x tremisabdoul
        if event.type == pygame.MOUSEBUTTONDOWN:
            Game.pressed[str(event.button)] = True
            if event.button == 1:
                if Game.pressed.get("3"):
                    Game.CastSpell = True
                    Game.Projectile.Add(Game)
                    Game.Countframes = 3
                print("Left Click (None)")
            elif event.button == 2:
                print("Middle Click (Hitbox + print(Game.PlayerPosition))")
                # Game.data.stop()
                # Game.data.play()
                Game.ShowHitbox = not Game.ShowHitbox
            elif event.button == 3:
                print("Right Click (Mode VisÃƒÂ©e)")
                pygame.mouse.set_visible(False)
                Game.PrepaSpell = True
            elif event.button > 3:
                if event.button % 2:
                    print("Scroll Down (None) Value =", event.button)
                else:
                    print("Scroll Up (None) Value =", event.button)
        # Boutons souris relaches -nekochii
        elif event.type == pygame.MOUSEBUTTONUP:
            Game.pressed[str(event.button)] = False
            if event.button == 3:
                Game.PrepaSpell = False
                pygame.mouse.set_visible(True)

        # Permet le resize de l'ecran -tremisabdoul
        if event.type == pygame.VIDEORESIZE:
            ReScale(Game, Screen)

        # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
        if event.type == pygame.QUIT:
            Game.Option = False
            Game.Pause = False
            Game.SaveMenu = False
            Game.Lobby = False
            Game.InGame = False
            Game.Running = False
            pygame.quit()


def PauseKeys(Game):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            if Game.pressed.get(pygame.K_F11):
                pygame.display.toggle_fullscreen()
            elif Game.pressed.get(pygame.K_ESCAPE):
                Game.Pause = False
                Game.InGame = True

        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Game.UI.resumebuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Pause = False
                Game.InGame = True
            elif Game.UI.savebuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Pause = False
                Game.SaveMenu = True
                Game.SaveValue = 2
            elif Game.UI.settingsbuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Pause = False
                Game.Option = True
            elif Game.UI.quitbuttonrect.collidepoint(event.pos):
                Game.Click.play()
                Game.Pause = False
                Game.Lobby = True

        if event.type == pygame.QUIT:
            Game.InGame = False
            Game.Option = False
            Game.SaveMenu = False
            Game.Lobby = False
            Game.Pause = False
            Game.Running = False
            pygame.quit()


def OptionKeys(Game):

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            if Game.pressed.get(pygame.K_ESCAPE):
                Game.Pause = True
                Game.Option = False

            elif Game.pressed.get(pygame.K_SPACE):
                Game.Option = False
                Game.InGame = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            for Key in Game.Keys:
                if Key[0].collidepoint(event.pos):
                    Key[1] = True
                if Game.Volume[0].collidepoint(event.pos):
                    Game.Volume[1] = True

        if event.type == pygame.QUIT:
            Game.InGame = False
            Game.Pause = False
            Game.SaveMenu = False
            Game.Lobby = False
            Game.Option = False
            Game.Running = False
            pygame.quit()


def SaveMenuKeys(Game, Screen, SavePos, State):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            if Game.pressed.get(pygame.K_ESCAPE):
                if Game.SaveValue == 1:
                    Game.SaveMenu = False
                    Game.Lobby = True
                    Game.SaveValue = 0
                elif Game.SaveValue == 2:
                    Game.SaveMenu = False
                    Game.Pause = True
                    Game.SaveValue = 0

        # Sauvegarde des donnees du joueurs (SaveValue == 2 signifie qu'il est rentrÃ© par le menu pause) -steven
        elif event.type == pygame.MOUSEBUTTONDOWN and Game.SaveValue == 2:
            if SavePos[0][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[0]
                Data_Save(Game, Screen, SaveState)

            elif SavePos[1][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[1]
                Data_Save(Game, Screen, SaveState)

            elif SavePos[2][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[2]
                Data_Save(Game, Screen, SaveState)

        elif event.type == pygame.MOUSEBUTTONDOWN and Game.SaveValue == 1:
            if SavePos[0][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[0]
                Data_Load(Game, Screen, SaveState)
                Game.SaveMenu = False
                Game.InGame = True

            elif SavePos[1][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[1]
                Data_Load(Game, Screen, SaveState)
                Game.SaveMenu = False
                Game.InGame = True

            elif SavePos[2][1].collidepoint(event.pos):
                Game.Click.play()
                SaveState = State[2]
                Data_Load(Game, Screen, SaveState)
                Game.SaveMenu = False
                Game.InGame = True

        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
        if event.type == pygame.QUIT:
            Game.SaveValue = 0
            Game.InGame = False
            Game.Option = False
            Game.Pause = False
            Game.Lobby = False
            Game.SaveMenu = False
            Game.Running = False
            pygame.quit()


""" ===  Camera  === """


def SmoothCamera(Game):
    """Mouvements de CamÃ©ra -tremisabdoul"""
    Game.Player.LastX = Game.Player.rect.x - 350
    Game.lastPosition = Game.Position
    Game.Player.rect.x = 350
    Game.Player.rect.x += (Game.Position + (Game.Player.LastX / 1.9) / 1.5)


def BackgroundScroll(Game):
    """DÃ©placement du Background -tremisabdoul"""
    checker = Game.PositionPlayer % 1280
    if -10 < checker < 10:
        Game.Background.rect.midtop = 640 - checker, 0


def ReScale(Game, Screen):
    """PAS FINI    Rescale Trop la flemme le le finir je vais le faire vous inquÃ©tez pas -tremisabdoul    PAS FINI"""
    Game.DataX = pygame.Surface.get_width(Screen)
    Game.DataY = pygame.Surface.get_height(Screen)
    Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
    Game.Background.image = pygame.transform.scale(Game.Background.image,
                                                   (Game.Rescale(Game.Background.image.get_width(), "X"),
                                                    Game.Rescale(Game.Background.image.get_height(), "Y")))
    Game.Player.image = pygame.transform.scale(Game.Player.image,
                                               (Game.Rescale(Game.Player.image.get_width(), "X"),
                                                Game.Rescale(Game.Player.image.get_height(), "Y")))


""" ===  Pop  === """


def NewPlatform(Game, x, y):
    """CrÃ©ation d'une plateforme -tremisabdoul"""
    from Scripts.Classes import Plateform
    Plateform = Plateform()
    Plateform.rect.x, Plateform.rect.y = x * 250, y * 150 + 130
    Game.all_plateform.add(Plateform)
    Game.PlateformNumber += 1


def NewWall(Game, x, y):
    """CrÃ©ation d'un mur -tremisabdoul"""
    from Scripts.Classes import Wall
    Wall = Wall()
    Wall.rect.x, Wall.rect.y, Wall.rect.height, Wall.rect.width = x * 250, y * 150, 150, 250
    Game.all_wall.add(Wall)
    Game.WallNumber += 1


def SpawnMonster(Game, x, y):
    from Scripts.Classes import Monster
    for _ in range(Game.randint(0, 1)):
        Mob = Monster()
        Mob.rect.x, Mob.rect.y = x * 250, y * 150
        Game.all_Monster.add(Mob)
        Game.Entities.add(Mob)


""" ===  Operations  === """


def Data_Save(Game, Screen, SaveState):
    """Save des donnÃ©es -tremisabdoul"""

    Loading = 0
    FullLoading = 4

    import csv

    Loading = LoadingScreen(Game, "I'm currently loading your data", Screen, FullLoading, Loading)

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
        "Game.Player.Armor": Game.Player.Armor,
        "Game.Player.Mana": Game.Player.Mana,
        "# Player[1]": "# Statistique Variable -steven",
        "Game.Player.CDR": Game.Player.CDR,
        "Game.Player.AttackSpeed": Game.Player.AttackSpeed,
        "Game.Player.CCHit": Game.Player.CCHit,
        "Game.Player.CCSpell": Game.Player.CCSpell,
        "Game.Player.CCDamage": Game.Player.CCDamage,
        "Game.Player.Penetration": Game.Player.Penetration,
        "Game.Player.ManaRegen": Game.Player.ManaRegen,
        "Game.Player.XP_Multiplicator": Game.Player.XP_Multiplicator,
        "Game.Player.Damage.Multiplicator": Game.Player.Damage_Multiplicator,
        "# Player[2]": "# Position -tremisabdoul",
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

    Loading = LoadingScreen(Game, "I'm currently opening your data file", Screen, FullLoading, Loading)

    text_file = open(SaveState, "w+", newline="")

    Loading = LoadingScreen(Game, "I'm currently writing your data file ()", Screen, FullLoading, Loading)

    with text_file:
        Writer = csv.writer(text_file, quoting=0)
        Writer.writerows(Datalist.items())

    text_file.close()
    del csv

    LoadingScreen(Game, "I saved your data", Screen, FullLoading, Loading)

    return 0


def Data_Load(Game, Screen, SaveState):
    """Load des donnÃ©es -tremisabdoul"""

    Loading = 0
    FullLoading = 7
    Replace = Game.PositionPlayer
    import csv

    Loading = LoadingScreen(Game, "I'm currently opening your data file", Screen, FullLoading, Loading)

    file = SaveState
    CSV_file = csv.DictReader(open(file, 'r'))
    Load = {}

    Loading = LoadingScreen(Game, "I'm currently reading your data file", Screen, FullLoading, Loading)

    for lines in CSV_file:
        Load[lines["Variable"]] = lines["Value"]

    Loading = LoadingScreen(Game, "I'm currently loading your data", Screen, FullLoading, Loading)

    Game.Player.Pv = int(Load["Game.Player.Pv"])
    Game.Player.MaxPv = int(Load["Game.Player.MaxPv"])
    Game.Player.Damage = float(Load["Game.Player.Damage"])
    Game.Player.Speed = float(Load["Game.Player.Speed"])
    Game.Player.SpeedY = float(Load["Game.Player.SpeedY"])
    Game.Player.Level = int(Load["Game.Player.Level"])
    Game.Player.Gold = int(Load["Game.Player.Gold"])
    Game.Player.rect.x = int(Load["Game.Player.rect.x"])
    Game.Player.rect.y = int(Load["Game.Player.rect.y"])
    Game.Player.rect.height = int(Load["Game.Player.rect.height"])
    Game.Player.rect.width = int(Load["Game.Player.rect.width"])
    Game.Player.Armor = int(Load["Game.Player.Armor"])
    Game.Player.Mana = int(Load["Game.Player.Mana"])
    Game.Player.LastY = int(Load["Game.Player.LastY"])
    Game.Player.YVector = float(Load["Game.Player.YVector"])
    Game.PositionPlayer = int(Load["Game.PositionPlayer"])
    Game.Player.Force.lastx = float(Load["Game.Player.Force.lastx"])
    Game.Player.Base_Gravity = float(Load["Game.Player.Base_Gravity"])
    Game.Monster.Base_Gravity = float(Load["Game.Monster.Base_Gravity"])
    Game.Player.Force.x = float(Load["Game.Player.Force.x"])
    Game.Player.CDR = float(Load["Game.Player.CDR"])
    Game.Player.AttackSpeed = float(Load["Game.Player.AttackSpeed"])
    Game.Player.CCHit = float(Load["Game.Player.CCHit"])
    Game.Player.CCSpell = float(Load["Game.Player.CCSpell"])
    Game.Player.CCDamage = float(Load["Game.Player.CCDamage"])
    Game.Player.Penetration = int(Load["Game.Player.Penetration"])
    Game.Player.ManaRegen = float(Load["Game.Player.ManaRegen"])
    Game.Player.XP_Multiplicator = float(Load["Game.Player.XP_Multiplicator"])
    Game.Player.Damage_Multiplicator = float(Load["Game.Player.Damage.Multiplicator"])

    Loading = LoadingScreen(Game, "I'm currently loading the mobs", Screen, FullLoading, Loading)
    for mob in Game.all_Monster:
        mob.rect.x -= Game.PositionPlayer - Replace
    Loading = LoadingScreen(Game, "I'm currently loading the plateforms", Screen, FullLoading, Loading)
    for plateform in Game.all_plateform:
        plateform.rect.x -= Game.PositionPlayer - Replace
    Loading = LoadingScreen(Game, "I'm currently loading your walls", Screen, FullLoading, Loading)
    for wall in Game.all_wall:
        wall.rect.x -= Game.PositionPlayer - Replace
    LoadingScreen(Game, "Your data has been loaded", Screen, FullLoading, Loading)
    Game.Sol.rect.x = 0
    return 0


def ImportOptions(Game):
    Options = open('Data/Options.txt', 'r')

    _ = Game.police1

    for line in Options:
        line.strip()
        print(line)
        exec(line)

    Options.close()


def OptionInterations(Game, Screen):

    for item in range(len(Game.Keys)):
        while Game.Keys[item][1]:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Game.Keys[item][2] = event.key
                    Game.Keys[item][1] = False

                if event.type == pygame.QUIT:
                    Game.InGame = False
                    Game.Lobby = False
                    Game.Pause = False
                    Game.running = False
                    pygame.quit()
                    quit()
                    break

            OptionPrinter(Game, Screen)
            MousePrinter(Screen, Game)
            pygame.display.flip()

            if not Game.Keys[item][1]:
                Options = open('Data/Options.txt', 'w')
                Options.write("Game.Keys = [[Game.UI.Option.Key1, False, " + str(Game.Keys[0][2]) +
                              "], [Game.UI.Option.Key2, False, " + str(Game.Keys[1][2]) +
                              "], [Game.UI.Option.Key3, False, " + str(Game.Keys[2][2]) +
                              "], [Game.UI.Option.Key4, False, " + str(Game.Keys[3][2]) +
                              "]]\nGame.Volume = [pygame.Rect(" + str((Game.Volume[2] - 0.03) * 500) +
                              " + 140, 275, 30, 60), False, " + str(Game.Volume[2]) + "]")
                Options.close()
                ImportOptions(Game)
        
        while Game.Volume[1]:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        Game.pressed[str(event.button)] = False
                        Game.Volume[1] = False

                if event.type == pygame.QUIT:
                    Game.InGame = False
                    Game.Lobby = False
                    Game.Pause = False
                    Game.running = False
                    pygame.quit()
                    quit()
                    break

            OptionPrinter(Game, Screen)
            MousePrinter(Screen, Game)
            pygame.display.flip()

            if 139 < Game.Mouse.rect.center[0] < 641:
                Game.Volume[0].x = Game.Mouse.rect.center[0] - 15
                Game.Volume[2] = round((Game.Mouse.rect.center[0] - 140) / 500, 2)
            elif 640 < Game.Mouse.rect.center[0]:
                Game.Volume[0].x = 625
                Game.Volume[2] = 1
            elif Game.Mouse.rect.center[0] < 140:
                Game.Volume[0].x = 125
                Game.Volume[2] = 0

            Music_Init(Game)

            if not Game.Volume[1]:
                Options = open('Data/Options.txt', 'w')
                Options.write("Game.Keys = [[Game.UI.Option.Key1, False, " + str(Game.Keys[0][2]) +
                              "], [Game.UI.Option.Key2, False, " + str(Game.Keys[1][2]) +
                              "], [Game.UI.Option.Key3, False, " + str(Game.Keys[2][2]) +
                              "], [Game.UI.Option.Key4, False, " + str(Game.Keys[3][2]) +
                              "]]\nGame.Volume = [pygame.Rect(" + str((Game.Volume[2] - 0.03) * 500) +
                              " + 140, 275, 30, 60), False, " + str(Game.Volume[2]) + "]")
                Options.close()
                ImportOptions(Game)
                Music_Init(Game)


""" ===  Music  === """


def Music_Init(Game):
    """Initialisation du module pygame.mixer -tremisabdoul"""
    pygame.mixer.music.set_volume(Game.Volume[2])
    print(pygame.mixer.music.get_volume())
    pygame.mixer.init()


def musicDANOARKI(Game):
    """Musique -tremisabdoul"""
    Timer = pygame.mixer.music.get_pos() / 1000.0

    if Timer + Game.MusicStart > Game.MusicLengh:
        pygame.mixer.music.rewind()
        Game.MusicStart = 0

    Game.MusicStart = Timer + Game.MusicStart

    pygame.mixer.music.load("Assets/Audio/Music/DANOARKI.mp3")
    Game.MusicLengh = 300
    pygame.mixer.music.play(-1, Game.MusicStart)


def musicDANOARKIOUT(Game):
    """Musique _tremisabdoul"""
    Timer = pygame.mixer.music.get_pos() / 1000.0
    if Timer + Game.MusicStart > Game.MusicLengh:
        pygame.mixer.music.rewind()
        Game.MusicStart = 0

    Game.MusicStart = Timer + Game.MusicStart

    pygame.mixer.music.load("Assets/Audio/Music/DANOARKIout.mp3")
    Game.MusicLengh = 300
    pygame.mixer.music.play(-1, Game.MusicStart)


"""
def initF():
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
                ],
                [  # Prepa spell
                    [  # (Prepa spell Right)
                        pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort.png")
                    ],
                    [  # ((Prepa spell Left))
                        pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort.png")
                    ]
                ],
                [  # Prepa spell jump
                    [  # (Prepa spell Right)
                        pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Jump.png")
                    ],
                    [  # ((Prepa spell Left))
                        pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Jump.png")
                    ]
                ],
                [  # Prepa spell fall
                    [  # (Prepa spell Right)
                        pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Fall.png")
                    ],
                    [  # ((Prepa spell Left))
                        pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Fall.png")
                    ]
                ],
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

    TilesPatern = {'Init':
                   'StepX, StepY = 0, 0',
                   '#':
                   'NewWall(Game, StepX, StepY)'
                   'StepX += 400',
                   '_':
                   'NewPlatform(Game, StepX, StepY)'
                   'StepX += 400',
                   ',':
                   'StepX = 0'
                   'StepY += 150',
                   '=':
                   'StepX = 0'
                   'StepY = 0'}
"""


print("/Scripts/Functions: Loaded")
