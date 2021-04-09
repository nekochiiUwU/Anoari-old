from User.UserData import *
import random as rd
import pygame

print("/Scripts/Classes: Loading")

"""=====  Game [1]  ====="""


class Game:

    # Fonction exÃƒÂ©cutÃƒÂ©e au dÃƒÂ©marrage de Game -tremisabdoul
    def __init__(self):
        # SaveSlot devient une sous-classe de Game -tremisabdoul
        self.Saves = SaveSlot()
        # UserData devient une sous-classe de Game -tremisabdoul
        self.UserData = UserData()
        self.DataY = self.UserData.UserGraphicInfo.current_h
        self.DataX = self.UserData.UserGraphicInfo.current_w

        # Contient toutes les touches prÃƒÂ©ssÃƒÂ©es -tremisabdoul
        self.pressed = {}

        # Variables Generales -tremisabdoul
        from math import atan2
        self.AngleCalc = atan2
        del atan2

        from math import degrees
        self.Deges = degrees
        del degrees

        self.Running = True
        self.Lobby = True
        self.ShowHitbox = False
        self.PrepaSpell = False
        self.InGame = False
        self.Option = False
        self.Pause = False
        self.PlateformNumber = 1
        self.Tickchecker = 1
        self.WallNumber = 1
        self.PositionPlayer = 0
        self.PaternNumber = 0
        self.lastPosition = 0
        self.ActualFrame = 0
        self.MusicLengh = 0
        self.MusicStart = 0
        self.Fullscreen = 0
        self.Position = 0
        self.Frame = 0
        self.Pas = None
        self.Paterns = {}
        self.Grid = {}

    def Rescale(self, value, XorY):
        if XorY == "X":
            return round((value / 1280) * self.DataX)
        elif XorY == "Y":
            return round((value / 720) * self.DataY)

    def init_suite(self):
        # Player devient une sous-classe de Game -tremisabdoul
        self.Player = Player()
        self.Arm = Arm()
        # Sol devient une sous-classe de Game -Steven
        self.Sol = Sol()
        # Mouse devient une sous-classe de Game -tremisabdoul
        self.Mouse = Mouse()
        # UI devient une sous-classe de Game -tremisabdoul
        self.UI = UI()
        # Monster devient une sous-classe de Game - steven
        self.Monster = Monster()
        self.Background = Background()
        self.wall = Wall()

        # CrÃƒÂ©ation du groupe composÃƒÂ© de tous les monstres -Steven
        self.all_Monster = pygame.sprite.Group()
        self.all_Monster.add(self.Monster)

        # CrÃƒÂ©ation du groupe composÃƒÂ© de tous les joueurs -Steven
        self.all_Player = pygame.sprite.Group()
        self.all_Player.add(self.Player)

        self.Entities = pygame.sprite.Group()
        self.Entities.add(self.Monster)
        self.Entities.add(self.Player)

        # CrÃƒÂ©ation du groupe composÃƒÂ© de toutes les plateformes -Steven
        self.all_plateform = pygame.sprite.Group()
        self.all_plateform.add(self.Sol)

        self.all_wall = pygame.sprite.Group()
        self.all_wall.add(self.wall)

        self.AcrossWall = pygame.sprite.Group()
        self.ApplyedPatens = pygame.sprite.Group()


"""=====  Game.Player [2.0]  ====="""


class Player(pygame.sprite.Sprite, Game):

    # Fonction exÃƒÂ©cutÃƒÂ©e au dÃƒÂ©marrage de Player -tremisabdoul
    def __init__(self):
        super().__init__()

        self.pop = False

        # Force devient une sous-classe de Player et Game est chargÃƒÂ© en tant que super-classe -tremisabdoul
        self.Force = Force()
        self.Game = Game

        # Statistiques -tremisabdoul
        self.Pv = 100
        self.MaxPv = 100
        self.Damage = 10
        self.Speed = 3
        self.SpeedY = 60
        self.Armor = 0
        self.Mana = 60
        self.MaxMana = 60  # ##### #
        # Statistique Variable -steven
        self.CDR = 0
        self.AttackSpeed = 0
        self.CCHit = 130
        self.CCSpell = 3
        self.CCDamage = 3
        self.Penetration = 0
        self.ManaRegen = 2
        self.XP_Multiplicator = 1
        self.Damage_Multiplicator = 1

        self.Level = 1
        self.Gold = 100

        # Statistique gagnÃƒÂ©e par niveau / points -steven
        self.Gain_Stat_Level = int((self.Level/2)**2+(self.Level/2))
        self.Point_Pv = 0
        self.Point_Damage = 0
        self.Point_Speed = 2  # ##### #
        self.Point_Armor = 0  # ##### #
        self.Point_Mana = 60  # ##### #
        self.Point_MaxMana = 0  # ##### #
        self.Point_CDR = 0  # ##### #
        self.Point_AttackSpeed = 0  # ##### #
        self.Point_CCHit = 0  # ##### #
        self.Point_CCSpell = 0  # ##### #
        self.Point_CCDamage = 0  # ##### #
        self.Point_Penetration = 0  # ##### #
        self.Point_ManaRegen = 0  # ##### #

        self.Weapon1 = Weapon()
        self.Weapon2 = Weapon()

        # DÃƒÂ©finit l'ÃƒÂ©lÃƒÂ©ment visuel en tant que variable et la hitbox de Player -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

        # Position de Player -tremisabdoul
        self.rect.center = (320, 600)

        self.LastY = 0
        self.YVector = 0
        self.YVectorblit = 0
        self.Base_Gravity = 0

        self.LastX = 0

        self.Direction = 1  # Droite = 1 Gauche = -1

        # Valeurs max et min que Player peut atteindre (Bords de l'ÃƒÂ©cran x) -tremisabdoul
        self.MinX = 20
        self.MaxX = 1200

        # Valeurs max et min que Player peut atteindre (Bords de l'ÃƒÂ©cran y) -tremisabdoul
        self.MinY = -20
        self.MaxY = 740
        self.MovementKey = False

    #   def Check_Collisions(rectA, rectB):
    #       if rectB.right < rectA.left:
    #           # rectB est ÃƒÂ  gauche
    #           return False
    #       if rectB.bottom < rectA.top:
    #           # rectB est au-dessus
    #           return False
    #       if rectB.left > rectA.right:
    #           # rectB est ÃƒÂ  droite
    #           return False
    #       if rectB.top > rectA.bottom:
    #           # rectB est en-dessous
    #           return False

    # Fonction de collision -tremisabdoul

    @staticmethod
    def check_collisions(sprite, group):
        Pass = pygame.sprite.Group()
        for item in group:
            if not -680 < sprite.rect.x - item.rect.x < 680:
                Pass.add(item)
                group.remove(item)
        Return = pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_rect)
        for item in Pass:
            group.add(item)
            Pass.remove(item)
        return Return

    # Fonction de mouvement (Droite) -tremisabdoul
    def Move_Right(self, Game):
        self.Force.xm += self.Speed
        if not Game.PrepaSpell:
            self.Direction = 1

    # Fonction de mouvement (Gauche) -tremisabdoul
    def Move_Left(self, Game):
        self.Force.xm -= self.Speed
        if not Game.PrepaSpell:
            self.Direction = 0

    # Fonction de gain de stat ( valeur placÃƒÂ©e arbitrairement lol ) - steven
    def Gain_Stats(self):
        self.MaxPv += self.Gain_Stat_Level + (4 * self.Point_Pv)
        self.Damage += self.Gain_Stat_Level + (2 * self.Point_Damage)

    # Fonction appliquÃƒÂ© que si l'utilisateur meurt
    def Death(self):
        self.all_Monster = pygame.sprite.Group()
        self.Player.Pv = self.Player.MaxPv


"""=====  Game.Player.Force [2.1]  ====="""


#  Contient les vecteurs physiques -tremisabdoul
class Force:

    # Fonction exÃƒÂ©cutÃƒÂ©e au demarÃƒÂ©e au lancement de Force - tremisabdoul
    def __init__(self):

        self.x = float(0)
        self.xm = float(0)
        self.StepX = float(0)
        self.lastx = float(0)
        self.lasty = float(0)

        self.Game = Game

    # Fonction permettant un mouvement fluide -tremisabdoul
    def AccelerationFunctionX(self):

        # Forces appliquÃƒÂ©s + ((Forces appliquÃƒÂ©s lors de la derniÃƒÂ¨re frame / 1.3) / 1.1) -tremisabdoul
        self.StepX = self.xm + self.x + ((self.lastx / 1.00001) / 1.4)

        """if round(self.StepX) == 0:
            self.StepX = 0
            self.lastx = 0
            self.x = 0
            self.xm = 0
            return 0

        else:"""
        self.lastx = self.StepX
        self.x = 0
        self.xm = 0
        return self.StepX

    # Faut se dire que la gravitÃƒÂ© a une force de 20 et que lorsque
    # Base_Gravity est a 0 c'est que la force appliquÃƒÂ©e par le sol est de -20
    def Gravity(self, Game0, Target):
        base = Target.rect.y
        if Target.Base_Gravity < 20:  # Si force de sol > 0
            Target.Base_Gravity += 0.4  # Diminution de la force "Sol" (Ratio 0.4)
            Target.rect.y += Target.Base_Gravity
        else:
            Target.Base_Gravity = 20  # Force de sol = 0
            Target.rect.y += 20

        # VÃƒÂ©rification des collisions entre Player et toutes les plateformes
        Collide = Game0.Player.check_collisions(Target, Game0.all_plateform)
        for item in Collide:

            if item and Target.YVector <= 1 and (Target.rect.bottom <= item.rect.top + Target.Base_Gravity + 2):
                Target.rect.y = base
                Replace = item.rect.top - (Target.rect.bottom - 1)  # Y reset (Premier pixel du rect de plateforme)
                if Target.Base_Gravity > 0.8:
                    Target.SpeedY = 0  # Cancel le saut
                Target.Base_Gravity = 0  # Reset la force du sol (-20)
                Target.rect.y += Replace


"""=====  Game.Sol [3]  ====="""


class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # DÃƒÂ©finit l'ÃƒÂ©lÃƒÂ©ment visuel en tant que variable -steven
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la rÃƒÂ©solution indiquÃƒÂ©e -tremisabdoul
        self.image = pygame.transform.scale(self.image, (1280, 34))

        # DÃƒÂ©finit la hitbox de sol -steven
        self.rect = self.image.get_rect()

        # Position de la plateforme principale -steven
        self.rect.x = 0
        self.rect.y = 686


"""=====  Game.Plateform [4]  ====="""


class Plateform(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        # DÃƒÂ©finit l'ÃƒÂ©lÃƒÂ©ment visuel en tant que variable -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la rÃƒÂ©solution indiquÃƒÂ©e -tremisabdoul
        self.image = pygame.transform.scale(self.image, (250, 20))

        # DÃƒÂ©finit la hitbox de sol -tremisabdoul
        self.rect = self.image.get_rect()

        # Position de la plateforme -tremisabdoul
        self.rect.x = 0
        self.rect.y = 0


"""=====  Game.Mouse [5]  ====="""


class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Rends la sourie windows invisible -tremisabdoul
        pygame.mouse.set_visible(True)

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

        """ CatÃƒÂ©gorie Pause """
        # Font grisÃƒÂ© (Ca prends full perf) -tremisabdoul
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

        # Boutton "PARAMÃƒË†TRE" -steven
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

        """ CatÃƒÂ©gorie Menu d'accueil """

        # IntÃƒÂ©gration de l'image qui apparaitrera du menu d'accueil -steven
        self.lobbybackground = pygame.image.load("Assets/Visual/background.jpg")
        self.lobbybackground = pygame.transform.scale(self.lobbybackground, (1280, 720))

        # IntÃƒÂ©gration du boutton "JOUER" -steven
        self.lobby_playbutton = pygame.image.load("Assets/Visual/UI/bouton_JOUER.png")
        self.lobby_playbutton = pygame.transform.scale(self.lobby_playbutton, (82, 30))
        self.lobby_playbuttonrect = self.lobby_playbutton.get_rect()
        self.lobby_playbuttonrect.x = -62
        self.lobby_playbuttonrect.y = 360 - 60

        # IntÃƒÂ©gration du boutton "CHARGER" -steven
        self.lobby_loadbutton = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.lobby_loadbutton = pygame.transform.scale(self.lobby_loadbutton, (140, 30))
        self.lobby_loadbuttonrect = self.lobby_loadbutton.get_rect()
        self.lobby_loadbuttonrect.x = -62
        self.lobby_loadbuttonrect.y = 360

        # IntÃƒÂ©gration du boutton "QUITTER" -Steven
        self.lobby_quitbutton = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.lobby_quitbutton = pygame.transform.scale(self.lobby_quitbutton, (100, 30))
        self.lobby_quitbuttonrect = self.lobby_quitbutton.get_rect()
        self.lobby_quitbuttonrect.x = -62
        self.lobby_quitbuttonrect.y = 360 + 60

    def TitleMenuButtunDeplacement(self, Game):

        Dep = (self.lobby_loadbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.lobby_loadbuttonrect.x = Dep * -Dep + 186

        Dep = (self.lobby_quitbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.lobby_quitbuttonrect.x = Dep * -Dep + 206

        Dep = (self.lobby_playbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.lobby_playbuttonrect.x = Dep * -Dep + 215


"""=====  Monstre [7]  ====="""


class Monster(pygame.sprite.Sprite, Game):

    # Fonction ÃƒÂ©xÃƒÂ©cutÃƒÂ© au dÃƒÂ©marrage de Monster -steven
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

    # DÃƒÂ©placement du monstre vers la droite -steven
    def Move_Right(self, Game):
        if Game.Player.check_collisions(self, Game.all_plateform):
            self.rect.x += self.Speed
        else:
            self.rect.x -= int(self.Speed * 2)
            self.Direction = 1

    # DÃƒÂ©placement du monstre vers la gauche -steven
    def Move_Left(self, Game):
        if Game.Player.check_collisions(self, Game.all_plateform):
            self.rect.x -= self.Speed
        else:
            self.rect.x += int(self.Speed * 2)
            self.Direction = 0


class Weapon:

    def __init__(self):
        # Type d'arme Ex: Mitraillette = 3
        self.MetaType = rd.randrange(1, 5, 1)

        # Arme en question Ex: Mitraillette.Poison = 3.4
        self.MetaWeapon = rd.randrange(1, 10, 1)

        # RarertÃƒÂ© Ex: Mitraillette.Poison.Rare = 3.4.2
        self.MetaClass = rd.randrange(1, 4, 1)

        # Donne l'ensemble des propiÃƒÂ©tÃƒÂ©es de l'arme  Ex: 3.4.2
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


class Wall(pygame.sprite.Sprite, Game):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Visual/Structure/Wall.png")
        self.image = pygame.transform.scale(self.image, (250, 150))
        self.rect = self.image.get_rect()
        self.rect.x = - 750
        self.rect.y = - 0


class Background:

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Visual/UI/Background.png")
        # self.image = pygame.transform.scale(self.image, (3848, 686))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(midtop=self.rect.midtop)
        self.rect.midtop = (self.rect.width / 3, 0)


class Arm:
    def __init__(self):
        super().__init__()
        self.Game = Game

        self.image = pygame.image.load("Assets/Visual/Mystique/Bras/bras mystique prepa spell.png")
        self.imageDirection = 0
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100
        self.rect = self.image.get_rect(center=self.rect.center)
        self.origin_image = self.image
        self.angle = 0

    def print(self, Game, Screen):
        self.rect.center = Game.Player.rect.center
        if self.rect.y - Game.Mouse.rect.y and self.rect.x - Game.Mouse.rect.x:
            self.angle = -Game.Deges(Game.AngleCalc(Game.Mouse.rect.center[1] - self.rect.center[1],
                                                    Game.Mouse.rect.center[0] - self.rect.center[0]))

        if -90 < self.angle < 90 and self.imageDirection:
            self.origin_image = pygame.image.load("Assets/Visual/Mystique/Bras/bras mystique prepa spell.png")
            self.imageDirection = 0
            Game.Player.Direction = 1
        elif not -90 < self.angle < 90 and not self.imageDirection:
            self.origin_image = pygame.image.load("Assets/Visual/Mystique/Left/bras mystique prepa spell.png")
            self.imageDirection = 1
            Game.Player.Direction = 0

        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        Screen.blit(self.image, self.rect)


class Patern(pygame.sprite.Sprite, Game):
    def __init__(self):
        super().__init__()
        self.ID = 0
        self.position = 0
        self.PaternCode = 0

    def Init(self, Game, NewWall, NewPlatform):
        self.ID = Game.PaternNumber
        self.position = Game.PaternNumber * 10 - 10
        Id = len(Game.ApplyedPatens)
        while Id > len(Game.Paterns) - 1:
            Id -= len(Game.Paterns)

        self.PaternCode = Game.Paterns[Id]
        posy = -1
        for item in range(len(self.PaternCode)):
            posx = -1
            if 2 <= item <= 6:
                posy += 1
                for tile in self.PaternCode[item]:
                    posx += 1
                    if tile == "#":
                        NewWall(Game, posx + self.position, posy)
                    elif tile == "_":
                        NewPlatform(Game, posx + self.position, posy)
        Game.PaternNumber += 1




print("/Scripts/Classes: Loaded")
