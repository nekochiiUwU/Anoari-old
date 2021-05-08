import pygame


class DataWeapons:
    def __init__(self, Game):

        super().__init__()

        self.Types = ["Lightning", "Fire", "Wind", "Water", "Shadow", "Light"]
        self.TypesProbabilties = [23, 46, 69, 92, 96, 100]
        self.TypesLight = [80, 70, 30, 20, 5, 95]

        globals()

        for item in range(30):
            print("Loading spells: spell" + str(item))
            exec("self.spell" + str(item) + " = " + "Spell(Game, item)")



        self.Weapons = [
            {
                "Name": "Lightning Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Fire Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Wind Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Water Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Shadow Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Light Staff",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            }
        ]

    def New(self, Game, Weapon):
        TypeID = Game.RandomProba([0, 1, 2, 3, 4, 5], self.TypesProbabilties)
        Type = self.Types[TypeID]

        Data = self.Weapons[TypeID]

        Rarety = Game.RandomProba(Data["Rarety"], Data["RaretyProba"])

        if TypeID < 4:
            A = TypeID * 6
            print(TypeID, A)
        else:
            A = TypeID - 8 + TypeID * 2
            print(TypeID, A)
        Spells = []

        for _ in range(Rarety):
            exec("global spell\nspell = self.spell" + str(Game.randint(0, 6) + A))
            global spell
            Spells.append(spell)
            if len(Spells) > 1:
                while Spells[-1].Name == Spells[-2].Name:
                    exec("global spell\nspell = self.spell" + str(Game.randint(0, 6) + A))
                    Spells.append(spell)

        Weapon.TypeID = TypeID
        Weapon.Type = Type
        Weapon.Data = Data
        Weapon.Rarety = Rarety
        Weapon.Spells = Spells

        print(TypeID, Type, Data, Rarety, "\n".join(["\t" + Spell.Name for Spell in Spells]), sep="\n")


# Lightning
class Spell0(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell0"


class Spell1(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell1"


class Spell2(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell2"


class Spell3(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell3"


class Spell4(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell4"


class Spell5(pygame.sprite.Sprite):
    def __init__(self, Game):
        super().__init__()
        self.Name = "Spell5"


# Fire
class Spell6(pygame.sprite.Sprite):
    def __init__(self, Game):
        import pygame
        super().__init__()

        self.Name = "FireBall"

        self.Speed  = 15
        self.Frames = ["Assets/Visual/Spells/FireBall/Nion1.png",
                       "Assets/Visual/Spells/FireBall/Nion2.png",
                       "Assets/Visual/Spells/FireBall/Nion3.png"]
        self.Frame        = 0
        self.origin_image = pygame.image.load("Assets/Visual/Spells/FireBall/Nion1.png")
        self.rect         = self.origin_image.get_rect()
        self.rect.x       = Game.Player.rect.x + 80
        self.rect.y       = Game.Player.rect.y + 45
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
                or Game.check_collisions(self, Game.all_plateform):
            Game.Projectiles.remove(self)
            for _ in range(5):
                Game.Particles.Add(Game, self.rect.center, 'Grey80', 32)
            for _ in range(5):
                Game.Particles.Add(Game, self.rect.center, 'Grey70', 24)
            for _ in range(5):
                Game.Particles.Add(Game, self.rect.center, 'Grey60', 16)
            for _ in range(5):
                Game.Particles.Add(Game, self.rect.center, 'Grey50', 12)

    @staticmethod
    def Add(Game):
        Game.Projectiles.add(Spell0(Game))


class Spell7:
    def __init__(self, Game):
        self.Name = "Spell7"


class Spell8:
    def __init__(self, Game):
        self.Name = "Spell8"


class Spell9:
    def __init__(self, Game):
        self.Name = "Spell9"


class Spell10:
    def __init__(self, Game):
        self.Name = "Spell10"


class Spell11:
    def __init__(self, Game):
        self.Name = "Spell11"


# Wind
class Spell12:
    def __init__(self, Game):
        self.Name = "Spell12"


class Spell13:
    def __init__(self, Game):
        self.Name = "Spell13"


class Spell14:
    def __init__(self, Game):
        self.Name = "Spell14"


class Spell15:
    def __init__(self, Game):
        self.Name = "Spell15"


class Spell16:
    def __init__(self, Game):
        self.Name = "Spell16"


class Spell17:
    def __init__(self, Game):
        self.Name = "Spell17"


# Water
class Spell18:
    def __init__(self, Game):
        self.Name = "Spell18"


class Spell19:
    def __init__(self, Game):
        self.Name = "Spell9"


class Spell20:
    def __init__(self, Game):
        self.Name = "Spell20"


class Spell21:
    def __init__(self, Game):
        self.Name = "Spell21"


class Spell22:
    def __init__(self, Game):
        self.Name = "Spell22"


class Spell23:
    def __init__(self, Game):
        self.Name = "Spell23"


# Shadow
class Spell24:
    def __init__(self, Game):
        self.Name = "Spell24"


class Spell25:
    def __init__(self, Game):
        self.Name = "Spell25"


class Spell26:
    def __init__(self, Game):
        self.Name = "Spell26"


# Light
class Spell27:
    def __init__(self, Game):
        self.Name = "Spell27"


class Spell28:
    def __init__(self, Game):
        self.Name = "Spell28"


class Spell29:
    def __init__(self, Game):
        self.Name = "Spell29"


def Spell(Game, item):
    exec("global spell\nspell = " + "Spell" + str(item) + "(Game)")
    global spell
    return spell


del pygame
