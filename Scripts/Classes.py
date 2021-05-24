from User.UserData import *
import random as rd
import pygame

print("/Scripts/Classes: Loading")

"""=====  Game [1]  ====="""


class Game:
    def __init__(self):

        self.pygame = pygame

        from math import atan2, degrees
        from time import time
        from random import randint
        self.AngleCalc, self.Deges, self.time, self.randint = atan2, degrees, time, randint
        del atan2, degrees, time, randint

        self.Saves    = SaveSlot()
        self.UserData = UserData()

        self.DataY = self.UserData.UserGraphicInfo.current_h
        self.DataX = self.UserData.UserGraphicInfo.current_w

        """ ===== Utility ===== """
        self.Running    = True
        self.Lobby      = True
        self.ShowHitbox = False
        self.PrepaSpell = False
        self.CastSpell = False
        self.Countframes = 0
        self.InGame     = False
        self.Option     = False
        self.Pause      = False
        self.SaveMenu   = False

        """ ===== Variable value ===== """
        self.PlateformNumber = 1
        self.Tickchecker     = 1
        self.WallNumber      = 1
        self.PositionPlayer  = 0
        self.PaternNumber    = 0
        self.lastPosition    = 0
        self.ActualFrame     = 0
        self.MusicLengh      = 0
        self.MusicStart      = 0
        self.Fullscreen      = 0
        self.SaveValue       = 0
        self.Position        = 0
        self.Frame           = 0
        self.Tick            = 0
        self.Timing = 0

        self.pressed = {}
        self.Paterns = {}
        self.Grid    = {}

        self.Timed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        """ ===== Song ===== """
        self.Click = pygame.mixer.Sound("Assets/Audio/FX/pas.mp3")
        self.data  = pygame.mixer.Sound("Assets/Audio/FX/DATA.mp3")

        """ ===== Police ===== """
        self.police1 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 10)
        self.police2 = pygame.font.Font("Assets/Font/Retro Gaming.ttf", 20)

        """ ===== Class Introduction ===== """
        self.Player     = Player()
        self.Arm        = Arm()
        self.Monster    = Monster()
        self.FinRudimentaire = FinRudimentaire()
        self.wall       = Wall()
        self.Sol        = Sol()
        self.Background = Background()
        self.Mouse      = Mouse()
        self.UI         = UI()
        self.Projectile = Projectile(self)
        self.Particles  = Particles()

        self.DataWeapon = None

        """ ===== Group ===== """
        self.all_Monster   = pygame.sprite.Group()
        self.all_Player    = pygame.sprite.Group()
        self.Entities      = pygame.sprite.Group()
        self.PreMade       = pygame.sprite.Group()
        self.all_plateform = pygame.sprite.Group()
        self.all_wall      = pygame.sprite.Group()
        self.AcrossWall    = pygame.sprite.Group()
        self.ApplyedPatens = pygame.sprite.Group()
        self.Projectiles   = pygame.sprite.Group()
        self.PreMade.add(self.FinRudimentaire)
        self.Entities.add(self.Player)
        self.all_plateform.add(self.Sol)
        self.all_wall.add(self.wall)
        self.all_Player.add(self.Player)

    def RandomRGB(self, RGB):
        """
        for item in range(3):
            Modifier = self.randint(-1, 1)
            RGB[item] += Modifier
            if not 0 < RGB[item] < 255:
                RGB[item] -= Modifier * 2
        """
        return (0, 0, 0)


    def Rescale(self, value, XorY):
        print("===\nx", self.UserData.DataX, ">>>", self.DataX, "\ny", self.UserData.DataY, ">>>", self.DataY)
        if XorY == "X":
            return round((value / self.UserData.DataX) * self.DataX)
        elif XorY == "Y":
            return round((value / self.UserData.DataY) * self.DataY)

    @staticmethod
    def check_collisions(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_rect)

    def RandomProba(self, Items, Probabilities):

        Possibilities = []
        for item in range(len(Probabilities)):
            for x in range(Probabilities[item]):
                if x > len(Possibilities):
                    Possibilities.append(Items[item])
        Possibilities.append(Items[-1])

        return Possibilities[self.randint(0, 99)]
    
    


"""=====  Game.Player [2.0]  ====="""


class Player(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        self.pop = False

        self.Force = Force()
        self.Game  = Game

        self.Pv      = 100
        self.MaxPv   = 100
        self.Damage  = 10
        self.Speed   = 3
        self.SpeedY  = 60
        self.Armor   = 0
        self.Mana    = 60
        self.MaxMana = 60  # ##### #
        self.CDR                  = 0
        self.AttackSpeed          = 0
        self.CCHit                = 130
        self.CCSpell              = 3
        self.CCDamage             = 3
        self.Penetration          = 0
        self.ManaRegen            = 2
        self.XP_Multiplicator     = 1
        self.Damage_Multiplicator = 1

        self.Level = 1
        self.Gold  = 100

        self.Gain_Stat_Level   = int((self.Level/2)**2+(self.Level/2))
        self.Point_Pv          = 0
        self.Point_Damage      = 0
        self.Point_Speed       = 2  # ##### #
        self.Point_Armor       = 0  # ##### #
        self.Point_Mana        = 60  # ##### #
        self.Point_MaxMana     = 0  # ##### #
        self.Point_CDR         = 0  # ##### #
        self.Point_AttackSpeed = 0  # ##### #
        self.Point_CCHit       = 0  # ##### #
        self.Point_CCSpell     = 0  # ##### #
        self.Point_CCDamage    = 0  # ##### #
        self.Point_Penetration = 0  # ##### #
        self.Point_ManaRegen   = 0  # ##### #

        self.Weapon1 = Class()
        self.Weapon2 = Class()

        self.Element = 'fire'

        self.image = pygame.image.load("Assets/Visual/Mystique/resp1.png")
        self.rect  = self.image.get_rect()
        self.rect  = self.image.get_rect(bottomleft=self.rect.bottomleft)

        self.rect.center = (320, 600)

        self.LastY        = 0
        self.YVector      = 0
        self.YVectorblit  = 0
        self.Base_Gravity = 0

        self.LastX = 0

        self.Direction = 1  # Droite = 1 Gauche = -1

        self.MinX = 20
        self.MaxX = 1200

        self.MinY = -20
        self.MaxY = 740
        self.MovementKey = False
        
    def Get_Hit(self, Damage, Game):
        #Bascule sur l'animation de la prise de dégats
        self.Pv -= Damage
        if self.Pv <= 0:
            self.Death(Game)

    def Move_Right(self, Game):
        self.Force.xm += self.Speed
        if not Game.PrepaSpell:
            self.Direction = 1

    def Move_Left(self, Game):
        self.Force.xm -= self.Speed
        if not Game.PrepaSpell:
            self.Direction = 0

    def Gain_Stats(self):
        self.MaxPv  += self.Gain_Stat_Level + (4 * self.Point_Pv)
        self.Damage += self.Gain_Stat_Level + (2 * self.Point_Damage)

    def Death(self, Game):
        self.all_Monster = pygame.sprite.Group()
        self.Pv = self.MaxPv
        Game.__init__()

    def Orb(self, Game):
        if Game.Frame % 2:
            if self.Element == 'fire':
                if self.Direction:
                    Game.Particles.Add(Game, (self.rect.center[0] - 25, self.rect.center[1] - 20), 'red', 6)
                    Game.Particles.Add(Game, (self.rect.center[0] - 25, self.rect.center[1] - 20), 'orangered', 6)
                    Game.Particles.Add(Game, (self.rect.center[0] - 25, self.rect.center[1] - 20), 'orangered4', 6)
                    Game.Particles.Add(Game, (Game.Player.rect.center[0] - 25, Game.Player.rect.center[1] - 20), 'red3', 6)
                else:
                    Game.Particles.Add(Game, (self.rect.center[0] + 25, self.rect.center[1] - 20), 'red', 6)
                    Game.Particles.Add(Game, (self.rect.center[0] + 25, self.rect.center[1] - 20), 'orangered', 6)
                    Game.Particles.Add(Game, (self.rect.center[0] + 25, self.rect.center[1] - 20), 'orangered4', 6)
                    Game.Particles.Add(Game, (Game.Player.rect.center[0] + 25, Game.Player.rect.center[1] - 20), 'red3', 6)


"""=====  Game.Player.Force [2.1]  ====="""


class Force:

    def __init__(self):

        self.x     = float(0)
        self.xm    = float(0)
        self.StepX = float(0)
        self.lastx = float(0)
        self.lasty = float(0)

        self.Game = Game

    def AccelerationFunctionX(self):

        self.StepX = self.xm + self.x + ((self.lastx / 1.00001) / 1.4)

        """if round(self.StepX) == 0:
            self.StepX = 0
            self.lastx = 0
            self.x = 0
            self.xm = 0
            return 0

        else:"""
        self.lastx = self.StepX
        self.x     = 0
        self.xm    = 0
        return self.StepX

    @staticmethod
    def Gravity(Game0, Target):
        base = Target.rect.y
        if Target.Base_Gravity < 20:
            Target.Base_Gravity += 0.4
            Target.rect.y += Target.Base_Gravity
        else:
            Target.Base_Gravity = 20
            Target.rect.y += 20

        Collide = Game0.check_collisions(Target, Game0.all_plateform)
        for item in Collide:

            if item and Target.YVector <= 1 and (Target.rect.bottom <= item.rect.top + Target.Base_Gravity + 2):
                Target.rect.y = base
                Replace = item.rect.top - (Target.rect.bottom - 1)  # Y reset (Premier pixel du rect de plateforme)
                if Target.Base_Gravity > 0.8:
                    Target.SpeedY = 0
                Target.Base_Gravity = 0
                Target.rect.y += Replace


"""=====  Game.Sol [3]  ====="""


class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Visual/plateforme_base - old.png")

        self.image = pygame.transform.scale(self.image, (1280, 34))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 686


"""=====  Game.Plateform [4]  ====="""


class Plateform(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        self.image = pygame.transform.scale(self.image, (250, 20))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0


"""=====  Game.Mouse [5]  ====="""


class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        pygame.mouse.set_visible(True)

        self.image = pygame.image.load("Assets/Visual/UI/Mouse.png")
        self.image = pygame.transform.scale(self.image, (22, 22))

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)


"""=====  Game.UI [6]  ====="""


class UI:

    def __init__(self):
        super().__init__()

        self.Lobby = LobbyUI()
        self.Option = OptionUI()

        self.baselayer = pygame.image.load("Assets/Visual/UI/baselayer.png")
        self.baselayer = pygame.transform.scale(self.baselayer, (1280, 720))

        self.resumebutton       = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.resumebutton       = pygame.transform.scale(self.resumebutton, (140, 30))
        self.resumebuttonrect   = self.resumebutton.get_rect()
        self.resumebuttonrect.x = 640 - 70
        self.resumebuttonrect.y = 360 - 40

        self.savebutton       = pygame.image.load("Assets/Visual/UI/bouton_SAUVEGARDER.png")
        self.savebutton       = pygame.transform.scale(self.savebutton, (172, 30))
        self.savebuttonrect   = self.savebutton.get_rect()
        self.savebuttonrect.x = 640 - 86
        self.savebuttonrect.y = 360

        self.settingsbutton       = pygame.image.load("Assets/Visual/UI/bouton_SETTINGS.png")
        self.settingsbutton       = pygame.transform.scale(self.settingsbutton, (100, 30))
        self.settingsbuttonrect   = self.settingsbutton.get_rect()
        self.settingsbuttonrect.x = 640 - 50
        self.settingsbuttonrect.y = 360 + 40

        self.quitbutton       = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.quitbutton       = pygame.transform.scale(self.quitbutton, (100, 30))
        self.quitbuttonrect   = self.quitbutton.get_rect()
        self.quitbuttonrect.x = 640 - 50
        self.quitbuttonrect.y = 360 + 80


"""=====  Game.Monster [7]  ====="""


class Monster(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        self.Pv          = 40
        self.MaxPv       = 100
        self.DamageDealt = 10
        self.Speed       = 3
        self.Price       = 2
        self.OnCD = False

        self.Special = []

        self.image = pygame.image.load("Assets/Visual/Entities/Monster/Slime/Stand1.png")

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
        self.LastY  = 675

        self.YVector      = 0
        self.YVectorblit  = 0
        self.Base_Gravity = 0

        self.rect = self.image.get_rect(midtop=self.rect.midtop)

        self.image0 = pygame.image.load("Assets/Visual/UI/100pv.png")
        self.image0 = pygame.transform.scale(self.image0, (200, 30))

        self.pvfontrect           = self.image0.get_rect()
        self.pvfontrect           = self.image0.get_rect(midbottom=self.pvfontrect.midbottom)
        self.pvfontrect.midbottom = self.rect.midtop
        self.pvfontrect.y        += 10

        self.Direction = 1

    def Life(self, Screen, Game):
        if self.Pv > 0:
            self.pvfontrect.midbottom = self.rect.midtop
            self.pvfontrect.y        -= 7
            self.image0               = pygame.transform.scale(self.image0, (int(self.Pv / self.MaxPv * 64), 8))
            self.Pv                  += 0.1
            #*
            Screen.blit(self.image0, (self.pvfontrect.x - Game.Position, self.pvfontrect.y))
        else:
            Game.all_Monster.remove(self)
            Game.Entities.remove(self)

    def Move_Right(self, Game):
        if Game.check_collisions(self, Game.all_plateform):
            self.rect.x += self.Speed
        else:
            self.rect.x   -= int(self.Speed * 2)
            self.Direction = 1

    def Move_Left(self, Game):
        if Game.check_collisions(self, Game.all_plateform):
            self.rect.x -= self.Speed
        else:
            self.rect.x   += int(self.Speed * 2)
            self.Direction = 0
            
    def Get_Hit(self, damage, Game):
        #Bascule sur l'animation de la prise de dégats
        self.Pv -= damage
        #* coupé collé du #* plus haut.[
        if self.Pv <= 0:
                Game.Entities.remove(self)
                Game.all_Monster.remove(self)
                Game.Player.Gold += self.Price
                del self
                #]


class Weapon:

    def __init__(self):
        # Type d'arme Ex: Staff = 3
        self.MetaType = rd.randrange(1, 5, 1)

        # Arme en question Ex: Staff.Feu = 3.4
        self.MetaWeapon = rd.randrange(1, 10, 1)

        # Rarerte Ex: Staff.Feu.Rare = 3.4.2
        self.MetaClass = rd.randrange(1, 4, 1)

        # Donne l'ensemble des propiÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â©es de l'arme  Ex: 3.4.2
        self.MetaName = [self.MetaType, self.MetaWeapon, self.MetaClass]

        self.Damage = rd.randrange(2, 9, 1)
        self.Speed  = rd.randrange(41, 80, 1)/10
        self.CD     = self.MetaWeapon * 3

        self.DamageBuff = 0
        self.SpeedBuff  = 0
        self.CDR        = 0
        self.tester     = self.MetaClass

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
        self.image  = pygame.image.load("Assets/Visual/Structure/Wall.png")
        self.image  = pygame.transform.scale(self.image, (250, 150))
        self.rect   = self.image.get_rect()
        self.rect.x = - 750
        self.rect.y = - 0


class Background:

    def __init__(self):
        super().__init__()
        self.image       = pygame.image.load("Assets/Visual/UI/Background.png")
        self.rect        = self.image.get_rect()
        self.rect        = self.image.get_rect(midtop=self.rect.midtop)
        self.rect.midtop = (self.rect.width / 3, 0)
        print("Oui", self.rect.height)


class Arm:
    def __init__(self):
        super().__init__()
        self.Game = Game

        self.image          = pygame.image.load("Assets/Visual/Mystique/Spells/bras mystique prepa spell.png")
        self.imageDirection = 0
        self.rect           = self.image.get_rect()

        self.rect.x       = 100
        self.rect.y       = 100
        self.rect         = self.image.get_rect(center=self.rect.center)
        self.origin_image = self.image
        self.angle        = 0

    def print(self, Game, Screen):
        self.rect.center = Game.Player.rect.center
        if self.rect.y - Game.Mouse.rect.y and self.rect.x - Game.Mouse.rect.x:
            self.angle = -Game.Deges(Game.AngleCalc(Game.Mouse.rect.center[1] - self.rect.center[1],
                                                    Game.Mouse.rect.center[0] - self.rect.center[0]))

        if -90 < self.angle < 90:
            if Game.CastSpell:

                self.origin_image = pygame.image.load("Assets/Visual/Mystique/Spells/bras mystique cast spell.png")
                Game.Countframes -= 1

                if Game.Countframes < 1:
                    Game.CastSpell = False
            else:
                self.origin_image = pygame.image.load("Assets/Visual/Mystique/Spells/bras mystique prepa spell.png")

            self.imageDirection = 0
            Game.Player.Direction = 1

        elif not -90 < self.angle < 90:
            if Game.CastSpell:

                self.origin_image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/bras mystique cast spell.png")
                Game.Countframes -= 1

                if Game.Countframes < 1:
                    Game.CastSpell = False
            else:
                self.origin_image = pygame.image.load("Assets/Visual/Mystique/Left/Spells/bras mystique prepa spell.png")

            self.imageDirection = 1
            Game.Player.Direction = 0

        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect  = self.image.get_rect(center=self.rect.center)
        Screen.blit(self.image, self.rect)


class Patern(pygame.sprite.Sprite, Game):
    def __init__(self):
        super().__init__()
        self.ID         = 0
        self.position   = 0
        self.PaternCode = 0

    def Init(self, Game, NewWall, NewPlatform, SpawnMonster):
        self.ID       = Game.PaternNumber
        self.position = Game.PaternNumber * 10 - 10
        Id            = len(Game.ApplyedPatens)
        while Id > len(Game.Paterns) - 1:
            Id -= len(Game.Paterns)

        self.PaternCode = Game.Paterns[Id]
        posy = -1
        for item in range(len(self.PaternCode)):
            posx = -1
            if 1 <= item <= 5:
                posy += 1
                for tile in self.PaternCode[item]:
                    posx += 1
                    if tile == "#":
                        NewWall(Game, posx + self.position, posy)
                    elif tile == "_":
                        NewPlatform(Game, posx + self.position, posy)
                    elif tile == "o":
                        SpawnMonster(Game, posx + self.position, posy)
        Game.PaternNumber += 1

        """ Checking
        for item in Game.Entities:
            print(item.rect)
        for item in Game.all_Monster:
            print(item.rect)
        """


class Projectile(pygame.sprite.Sprite):

    def __init__(self, Game):
        super().__init__()

        self.Damage = 10

        self.Radius = 42

        self.Speed  = 15
        self.Frames = ["Assets/Visual/Spells/FireBall/Nion1.png",
                       "Assets/Visual/Spells/FireBall/Nion2.png",
                       "Assets/Visual/Spells/FireBall/Nion3.png"]
        self.Frame        = 0
        self.origin_image = pygame.image.load("Assets/Visual/Spells/FireBall/Nion1.png")
        self.rect         = self.origin_image.get_rect()
        self.rect.x, self.rect.y = Game.Player.rect.center
        self.DistanceX    = Game.Mouse.rect.center[0] - self.rect.center[0]
        self.DistanceY    = Game.Mouse.rect.center[1] - self.rect.center[1]

        if self.DistanceY == 0:
            self.DistanceY = 0.01
        from math import sqrt

        self.norm       = sqrt(self.DistanceX ** 2 + self.DistanceY ** 2)
        self.DirectionX = self.DistanceX / self.norm
        self.DirectionY = self.DistanceY / self.norm
        self.DirectionX = self.DirectionX * sqrt(2)
        self.DirectionY = self.DirectionY * sqrt(2)

        self.DirectionX, self.DirectionY = self.DirectionX * self.Speed, self.DirectionY * self.Speed

        self.angle = -Game.Deges(Game.AngleCalc(self.DirectionY, self.DirectionX))

        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect  = self.image.get_rect(center=self.rect.center)

        self.rect.x = Game.Player.rect.center[0] + int(self.DirectionX * 1.7)
        self.rect.y = Game.Player.rect.center[1] + int(self.DirectionY * 1.7)

    def move(self, Game):

        if Game.Frame % 2:
            if self.Frame == 0:
                self.Frame = 1
                self.origin_image = pygame.image.load(self.Frames[1])
            if self.Frame == 1:
                self.Frame = 2
                self.origin_image = pygame.image.load(self.Frames[2])
            if self.Frame == 2:
                self.Frame = 0
                self.origin_image = pygame.image.load(self.Frames[0])

        self.rect.x     += self.DirectionX
        self.rect.y     += self.DirectionY
        self.DirectionY += 0.05
        self.angle       = -Game.Deges(Game.AngleCalc(self.DirectionY, self.DirectionX))

        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect  = self.image.get_rect(center=self.rect.center)

        Game.Particles.Add(Game, self.rect.center, 'red', 8)
        Game.Particles.Add(Game, self.rect.center, 'orangered', 8)

        if not -1280 < self.rect.x - Game.Player.rect.x < 1280\
                or not -720 < self.rect.y < 720\
                or Game.check_collisions(self, Game.all_wall)\
                or Game.check_collisions(self, Game.all_plateform)\
                or Game.check_collisions(self, Game.all_Monster):
            Game.Projectiles.remove(self)

            for Entity in Game.Entities:
                if self.rect.center[0] - self.Radius <= Entity.rect.topleft[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.topleft[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[1] - self.Radius <= Entity.rect.topright[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[0] - self.Radius <= Entity.rect.topright[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.midleft[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.midleft[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.midright[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.midright[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.midtop[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.midtop[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.midbottom[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.midbottom[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.bottomleft[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.bottomleft[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)
                elif self.rect.center[0] - self.Radius <= Entity.rect.bottomright[0] <= self.rect.center[0] + self.Radius and\
                        self.rect.center[1] - self.Radius <= Entity.rect.bottomright[1] <= self.rect.center[1] + self.Radius:
                    Entity.Get_Hit(self.Damage, Game)

            for _ in range(5):
                Game.Particles.Add(Game, self.rect.center, 'Grey80', 32)
            for _ in range(3):
                Game.Particles.Add(Game, self.rect.center, 'Grey70', 24)
            for _ in range(3):
                Game.Particles.Add(Game, self.rect.center, 'Grey60', 16)
            for _ in range(3):
                Game.Particles.Add(Game, self.rect.center, 'Grey50', 12)


    @staticmethod
    def Add(Game):
        Game.Projectiles.add(Projectile(Game))


class Particles:
    def __init__(self):
        self.Particles = []

    def Print(self, Game, Screen):
        if self.Particles:
            for Particle in self.Particles:
                Particle[0][0] -= Game.Position

                if not Game.Frame % 2:
                    Particle[0][1] += Particle[3]
                    Particle[0][0] += Particle[2]

                Particle[1] -= Particle[5]

                if Particle[1] < 0.1:
                    self.Particles.remove(Particle)
                pygame.draw.circle(Screen, Particle[4], [Particle[0][0], Particle[0][1]], Particle[1])

    def Add(self, Game, Position, Color, Radius, Decrease = 0):

        x = Position[0] + Game.randint(int(-Radius / 2), int(Radius / 2))
        y = Position[1] + Game.randint(int(-Radius / 2), int(Radius / 2))

        DirectionX = Game.randint(-2, 2)
        DirectionY = Game.randint(-2, 2)

        if not Decrease:
            Decrease = Radius / 20

        #               v rect v        v taille v          v mouvement v       v couleur v
        Particle = [[int(x), int(y)], int(Radius), int(DirectionX), int(DirectionY), Color, Decrease]
        self.Particles.append(Particle)


class FinRudimentaire(pygame.sprite.Sprite, Game):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Assets/Visual/Structure/ligneFin.png")
        self.rect = self.image.get_rect()
        self.rect.x = 10400
        self.rect.y = 0
        self.origin_image = self.image

        self.YVector = 0
        self.YVectorblit = 0
        self.Base_Gravity = 0


class Class:
    def __init__(self):
        pass


class LobbyUI:
    def __init__(self):
        self.background = pygame.image.load("Assets/Visual/background.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))

        self.playbutton       = pygame.image.load("Assets/Visual/UI/bouton_JOUER.png")
        self.playbutton       = pygame.transform.scale(self.playbutton, (82, 30))
        self.playbuttonrect   = self.playbutton.get_rect()
        self.playbuttonrect.x = -62
        self.playbuttonrect.y = 360 - 60

        self.loadbutton       = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.loadbutton       = pygame.transform.scale(self.loadbutton, (140, 30))
        self.loadbuttonrect   = self.loadbutton.get_rect()
        self.loadbuttonrect.x = -62
        self.loadbuttonrect.y = 360

        self.quitbutton       = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.quitbutton       = pygame.transform.scale(self.quitbutton, (100, 30))
        self.quitbuttonrect   = self.quitbutton.get_rect()
        self.quitbuttonrect.x = -62
        self.quitbuttonrect.y = 360 + 60

    def TitleMenuButtonDeplacement(self, Game):

        Dep = (self.loadbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.loadbuttonrect.x = Dep * -Dep + 186

        Dep = (self.quitbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.quitbuttonrect.x = Dep * -Dep + 206

        Dep = (self.playbuttonrect.y - Game.Mouse.rect.y) / 16
        if Dep > 0:
            Dep = -Dep
        self.playbuttonrect.x = Dep * -Dep + 215


class OptionUI:
    def __init__(self):
        super().__init__()

        self.Color = [10, 10, 20]

        self.Cursor = pygame.image.load("Assets/Visual/UI/Cursor.png")

        self.Key1 = pygame.Rect(100, 400, 125, 125)
        self.Key2 = pygame.Rect(100, 550, 125, 125)
        self.Key3 = pygame.Rect(250, 550, 125, 125)
        self.Key4 = pygame.Rect(250, 400, 125, 125)

        """C'Ã©tait chiant"""
        self.Keys = {
            0: pygame.image.load("Assets/Visual/UI/Key/Other.png"),
            32: pygame.image.load("Assets/Visual/UI/Key/Space.png"),
            48: pygame.image.load("Assets/Visual/UI/Key/0.png"),
            49: pygame.image.load("Assets/Visual/UI/Key/1.png"),
            50: pygame.image.load("Assets/Visual/UI/Key/2.png"),
            51: pygame.image.load("Assets/Visual/UI/Key/3.png"),
            52: pygame.image.load("Assets/Visual/UI/Key/4.png"),
            53: pygame.image.load("Assets/Visual/UI/Key/5.png"),
            54: pygame.image.load("Assets/Visual/UI/Key/6.png"),
            55: pygame.image.load("Assets/Visual/UI/Key/7.png"),
            56: pygame.image.load("Assets/Visual/UI/Key/8.png"),
            57: pygame.image.load("Assets/Visual/UI/Key/9.png"),
            97: pygame.image.load("Assets/Visual/UI/Key/A.png"),
            98: pygame.image.load("Assets/Visual/UI/Key/B.png"),
            99: pygame.image.load("Assets/Visual/UI/Key/C.png"),
            100: pygame.image.load("Assets/Visual/UI/Key/D.png"),
            101: pygame.image.load("Assets/Visual/UI/Key/E.png"),
            102: pygame.image.load("Assets/Visual/UI/Key/F.png"),
            103: pygame.image.load("Assets/Visual/UI/Key/G.png"),
            104: pygame.image.load("Assets/Visual/UI/Key/H.png"),
            105: pygame.image.load("Assets/Visual/UI/Key/I.png"),
            106: pygame.image.load("Assets/Visual/UI/Key/J.png"),
            107: pygame.image.load("Assets/Visual/UI/Key/K.png"),
            108: pygame.image.load("Assets/Visual/UI/Key/L.png"),
            109: pygame.image.load("Assets/Visual/UI/Key/M.png"),
            110: pygame.image.load("Assets/Visual/UI/Key/N.png"),
            111: pygame.image.load("Assets/Visual/UI/Key/O.png"),
            112: pygame.image.load("Assets/Visual/UI/Key/P.png"),
            113: pygame.image.load("Assets/Visual/UI/Key/Q.png"),
            114: pygame.image.load("Assets/Visual/UI/Key/R.png"),
            115: pygame.image.load("Assets/Visual/UI/Key/S.png"),
            116: pygame.image.load("Assets/Visual/UI/Key/T.png"),
            117: pygame.image.load("Assets/Visual/UI/Key/U.png"),
            118: pygame.image.load("Assets/Visual/UI/Key/V.png"),
            119: pygame.image.load("Assets/Visual/UI/Key/W.png"),
            120: pygame.image.load("Assets/Visual/UI/Key/X.png"),
            121: pygame.image.load("Assets/Visual/UI/Key/Y.png"),
            122: pygame.image.load("Assets/Visual/UI/Key/Z.png"),
        }


print("/Scripts/Classes: Loaded")