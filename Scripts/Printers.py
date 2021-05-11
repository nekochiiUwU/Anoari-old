import pygame

""" ===  Priters  === """


def Printer(Screen, Game):
    """Fonction d'affichage: Elements in-game -tremisabdoul"""

    Game.Background.rect.x -= Game.Position
    Screen.blit(Game.Background.image, Game.Background.rect)

    PrintProjectiles(Game, Screen)

    PrintEntities(Game, Screen)

    PrintPreMade(Game, Screen)

    Game.Particles.Print(Game, Screen)

    PrintStructures(Game, Screen)

    PrintMouse3Condition(Game, Screen)

    if Game.ShowHitbox:
        ShowHitbox(Game, Screen)


def LobbyBlit(Screen, Game):
    """Affichage des Elements du lobby -steven"""
    Screen.blit(Game.UI.Lobby.background, (0, 0))
    Screen.blit(Game.UI.Lobby.loadbutton, Game.UI.Lobby.loadbuttonrect)
    Screen.blit(Game.UI.Lobby.playbutton, Game.UI.Lobby.playbuttonrect)
    Screen.blit(Game.UI.Lobby.quitbutton, Game.UI.Lobby.quitbuttonrect)
    MousePrinter(Screen, Game)


def OptionPrinter(Game, Screen):
    """Affichage des options -steven"""
    Screen.fill((0, 0, 0))

    for item in Game.Keys:
        if not 97 <= item[2] <= 122 and not 48 <= item[2] <= 57 and not item[2] == 32:
            item[2] = 0

    K1Image = Game.UI.Option.Keys[Game.Keys[0][2]]
    K2Image = Game.UI.Option.Keys[Game.Keys[1][2]]
    K3Image = Game.UI.Option.Keys[Game.Keys[2][2]]
    K4Image = Game.UI.Option.Keys[Game.Keys[3][2]]


    Screen.blit( K1Image, Game.UI.Option.Key1)
    Screen.blit( K2Image, Game.UI.Option.Key2)
    Screen.blit( K3Image, Game.UI.Option.Key3)
    Screen.blit( K4Image, Game.UI.Option.Key4)

    Key = Game.police1.render("Jump", 1, (200, 200, 200))
    Screen.blit(Key, (Game.UI.Option.Key1[0] + int(62.5 - Key.get_width() / 2), Game.UI.Option.Key1[1] + 130))

    Key = Game.police1.render("Left", 1, (200, 200, 200))
    Screen.blit(Key, (Game.UI.Option.Key2[0] + int(62.5 - Key.get_width() / 2), Game.UI.Option.Key2[1] + 130))

    Key = Game.police1.render("Right", 1, (200, 200, 200))
    Screen.blit(Key, (Game.UI.Option.Key3[0] + int(62.5 - Key.get_width() / 2), Game.UI.Option.Key3[1] + 130))

    Key = Game.police1.render("Trash", 1, (200, 200, 200))
    Screen.blit(Key, (Game.UI.Option.Key4[0] + int(62.5 - Key.get_width() / 2), Game.UI.Option.Key4[1] + 130))


    Texte(Game.police2, 'Resolution : ', (255, 255, 255), Screen, (100, 100))
    Texte(Game.police2, 'Volume : ', (255, 255, 255), Screen, (100, 225))
    Texte(Game.police2, 'Controles : ', (255, 255, 255), Screen, (100, 350))

    MousePrinter(Screen, Game)


def pauseblit(Screen, Game):
    """Fonction d'affichage: Elements de pause -tremisabdoul"""

    Screen.blit(Game.Background.image, Game.Background.rect)
    Screen.blit(Game.UI.baselayer, (0, 0))

    Screen.blit(Game.UI.resumebutton, Game.UI.resumebuttonrect)
    Screen.blit(Game.UI.savebutton, Game.UI.savebuttonrect)
    Screen.blit(Game.UI.settingsbutton, Game.UI.settingsbuttonrect)
    Screen.blit(Game.UI.quitbutton, Game.UI.quitbuttonrect)

    Game.Particles.Add(Game, Game.Mouse.rect.center, 'white', 5)
    Game.Particles.Add(Game, Game.Mouse.rect.center, 'grey', 5)
    Game.Particles.Add(Game, Game.Mouse.rect.center, 'black', 5)
    Game.Particles.Print(Game, Screen)

    MousePrinter(Screen, Game)


def SaveMenuPrinter(Game, Screen, SaveButton1, SaveButton2, SaveButton3):
    """Affichage dans la Loop SaveMenu -steven"""
    MousePrinter(Screen, Game)

    White = (255, 255, 255)
    Screen.fill((0, 0, 0))

    # Creation des rectangles -steven
    Rectangle(Screen, White, SaveButton1, 2)
    Rectangle(Screen, White, SaveButton2, 2)
    Rectangle(Screen, White, SaveButton3, 2)


""" ===  Print Tools  === """


def Texte(Police, text, color, Screen, Position):
    """Creation de texte -steven"""
    Texte_Contenu = Police.render(text, 1, color)
    Screen.blit(Texte_Contenu, Position)


def Rectangle(Screen, color, rect, border_radius):
    """Creation de rectangle -steven"""
    pygame.draw.rect(Screen, color, rect, border_radius)


def ShowHitbox(Game, Screen):
    for Object in Game.Entities:
        Draw_rect(Screen, Object)

    for Object in Game.all_wall:
        Draw_rect(Screen, Object)

    for Object in Game.all_plateform:
        Draw_rect(Screen, Object)

    for Object in Game.Projectiles:
        Draw_rect(Screen, Object)


def MousePrinter(Screen, Game):
    """Affichage de la sourie -tremisabdoul"""
    Game.Mouse.rect.center = pygame.mouse.get_pos()
    Screen.blit(Game.Mouse.image, Game.Mouse.rect)


def PrintMouse3Condition(Game, Screen):

    if Game.pressed.get("3"):
        Game.Player.Orb(Game)
        Game.Arm.print(Game, Screen)
        Animation(Game)
        Screen.blit(Game.Player.image, Game.Player.rect)
        UIPrinter(Screen, Game)
        MousePrinter(Screen, Game)
    else:
        Animation(Game)
        Screen.blit(Game.Player.image, Game.Player.rect)
        UIPrinter(Screen, Game)


def PrintEntities(Game, Screen):
    for Entity in Game.Entities:
        if Entity != Game.Player:
            Entity.rect.x -= Game.Position
            Screen.blit(Entity.image, Entity.rect)
            Entity.Life(Screen, Game)


def PrintPreMade(Game, Screen):
    for Entity in Game.PreMade:
        Entity.rect.x -= Game.Position
        Screen.blit(Entity.image, Entity.rect)


def PrintProjectiles(Game, Screen):
    for Projectile in Game.Projectiles:
        Projectile.rect.x -= Game.Position
        Projectile.move(Game)
        Screen.blit(Projectile.image, Projectile.rect)


def PrintStructures(Game, Screen):
    Game.Sol.rect.x += Game.Position

    for Structure in Game.all_plateform:
        Structure.rect.x -= Game.Position
        if -250 < Structure.rect.x < 1280:
            Screen.blit(Structure.image, Structure.rect)

    for Structure in Game.all_wall:
        Structure.rect.x -= Game.Position
        if -250 < Structure.rect.x < 1280:
            Screen.blit(Structure.image, Structure.rect)

    Screen.blit(Game.Sol.image, Game.Sol.rect)


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


def Draw_rect(Screen, Target):
    """Affiche le canevas / la HitBox de l'élément appellé -tremisabdoul"""
    pygame.draw.lines(Screen, (200, 150, 100), True, (
        Target.rect.midbottom, Target.rect.midtop, Target.rect.topleft, Target.rect.bottomleft, Target.rect.bottomright,
        Target.rect.topright, Target.rect.topleft, Target.rect.midleft, Target.rect.midright, Target.rect.bottomright))


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


""" ===  Animations  === """


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
