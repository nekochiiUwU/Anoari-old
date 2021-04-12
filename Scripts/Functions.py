
# Contient toutes les fonctions (pour ne pas envahir les autres fichiers) -tremisabdoul

import pygame
import os

print("/Scripts/Functions: Loading")


def Music_Init():
    """Initialisation du module pygame.mixer -tremisabdoul"""
    pygame.mixer.music.set_volume(0.4)
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


def Display():
    """Création de la fenètre -tremisabdoul"""

    pygame.init()
    pygame.display.set_caption("Anoari")
    size = (1280, 720)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    return screen


def Jump(Game):
    """Saut: [ Key: Space ] -tremisabdoul"""
    global booleanjump
    if Game.Player.SpeedY > -17 and Game.pressed.get(pygame.K_SPACE) and booleanjump:
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
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.MovementKey = True
        Game.Player.Move_Right(Game)

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.MovementKey = True
        Game.Player.Move_Left(Game)


def MousePrinter(Screen, Game):
    """Affichage de la sourie -tremisabdoul"""

    Game.Mouse.rect.center = pygame.mouse.get_pos()
    Screen.blit(Game.Mouse.image, Game.Mouse.rect)


def Printer(Screen, Game):
    """Fonction d'affichage: Elements in-game -tremisabdoul"""

    Game.Background.rect.x -= Game.Position
    Game.Sol.rect.x += Game.Position

    print(Game.Sol.rect)

    Screen.blit(Game.Background.image, Game.Background.rect)

    for Entity in Game.Entities:
        if Entity != Game.Player:
            Entity.rect.x -= Game.Position
            Screen.blit(Entity.image, Entity.rect)

    for Projectile in Game.Projectiles:
        Projectile.rect.x -= Game.Position
        Projectile.move(Game)
        Screen.blit(Projectile.image, Projectile.rect)

    Game.Particles.Print(Game, Screen)

    for Structure in Game.all_plateform, Game.all_wall:
        Structure.rect.x -= Game.Position
        if -250 < Structure.rect.x < 1280:
            Screen.blit(Structure.image, Structure.rect)

    if Game.pressed.get("3"):
        MousePrinter(Screen, Game)
        Game.Arm.print(Game, Screen)
    else:
        if Game.Player.Direction:
            Game.Mouse.rect.y = Game.Player.rect.y + 50
            Game.Mouse.rect.x = Game.Player.rect.x + 220
        else:
            Game.Mouse.rect.y = Game.Player.rect.y + 50
            Game.Mouse.rect.x = Game.Player.rect.x - 100

    Screen.blit(Game.Sol.image, Game.Sol.rect)

    Animation(Game)
    Screen.blit(Game.Player.image, Game.Player.rect)

    if Game.Frame % 2:
        Game.Particles.Add((Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'red', 6)
        Game.Particles.Add((Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'orangered', 6)
        Game.Particles.Add((Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'orangered4', 6)
        Game.Particles.Add((Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'red3', 6)

    if Game.ShowHitbox:
        for Object in Game.Entities, Game.all_wall, Game.all_plateform:
            Draw_rect(Screen, Game.Object)

    UIPrinter(Screen, Game)


# Print: -tremisabdoul
def UIPrinter(Screen, Game):
    """Fonction d'affichage: Elements d'interface in-game -tremisabdoul"""

    # Cree une couleur plus ou moins rouge en fonction des PV restants -tremisabdoul
    Color = (Game.Player.Pv / Game.Player.MaxPv) * 255
    LifeColor = [255, Color, Color]

    opti = str(round(Game.Player.Pv))
    opti = str(str(opti) + " / " + str(Game.Player.MaxPv) + " HP")
    opti = Game.police1.render(str(opti), True, LifeColor)
    Screen.blit(opti, (15 + Color / 50, 48 + Color / 50))

    opti1 = round((Game.Player.Pv / Game.Player.MaxPv) * 100)
    opti1 = opti1 * "|"
    opti1 = Game.police1.render(str(opti1), True, LifeColor)
    Screen.blit(opti1, (15 + Color / 50, 60 + Color / 50))

    if Game.ShowHitbox:
        jump = "Jump: " + str(Game.Player.SpeedY)
        jump = Game.police1.render(str(jump), True, (128, 255, 128))
        Screen.blit(jump, (15, 80))

        jump1 = round((Game.Player.SpeedY / 16) * 100)
        jump1 = -jump1 * "|"
        jump1 = Game.police1.render(str(jump1), True, (128, 255, 128))
        Screen.blit(jump1, (15, 100))

        # Permet de voir le nombre de frames a la seconde -tremisabdoul -tremisabdoul
        frame = 1
        fps = frame / Game.Tickchecker
        fps = "FPS : " + str(round(fps))
        printfps = Game.police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        y = 34
        for Entity in Game.Entities:
            Entity.YVectorblit = Game.police1.render("Y Vector checker: " + str(Entity.YVector), True, (100, 100, 200))
            Screen.blit(Entity.YVectorblit, (100, y))
            y += 10


def pauseblit(Screen, Game):
    """Fonction d'affichage: Elements de pause -tremisabdoul"""

    Screen.blit(Game.Background.image, Game.Background.rect)
    Screen.blit(Game.UI.baselayer, (0, 0))

    Screen.blit(Game.UI.resumebutton, Game.UI.resumebuttonrect)
    Screen.blit(Game.UI.savebutton, Game.UI.savebuttonrect)
    Screen.blit(Game.UI.settingsbutton, Game.UI.settingsbuttonrect)
    Screen.blit(Game.UI.quitbutton, Game.UI.quitbuttonrect)

    Game.Particles.Add(Game.Mouse.rect.center, 'white', 10)
    Game.Particles.Add(Game.Mouse.rect.center, 'grey', 10)
    Game.Particles.Add(Game.Mouse.rect.center, 'black', 10)
    Game.Particles.Print(Game, Screen)

    MousePrinter(Screen, Game)


def pause(Game, Screen):
    """ Loop de pause -tremisabdoul"""

    while Game.Pause:

        # Init du compteur d'FPS -tremisabdoul
        tick = Game.time()

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
                Game.Pause = False
                Game.running = False
                pygame.quit()

        # Affichage -tremisabdoul
        pauseblit(Screen, Game)
        pygame.display.flip()

        # Limiteur d'FPS
        FrameLimiter(Game, tick)


# Loop de Jeu: -tremisabdoul
def inGame(Game, Screen):
    """ Loop de Jeu -tremisabdoul"""

    while Game.InGame:
        """ ===== Frame Limiter ===== """
        tick = Game.time()
        Game.Frame += 1
        """ ===== Movements ===== """
        Movements(Game, Screen)
        """ ===== Camera ===== """
        SmoothCamera(Game)
        """ ===== Printer ===== """
        Printer(Screen, Game)
        """ ===== Affichage ===== """
        pygame.display.flip()
        """ ===== Key Inputs ===== """
        InGameKeys(Game, Screen)
        """ ===== Frame Limiter ===== """
        FrameLimiter(Game, tick)


def LobbyBlit(Screen, Game):
    """Fonction d'affichage: Elements du lobby -steven"""
    Screen.blit(Game.UI.lobbybackground, (0, 0))
    Screen.blit(Game.UI.lobby_loadbutton, Game.UI.lobby_loadbuttonrect)
    Screen.blit(Game.UI.lobby_playbutton, Game.UI.lobby_playbuttonrect)
    Screen.blit(Game.UI.lobby_quitbutton, Game.UI.lobby_quitbuttonrect)


def Lobby(Game, Screen):
    """Loop d'ecran d'acceuil -steven"""

    while Game.Lobby:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = Game.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Boutons souris enfonces -nekochii
                if Game.UI.lobby_playbuttonrect.collidepoint(event.pos):
                    Game.Click.play()
                    Game.InGame = True
                    Game.Lobby = False
                elif Game.UI.lobby_loadbuttonrect.collidepoint(event.pos):
                    Game.Click.play()
                    Game.Lobby = False
                    Game.SaveMenu = True
                    Game.SaveValue = 1
                elif Game.UI.lobby_quitbuttonrect.collidepoint(event.pos):
                    Game.Click.play()
                    Game.Running = False
                    pygame.quit()

            # Boutons souris enfonces -nekochii x tremisabdoul
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                Game.pressed[str(event.button)] = True
            # Boutons souris relaches -nekochii
            elif event.type == pygame.MOUSEBUTTONUP:
                Game.pressed[str(event.button)] = False

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

        # Permet de recuperer le nombre de frames a la seconde -tremisabdoul
        tickchecker = Game.time()
        tickchecker -= tick

        Game.UI.TitleMenuButtunDeplacement(Game)
        LobbyBlit(Screen, Game)

        MousePrinter(Screen, Game)

        while tickchecker < 0.016:
            tickchecker = Game.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))

        pygame.display.flip()


def Option(Game, Screen):
    while Game.Option:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = Game.time()

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

        # Permet de recuperer le nombre de frames a la seconde -tremisabdoul
        tickchecker = Game.time()
        tickchecker -= tick

        MousePrinter(Screen, Game)

        White = (255, 255, 255)
        Screen.fill((0, 0, 0))
        pygame.draw.rect(Screen, White, pygame.Rect(600, 200, 100, 60),  2)

        # Affichage du necessaire pour le texte des Options -steven
        Texte('Resolution : ', police2, (255, 255, 255), Screen, 100, 100)
        Texte('Volume : ', police2, (255, 255, 255), Screen, 100, 225)
        Texte('Controles : ', police2, (255, 255, 255), Screen, 100, 350)

        pygame.display.flip()

        while tickchecker < 0.017:
            tickchecker = Game.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))


# Fonction du menu des sauvegardes -steven
def SaveMenu(Game, Screen):
    while Game.SaveMenu:
        # Initialisation du compteur de temps pour limiter les fps -tremisabdoul
        tick = Game.time()

        # Position des rectangles de sauvegarde -steven
        SaveButton1 = pygame.Rect(125, 50, 500, 100)
        SaveButton2 = pygame.Rect(125, 200, 500, 100)
        SaveButton3 = pygame.Rect(125, 350, 500, 100)

        # Liste regroupant les noms des sauvegardes
        State = ["Save/save1.csv", "Save/save2.csv", "Save/save3.csv", "Save/save4.csv", "Save/save5.csv"]
        # SaveState = 0

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

            # Sauvegarde des donnees du joueurs (SaveValue == 2 signifie qu'il est rentré par le menu pause) -steven
            elif event.type == pygame.MOUSEBUTTONDOWN and Game.SaveValue == 2:
                if SaveButton1.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[0]
                    Data_Save(Game, Screen, police1, SaveState)

                elif SaveButton2.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[1]
                    Data_Save(Game, Screen, police1, SaveState)

                elif SaveButton3.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[2]
                    Data_Save(Game, Screen, police1, SaveState)

            # Chargement des donnees du joueurs (SaveValue == 1 signifie qu'il est rentré par le menu d'accueil) -steven
            elif event.type == pygame.MOUSEBUTTONDOWN and Game.SaveValue == 1:
                if SaveButton1.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[0]
                    Data_Load(Game, Screen, police1, SaveState)
                    Game.SaveMenu = False
                    Game.InGame = True

                elif SaveButton2.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[1]
                    Data_Load(Game, Screen, police1, SaveState)
                    Game.SaveMenu = False
                    Game.InGame = True

                elif SaveButton3.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[2]
                    Data_Load(Game, Screen, police1, SaveState)
                    Game.SaveMenu = False
                    Game.InGame = True

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
            if event.type == pygame.QUIT:
                Game.SaveValue = 0
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.SaveMenu = False
                Game.running = False
                pygame.quit()

        # Permet de recuperer le nombre de frames a la seconde -tremisabdoul
        tickchecker = Game.time()
        tickchecker -= tick

        MousePrinter(Screen, Game)

        White = (255, 255, 255)
        Screen.fill((0, 0, 0))

        # Creation des rectangles -steven
        Rectangle(Screen, White, SaveButton1, 2)
        Rectangle(Screen, White, SaveButton2, 2)
        Rectangle(Screen, White, SaveButton3, 2)

        pygame.display.flip()

        while tickchecker < 0.017:
            tickchecker = Game.time()
            tickchecker -= tick

        fps = 1 / tickchecker
        fps = "FPS : " + str(round(fps))
        # Transforme une variable en composent graphique -tremisabdoul
        printfps = police1.render(str(fps), True, (255, 255, 255))
        Screen.blit(printfps, (6, 34))


# Fonction du texte -steven
def Texte(text, color, Screen, x, y):
    Texte_Contenu = police2.render(text, 1, color)
    Texte_Rect = (x, y)
    Screen.blit(Texte_Contenu, Texte_Rect)


# Fonction des rectangles -steven
def Rectangle(Screen, color, rect, border_radius):
    pygame.draw.rect(Screen, color, rect, border_radius)


# TKT -tremisabdoul
def Data_Save(Game, Screen, SaveState):

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

    Loading = LoadingScreen("I'm actually saving your data", Screen, police1, FullLoading, Loading)
    text_file = open(SaveState, "w+", newline="")
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
def Data_Load(Game, Screen, SaveState):

    Loading = 0
    FullLoading = 88
    Replace = Game.PositionPlayer
    import csv

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    file = SaveState
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
    Game.Player.rect.x = int(Load["Game.Player.rect.x"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.y = int(Load["Game.Player.rect.y"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.height = int(Load["Game.Player.rect.height"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.rect.width = int(Load["Game.Player.rect.width"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Armor = int(Load["Game.Player.Armor"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Mana = int(Load["Game.Player.Mana"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.LastY = int(Load["Game.Player.LastY"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.YVector = float(Load["Game.Player.YVector"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.PositionPlayer = int(Load["Game.PositionPlayer"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Force.lastx = float(Load["Game.Player.Force.lastx"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Base_Gravity = float(Load["Game.Player.Base_Gravity"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Monster.Base_Gravity = float(Load["Game.Monster.Base_Gravity"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Force.x = float(Load["Game.Player.Force.x"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.CDR = float(Load["Game.Player.CDR"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.AttackSpeed = float(Load["Game.Player.AttackSpeed"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.CCHit = float(Load["Game.Player.CCHit"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.CCSpell = float(Load["Game.Player.CCSpell"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.CCDamage = float(Load["Game.Player.CCDamage"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Penetration = int(Load["Game.Player.Penetration"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.ManaRegen = float(Load["Game.Player.ManaRegen"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.XP_Multiplicator = float(Load["Game.Player.XP_Multiplicator"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)
    Game.Player.Damage_Multiplicator = float(Load["Game.Player.Damage.Multiplicator"])
    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for mob in Game.all_Monster:
        mob.rect.x -= Game.PositionPlayer - Replace
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for plateform in Game.all_plateform:
        plateform.rect.x -= Game.PositionPlayer - Replace
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    for wall in Game.all_wall:
        wall.rect.x -= Game.PositionPlayer - Replace
        Loading = LoadingScreen("I'm actually loading your data", Screen, police1, FullLoading, Loading)

    Game.Sol.rect.x = 0
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
    if Game.PrepaSpell:
        if Game.Player.YVector:
            if Game.Player.YVector < 0:
                PrepaSpellFallAnimation(Game)
            else:
                PrepaSpellJumpAnimation(Game)
        elif Game.Player.MovementKey:
            PrepaSpellRunAnimation(Game)
        else:
            PrepaSpellAnimation(Game)

    elif Game.Player.YVector:
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
    if Game.Player.Direction:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump2.png")
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump2.png")


# TKT -tremisabdoul
def JumpAnimation(Game):
    if Game.Player.Direction:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump1.png")
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump1.png")


# TKT -tremisabdoul
def RunAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Run/Run1.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Run/Run2.png")
    else:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Run/Run1.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Run/Run2.png")


# TKT -tremisabdoul
def StandAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp2.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
    else:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/resp2.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/resp1.png")


# TKT -tremisabdoul
def PrepaSpellJumpAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Jump.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Jump.png")


# TKT -tremisabdoul
def PrepaSpellFallAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Fall.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Fall.png")


# TKT -tremisabdoul
def PrepaSpellRunAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort marche.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort marche 2.png")
    else:
        if Game.Frame % 4 == 0:
            if Game.ActualFrame <= 0:
                Game.ActualFrame = 1
                Game.Player.image = pygame.image.load\
                ("Assets/Visual/Mystique/Left/Spells/mystique prepa sort marche.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = pygame.image.load\
                ("Assets/Visual/Mystique/Left/Spells/mystique prepa sort marche 2.png")


# TKT -tremisabdoul
def PrepaSpellAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort.png")


# TKT -tremisabdoul
def BackgroundScroll(Game):
    checker = Game.PositionPlayer % 1280
    if -10 < checker < 10:
        Game.Background.rect.midtop = 640 - checker, 0


def LoadingScreen(Message, Screen, Ratio, Loading):
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


def NewPlatform(Game, x, y):
    from Scripts.Classes import Plateform
    Plateform = Plateform()
    Plateform.rect.x, Plateform.rect.y = x * 250, y * 150 + 130
    Game.all_plateform.add(Plateform)
    Game.PlateformNumber += 1


def NewWall(Game, x, y):
    from Scripts.Classes import Wall
    Wall = Wall()
    Wall.rect.x, Wall.rect.y, Wall.rect.height, Wall.rect.width = x * 250, y * 150, 150, 250
    Game.all_wall.add(Wall)
    Game.WallNumber += 1


def Movements(Game, Screen):
    # Fonction de deplacement gauche / droite -tremisabdoul
    global booleanjump
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

    # Active le Jump() -tremisabdoul
    if Game.pressed.get(pygame.K_SPACE) \
            and Game.Player.check_collisions(Game.Player, Game.all_plateform) \
            and Game.Player.YVector == 0:

        global booleanjump
        Game.Player.SpeedY = -5
        booleanjump = 1
        Jump(Game)
    elif Game.Player.SpeedY:
        Jump(Game)

    for Entity in Game.Entities:
        Game.Player.Force.Gravity(Game, Entity)
        Entity.YVector = Entity.LastY - Entity.rect.y

    # Deplacements de player -tremisabdoul
    # Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Position = Game.Player.Force.AccelerationFunctionX()
    for Target in Game.Entities:
        Collide = Game.Player.check_collisions(Target, Game.all_wall)

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


def InGameKeys(Game, Screen):
    # Check les input et instances -tremisabdoul
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
                Lunch_Projectile(Game)
                print("Left Click (None)")
            elif event.button == 2:
                print("Middle Click (Hitbox + print(Game.PlayerPosition))")
                # Game.data.stop()
                # Game.data.play()
                Game.ShowHitbox = not Game.ShowHitbox
            elif event.button == 3:
                print("Right Click (Mode VisÃ©e)")
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
            Game.InGame = False
            Game.Lobby = False
            Game.Pause = False
            Game.running = False
            pygame.quit()
            quit()
            break


def FrameLimiter(Game, tick):
    # Permet d'avoir des frames regulieres -tremisabdoul
    Game.Tickchecker = Game.time()
    Game.Tickchecker -= tick
    if Game.ShowHitbox:
        print("\n Player Posion: ", Game.PositionPlayer)
        try:
            global Test
            start = Game.time()
            Test = Game.time() - start
            print("",
                  round((Game.Tickchecker - Test) / 0.00017), "\t% of 60 FPS: Framerate without Test\n",
                  round(Game.Tickchecker / 0.00017), "\t% of 60 FPS: Framerate\n",
                  round(Test / 0.00017), "\t% of 60 FPS : Test\n")
        except:
            Test = 0

    while Game.Tickchecker < 0.017:
        Game.Tickchecker = Game.time()
        Game.Tickchecker -= tick


def Paterns(Game, NewWall, NewPlatform):

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
        print(Patern)
        Game.Paterns[Patern] = Game.Paterns[Patern].split(":")
        print("\nID Game.Paterns[", Patern, "] :  ", Game.Paterns[Patern], ": ", sep='')

        for item in range(len(Game.Paterns[Patern])):
            if 2 <= item <= 6:
                Game.Paterns[Patern][item] = ",".join(Game.Paterns[Patern][item])
                Game.Paterns[Patern][item] = Game.Paterns[Patern][item].split(",")
            print("\tID Game.Paterns[", Patern, "][", item, "] :  ", Game.Paterns[Patern][item], "\n", sep='')
            if isinstance(Game.Paterns[Patern][item], list):
                for Chr in range(len(Game.Paterns[Patern][item])):
                    print("\t\tID Game.Paterns[", Patern, "][", item, "][", Chr, "] :  ",
                          Game.Paterns[Patern][item][Chr], sep='')

    Game.Grid = {"xTiles": len(Game.Paterns[0][2]),
                 "yTiles": len(Game.Paterns[0]),
                 "width": 250,
                 "height": 150,
                 "x": 0,
                 "y": 0}

    for _ in range(30):
        from Scripts.Classes import Patern
        Patern = Patern()
        Patern.Init(Game, NewWall, NewPlatform)
        Game.ApplyedPatens.add(Patern)


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


def SmoothCamera(Game):
    Game.Player.LastX = Game.Player.rect.x - 350
    Game.lastPosition = Game.Position
    Game.Player.rect.x = 350
    # Information Smooth Cam:
    #   Valeur Numerique n°2: Vitesse de camera ├──────────────────────┬┬┐ (y > 1)
    #   Valeur Numerique n°1: Décalage max du Player ├──────────┬┬┐    │││ (x > 1)
    #   ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬  ▼▼▼    ▼▼▼
    Game.Player.rect.x += (Game.Position + (Game.Player.LastX / 1.9) / 1.5)


def Lunch_Projectile(Game):
    from Scripts.Classes import Projectile
    Game.Projectiles.add(Projectile(Game))


print("/Scripts/Functions: Loaded")
