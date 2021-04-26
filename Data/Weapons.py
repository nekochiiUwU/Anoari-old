class DataWeapons:
    def __init__(self):

        self.Types = ["Fire", "Ice", "Air", "Stone", "Shadow", "Light"]
        self.TypesProbabilties = [23, 46, 69, 92, 96, 100]
        self.TypesLight = [70, 30, 60, 40, 5, 95]

        for item in range(30):
            print(item)
            exec("self.spell" + str(item) + " = " + "Spell" + str(item) + "()")

        self.Weapons = [
            {
                "Name": "Fire",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Ice",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Air",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Stone",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Shadow",

                "Damage": 10,
                "AttackSpeed": 1.5,

                "CritDamageMultiplicator": 2,
                "CritProbability": 10,

                "Rarety": [1, 2, 3],
                "RaretyProba": [75, 95, 100],

                "Spells": "spell"

            },
            {
                "Name": "Light",

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
        else:
            A = TypeID - 8 + TypeID * 2
        Spells = []
        for _ in range(Rarety):
            exec("self.Spell" + " = " + "self.spell" + str(Game.randint(0, 6) + A))
            Spells.append(self.Spell)

            print(self.Spell)

        for Spell in Spells:
            print(Spell.Name)
        print(TypeID, Type, Data, Rarety, sep="\n")


# Fire
class Spell0:
    def __init__(self):
        self.Name = "Spell0"


class Spell1:
    def __init__(self):
        self.Name = "Spell1"


class Spell2:
    def __init__(self):
        self.Name = "Spell2"


class Spell3:
    def __init__(self):
        self.Name = "Spell3"


class Spell4:
    def __init__(self):
        self.Name = "Spell4"


class Spell5:
    def __init__(self):
        self.Name = "Spell5"


# Ice
class Spell6:
    def __init__(self):
        self.Name = "Spell6"


class Spell7:
    def __init__(self):
        self.Name = "Spell7"


class Spell8:
    def __init__(self):
        self.Name = "Spell8"


class Spell9:
    def __init__(self):
        self.Name = "Spell9"


class Spell10:
    def __init__(self):
        self.Name = "Spell10"


class Spell11:
    def __init__(self):
        self.Name = "Spell11"


# Air
class Spell12:
    def __init__(self):
        self.Name = "Spell12"


class Spell13:
    def __init__(self):
        self.Name = "Spell13"

class Spell14:
    def __init__(self):
        self.Name = "Spell14"


class Spell15:
    def __init__(self):
        self.Name = "Spell15"


class Spell16:
    def __init__(self):
        self.Name = "Spell16"


class Spell17:
    def __init__(self):
        self.Name = "Spell17"


# Stone
class Spell18:
    def __init__(self):
        self.Name = "Spell18"


class Spell19:
    def __init__(self):
        self.Name = "Spell9"


class Spell20:
    def __init__(self):
        self.Name = "Spell20"


class Spell21:
    def __init__(self):
        self.Name = "Spell21"


class Spell22:
    def __init__(self):
        self.Name = "Spell22"


class Spell23:
    def __init__(self):
        self.Name = "Spell23"


# Shadow
class Spell24:
    def __init__(self):
        self.Name = "Spell24"


class Spell25:
    def __init__(self):
        self.Name = "Spell25"


class Spell26:
    def __init__(self):
        self.Name = "Spell26"


# Light
class Spell27:
    def __init__(self):
        self.Name = "Spell27"


class Spell28:
    def __init__(self):
        self.Name = "Spell28"


class Spell29:
    def __init__(self):
        self.Name = "Spell29"
