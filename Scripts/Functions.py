
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

    Screen.blit(Game.Background.image, Game.Background.rect)

    for Entity in Game.Entities:
        if Entity != Game.Player:
            Entity.rect.x -= Game.Position
            Screen.blit(Entity.image, Entity.rect)
            Entity.Life(Screen, Game)

    for Projectile in Game.Projectiles:
        Projectile.rect.x -= Game.Position
        Projectile.move(Game)
        Screen.blit(Projectile.image, Projectile.rect)

    Game.Particles.Print(Game, Screen)

    for Structure in Game.all_plateform:
        Structure.rect.x -= Game.Position
        if -250 < Structure.rect.x < 1280:
            Screen.blit(Structure.image, Structure.rect)

    for Structure in Game.all_wall:
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
        Game.Particles.Add(Game, (Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'red', 6)
        Game.Particles.Add(Game, (Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'orangered', 6)
        Game.Particles.Add(Game, (Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'orangered4', 6)
        Game.Particles.Add(Game, (Game.Player.rect.center[0] - 35, Game.Player.rect.center[1] - 20), 'red3', 6)

    if Game.ShowHitbox:
        for Object in Game.Entities:
            Draw_rect(Screen, Object)

        for Object in Game.all_wall:
            Draw_rect(Screen, Object)

        for Object in Game.all_plateform:
            Draw_rect(Screen, Object)

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

    Game.Particles.Add(Game, Game.Mouse.rect.center, 'white', 10)
    Game.Particles.Add(Game, Game.Mouse.rect.center, 'grey', 10)
    Game.Particles.Add(Game, Game.Mouse.rect.center, 'black', 10)
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
        """ ===== Printer ===== """
        Printer(Screen, Game)
        """ ===== Key Inputs ===== """
        InGameKeys(Game, Screen)
        """ ===== Frame Limiter ===== """
        FrameLimiter(Game, Screen)
        """ ===== Affichage ===== """
        pygame.display.flip()
        """Test Network"""
        Slimeposition = Game.Network.read_pos(Game.Network.send(Game.Network.make_Data((Game.Monster.rect.x, Game.Monster.rect.y), "tuple")))
        print(Slimeposition)
        Game.Monster.rect.x = Slimeposition[0]
        Game.Monster.rect.y = Slimeposition[1]

def LobbyBlit(Screen, Game):
    """Affichage des Elements du lobby -steven"""
    Screen.blit(Game.UI.lobbybackground, (0, 0))
    Screen.blit(Game.UI.lobby_loadbutton, Game.UI.lobby_loadbuttonrect)
    Screen.blit(Game.UI.lobby_playbutton, Game.UI.lobby_playbuttonrect)
    Screen.blit(Game.UI.lobby_quitbutton, Game.UI.lobby_quitbuttonrect)
    MousePrinter(Screen, Game)


def Lobby(Game, Screen):
    """Loop d'ecran d'acceuil -steven"""

    while Game.Lobby:
        tick = Game.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_F11):
                    pygame.display.toggle_fullscreen()

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                Game.pressed[str(event.button)] = True

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

            elif event.type == pygame.MOUSEBUTTONUP:
                Game.pressed[str(event.button)] = False

            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

        Game.UI.TitleMenuButtunDeplacement(Game)

        LobbyBlit(Screen, Game)

        tickchecker = Game.time()
        tickchecker -= tick

        if tickchecker:
            fps = 1 / tickchecker
            fps = "FPS : " + str(round(fps))
        else:
            fps = "Il n'as meme pas eu le temps de compter..."

        Texte(Game.police1, fps, (255, 255, 255), Screen, (6, 34))

        pygame.display.flip()


def OptionPrinter(Game, Screen):
    """Affichage des options -steven"""
    White = (255, 255, 255)
    Screen.fill((0, 0, 0))
    pygame.draw.rect(Screen, White, pygame.Rect(600, 200, 100, 60), 2)

    Texte(Game.police2, 'Resolution : ', (255, 255, 255), Screen, (100, 100))
    Texte(Game.police2, 'Volume : ', (255, 255, 255), Screen, (100, 225))
    Texte(Game.police2, 'Controles : ', (255, 255, 255), Screen, (100, 350))

    MousePrinter(Screen, Game)


def Option(Game, Screen):
    """Loop des options -steven"""
    while Game.Option:

        tick = Game.time()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                Game.pressed[event.key] = True

                if Game.pressed.get(pygame.K_ESCAPE):
                    Game.Pause = True
                    Game.Option = False

            elif event.type == pygame.KEYUP:
                Game.pressed[event.key] = False

            if event.type == pygame.QUIT:
                Game.InGame = False
                Game.Lobby = False
                Game.Pause = False
                Game.running = False
                pygame.quit()

        OptionPrinter(Game, Screen)

        tickchecker = Game.time()
        tickchecker -= tick

        if tickchecker:
            fps = 1 / tickchecker
            fps = "FPS : " + str(round(fps))
        else:
            fps = "Il n'as meme pas eu le temps de compter..."

        Texte(Game.police1, fps, (255, 255, 255), Screen, (6, 34))

        pygame.display.flip()


def SaveMenuPrinter(Game, Screen, SaveButton1, SaveButton2, SaveButton3):
    """Affichage dans la Loop SaveMenu -steven"""
    MousePrinter(Screen, Game)

    White = (255, 255, 255)
    Screen.fill((0, 0, 0))

    # Creation des rectangles -steven
    Rectangle(Screen, White, SaveButton1, 2)
    Rectangle(Screen, White, SaveButton2, 2)
    Rectangle(Screen, White, SaveButton3, 2)


def SaveMenu(Game, Screen):
    """Loop de menu de save -steven"""

    SaveButton1 = pygame.Rect(125, 50, 500, 100)
    SaveButton2 = pygame.Rect(125, 200, 500, 100)
    SaveButton3 = pygame.Rect(125, 350, 500, 100)

    while Game.SaveMenu:
        tick = Game.time()

        State = ["Save/save1.csv", "Save/save2.csv", "Save/save3.csv", "Save/save4.csv", "Save/save5.csv"]

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
                    Data_Save(Game, Screen, SaveState)

                elif SaveButton2.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[1]
                    Data_Save(Game, Screen, SaveState)

                elif SaveButton3.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[2]
                    Data_Save(Game, Screen, SaveState)

            # Chargement des donnees du joueurs (SaveValue == 1 signifie qu'il est rentré par le menu d'accueil) -steven
            elif event.type == pygame.MOUSEBUTTONDOWN and Game.SaveValue == 1:
                if SaveButton1.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[0]
                    Data_Load(Game, Screen, SaveState)
                    Game.SaveMenu = False
                    Game.InGame = True

                elif SaveButton2.collidepoint(event.pos):
                    Game.Click.play()
                    SaveState = State[1]
                    Data_Load(Game, Screen, SaveState)
                    Game.SaveMenu = False
                    Game.InGame = True

                elif SaveButton3.collidepoint(event.pos):
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
                Game.Lobby = False
                Game.Pause = False
                Game.SaveMenu = False
                Game.running = False
                pygame.quit()

        tickchecker = Game.time()
        tickchecker -= tick

        if tickchecker:
            fps = 1 / tickchecker
            fps = "FPS : " + str(round(fps))
        else:
            fps = "Il n'as meme pas eu le temps de compter..."

        Texte(Game.police1, fps, (255, 255, 255), Screen, (6, 34))

        SaveMenuPrinter(Game, Screen, SaveButton1, SaveButton2, SaveButton3)

        pygame.display.flip()


def Data_Save(Game, Screen, SaveState):
    """Save des données -tremisabdoul"""

    Loading = 0
    FullLoading = 4

    import csv

    Loading = LoadingScreen(Game, "I'm actually loading your data", Screen, FullLoading, Loading)

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

    Loading = LoadingScreen(Game, "I'm actually opening your data file", Screen, FullLoading, Loading)

    text_file = open(SaveState, "w+", newline="")

    Loading = LoadingScreen(Game, "I'm actually writing your data file ()", Screen, FullLoading, Loading)

    with text_file:
        Writer = csv.writer(text_file, quoting=0)
        Writer.writerows(Datalist.items())

    text_file.close()
    del csv

    LoadingScreen(Game, "I saved your data", Screen, FullLoading, Loading)

    return 0


def Data_Load(Game, Screen, SaveState):
    """Load des données -tremisabdoul"""

    Loading = 0
    FullLoading = 7
    Replace = Game.PositionPlayer
    import csv

    Loading = LoadingScreen(Game, "I'm actually opening your data file", Screen, FullLoading, Loading)

    file = SaveState
    CSV_file = csv.DictReader(open(file, 'r'))
    Load = {}

    Loading = LoadingScreen(Game, "I'm actually reading your data file", Screen, FullLoading, Loading)

    for lines in CSV_file:
        Load[lines["Variable"]] = lines["Value"]

    Loading = LoadingScreen(Game, "I'm actually loading your data", Screen, FullLoading, Loading)

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

    Loading = LoadingScreen(Game, "I'm actually loading the mobs", Screen, FullLoading, Loading)
    for mob in Game.all_Monster:
        mob.rect.x -= Game.PositionPlayer - Replace
    Loading = LoadingScreen(Game, "I'm actually loading the plateforms", Screen, FullLoading, Loading)
    for plateform in Game.all_plateform:
        plateform.rect.x -= Game.PositionPlayer - Replace
    Loading = LoadingScreen(Game, "I'm actually loading your walls", Screen, FullLoading, Loading)
    for wall in Game.all_wall:
        wall.rect.x -= Game.PositionPlayer - Replace
    LoadingScreen(Game, "Your data has been loaded", Screen, FullLoading, Loading)
    Game.Sol.rect.x = 0
    return 0


def ReScale(Game, Screen):
    """PAS FINI    Rescale Trop la flemme le le finir je vais le faire vous inquétez pas -tremisabdoul    PAS FINI"""
    Game.DataX = pygame.Surface.get_width(Screen)
    Game.DataY = pygame.Surface.get_height(Screen)
    Game.Player.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
    Game.Background.image = pygame.transform.scale(Game.Background.image,
                                                   (Game.Rescale(Game.Background.image.get_width(), "X"),
                                                    Game.Rescale(Game.Background.image.get_height(), "Y")))
    Game.Player.image = pygame.transform.scale(Game.Player.image,
                                               (Game.Rescale(Game.Player.image.get_width(), "X"),
                                                Game.Rescale(Game.Player.image.get_height(), "Y")))


def Animation(Game):
    """Animations (base par tremisabdoul) (PrepaSpell par nekochii) (Déssinées par nekochii)"""
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


def FallAnimation(Game):
    if Game.Player.Direction:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump2.png")
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump2.png")


def JumpAnimation(Game):
    if Game.Player.Direction:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Jump/Jump1.png")
    else:
        Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Jump/Jump1.png")


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


def PrepaSpellJumpAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Jump.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Jump.png")


def PrepaSpellFallAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort Fall.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort Fall.png")


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
                Game.Player.image = \
                    pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort marche.png")
            elif Game.ActualFrame >= 1:
                Game.ActualFrame = 0
                Game.Player.image = \
                    pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort marche 2.png")


def PrepaSpellAnimation(Game):
    if Game.Player.Direction:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Spells/mystique prepa sort.png")
    else:
        if Game.Frame % 4 == 0:
            Game.Player.image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/mystique prepa sort.png")


def BackgroundScroll(Game):
    """Déplacement du Background -tremisabdoul"""
    checker = Game.PositionPlayer % 1280
    if -10 < checker < 10:
        Game.Background.rect.midtop = 640 - checker, 0


def LoadingScreen(Game, Message, Screen, Ratio, Loading):
    """Affichage d'un écran de chargement -tremisabdoul"""
    Loading += 1
    Screen.fill((0, 0, 0))

    image = pygame.image.load("Assets/Visual/UI/Load.png")
    rect = image.get_rect()
    image = pygame.transform.scale(image, (int(Loading / Ratio * pygame.Surface.get_rect(Screen).width/2),
                                           int(pygame.Surface.get_rect(Screen).height/40)))
    rect = image.get_rect(center=rect.center)
    rect.center = pygame.Surface.get_rect(Screen).center
    Screen.blit(image, (rect.x, rect.y))

    Texte(Game.police1, "Please Wait: " + str((Loading / Ratio) * 100) + "%", (255, 255, 255),
          Screen, (pygame.Surface.get_rect(Screen).width-512, pygame.Surface.get_rect(Screen).height/4))

    Texte(Game.police1, Message, (255, 255, 255), Screen,
          (pygame.Surface.get_rect(Screen).width-512, pygame.Surface.get_rect(Screen).height/3))

    pygame.display.flip()

    return Loading


def Draw_rect(Screen, Target):
    """Affiche le canevas / la HitBox de l'élément appellé -tremisabdoul"""
    pygame.draw.lines(Screen, (200, 150, 100), True, (
        Target.rect.midbottom, Target.rect.midtop, Target.rect.topleft, Target.rect.bottomleft, Target.rect.bottomright,
        Target.rect.topright, Target.rect.topleft, Target.rect.midleft, Target.rect.midright, Target.rect.bottomright))


def NewPlatform(Game, x, y):
    """Création d'une plateforme -tremisabdoul"""
    from Scripts.Classes import Plateform
    Plateform = Plateform()
    Plateform.rect.x, Plateform.rect.y = x * 250, y * 150 + 130
    Game.all_plateform.add(Plateform)
    Game.PlateformNumber += 1


def NewWall(Game, x, y):
    """Création d'un mur -tremisabdoul"""
    from Scripts.Classes import Wall
    Wall = Wall()
    Wall.rect.x, Wall.rect.y, Wall.rect.height, Wall.rect.width = x * 250, y * 150, 150, 250
    Game.all_wall.add(Wall)
    Game.WallNumber += 1


def Movements(Game):
    """Contiens tout les mouvements ingame -tremisabdoul"""
    global booleanjump

    DeplacementX(Game)

    for Entity in Game.Entities:
        Entity.LastY = Entity.rect.y

    for Monster in Game.all_Monster:
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

    if Game.pressed.get(pygame.K_SPACE) \
            and Game.Player.check_collisions(Game.Player, Game.all_plateform) \
            and Game.Player.YVector == 0:
        Game.Player.SpeedY = -5
        booleanjump = 1
        Jump(Game)

    elif Game.Player.SpeedY:
        Jump(Game)

    for Entity in Game.Entities:
        Game.Player.Force.Gravity(Game, Entity)
        Entity.YVector = Entity.LastY - Entity.rect.y

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


def FrameLimiter(Game, Screen):
    """Limiteur de FPS -tremisabdoul"""
    Game.Tickchecker = Game.time()
    Game.Tickchecker -= Game.Tick
    if Game.ShowHitbox:
        print("\n Player Posion: ", Game.PositionPlayer)
        try:
            start = Game.time()
            Test = Game.time() - start
            TestL1 = str(round((Game.Tickchecker - Test) / 0.00017)) + "    % of 60 FPS: Framerate without Test"
            TestL2 = str(round(Game.Tickchecker / 0.00017)) + "    % of 60 FPS: Framerate"
            TestL3 = str(round(Test / 0.00017)) + "    % of 60 FPS : Test"
            Texte(Game.police1, TestL1, (255, 255, 255), Screen, (1000, 20))
            Texte(Game.police1, TestL2, (255, 255, 255), Screen, (1000, 40))
            Texte(Game.police1, TestL3, (255, 255, 255), Screen, (1000, 60))
        finally:
            Test = 0

    while Game.Tickchecker < 0.017:
        Game.Tickchecker = Game.time()
        Game.Tickchecker -= Game.Tick


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


def SmoothCamera(Game):
    """Mouvements de Caméra -tremisabdoul"""
    Game.Player.LastX = Game.Player.rect.x - 350
    Game.lastPosition = Game.Position
    Game.Player.rect.x = 350
    # Information Smooth Cam:
    #   Valeur Numerique n°2: Vitesse de camera ├──────────────────────┬┬┐ (y > 1)
    #   Valeur Numerique n°1: Décalage max du Player ├──────────┬┬┐    │││ (x > 1)
    #   ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬  ▼▼▼    ▼▼▼
    Game.Player.rect.x += (Game.Position + (Game.Player.LastX / 1.9) / 1.5)


def Lunch_Projectile(Game):
    """Lancement de Projectiles -tremisabdoul"""
    from Scripts.Classes import Projectile
    Game.Projectiles.add(Projectile(Game))


def Texte(Police, text, color, Screen, Position):
    """Creation de texte -steven"""
    Texte_Contenu = Police.render(text, 1, color)
    Screen.blit(Texte_Contenu, Position)


def Rectangle(Screen, color, rect, border_radius):
    """Creation de rectangle -steven"""
    pygame.draw.rect(Screen, color, rect, border_radius)


def Paterns(Game, NewWall, NewPlatform):
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


print("/Scripts/Functions: Loaded")
