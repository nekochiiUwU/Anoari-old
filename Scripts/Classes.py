import pygame

"""=====  Game [1]  ====="""


class Game:

    # Fonction éxécuté au démarrage de Game -tremisabdoul
    def __init__(self):
        # Player deviens une sous-classe de Game -tremisabdoul
        self.Player = Player()
        # Sol deviens une sous-classe de Game -Steven
        self.Sol = Sol()
        # Mouse deviens une sous-classe de Game -tremisabdoul
        self.Mouse = Mouse()
        self.UI = UI()
        self.Plateform = Plateform()

        # Création du groupe composé de tous les joueurs -Steven
        self.all_Player = pygame.sprite.Group()
        self.all_Player.add(self.Player)

        # Création du groupe composé de toutes les plateformes -Steven
        self.all_platform = pygame.sprite.Group()
        self.all_platform.add(self.Sol)
        self.all_platform.add(self.Plateform)

        # Contiens Les Touches Préssées -tremisabdoul
        self.pressed = {}


"""=====  Game.Player [2]  ====="""


class Player(pygame.sprite.Sprite, Game):

    # Fonction éxécuté au démarrage de Player -tremisabdoul
    def __init__(self):
        super().__init__()

        self.pop = False

        # Force deviens une sous-classe de Player et Game est load en tant que super-classe -tremisabdoul
        self.Force = Force()
        self.Game = Game

        # Statistiques -tremisabdoul
        self.Pv = 50
        self.MaxPv = 100
        self.Damage = 10
        self.Speed = 3
        self.SpeedY = 0

        self.Level = 0
        self.Gold = 0

        # Definit l'élément visuels en tant que variable -tremisabdoul
        self.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame1.png")
        self.imageTag = 1
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

        # Position de Player -tremisabdoul
        self.rect.x = 50
        self.rect.y = 82

        self.LastY = 0
        self.YVector = 0

        # Valeurs max et min que Player peut atteindre (Bords de l'écran x) -tremisabdoul
        self.MinX = +20
        self.MaxX = 1200

        # Valeurs max et min que Player peut atteindre (Bords de l'écran y) -tremisabdoul
        self.MinY = -20
        self.MaxY = 740

    #def Check_Collisions(rectA, rectB):
    #    if rectB.right < rectA.left:
    #        # rectB est à gauche
    #        return False
    #    if rectB.bottom < rectA.top:
    #        # rectB est au-dessus
    #        return False
    #    if rectB.left > rectA.right:
    #        # rectB est à droite
    #        return False
    #    if rectB.top > rectA.bottom:
    #        # rectB est en-dessous
    #        return False

    # Fonction de collisions en fonction du rect -tremisabdoul

    @staticmethod
    def check_collisions(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Fonction de mouvement (Droite) -tremisabdoul
    def Move_Right(self):
        self.Force.x += self.Speed
        self.imageTag = 1

    # Fonction de mouvement (Gauche) -tremisabdoul
    def Move_Left(self):
        self.Force.x -= self.Speed
        self.imageTag = -1


"""=====  Game.Player.Force [2.1]  ====="""


#  Contient les vecteurs physiques -tremisabdoul
class Force:

    # Fonction exécutée au demarée au lancement de Force
    def __init__(self):

        self.x = float(0)
        self.y = float(0)
        self.StepX = float(0)
        self.StepY = float(0)
        self.lastx = float(0)
        self.lasty = float(0)

        self.Base_Gravity = 0
        self.Game = Game

    # Fonction permettant un mouvement fluide -tremisabdoul
    def AccelerationFunctionX(self):

        # Forces appliqués + ((Forces appliqués lors de la dernière frame / 1.3) / 1.1) -tremisabdoul
        self.StepX = self.x + ((self.lastx / 1.3) / 1.1)

        if round(self.StepX) == 0:
            self.StepX = 0
            self.lastx = self.StepX
            self.x = 0
            return 0

        else:
            self.lastx = self.StepX
            self.x = 0
            return self.StepX

    # Faut se dire que la gravité a une force de 33 et que lorsque
    # Base_Gravity est a 0 c'est que la force appliquée par le sol est de -33
    def Gravity(self, Game0):

        # Verification des collisions entre Player et toutes les plateformes
        Collide = Game0.Player.check_collisions(Game0.Player, Game0.all_platform)

        if not Collide or Game0.Player.YVector > 0:

            if self.Base_Gravity < 33:  # Si force de sol > 0
                self.Base_Gravity += 0.66  # Diminution de la force "Sol" (Ratio 0.66)
                return self.Base_Gravity

            else:
                self.Base_Gravity = 33  # Force de sol = 0
                return 33

        else:
            Game0.Player.SpeedY = 0  # Cancel le saut
            Apply = Collide[0].rect.top - Game0.Player.rect.bottom + 1  # Y reset (Premier pixel du rect de plateforme)
            self.Base_Gravity = 0  # Reset la force du sol (-33)
            return Apply


"""=====  Game.Sol [3]  ====="""


# Sol -steven
class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Définit l'élément visuel en tant que variable -steven
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la resolution indiquée -tremisabdoul
        self.image = pygame.transform.scale(self.image, (1280, 20))

        # Définit la hitbox de sol -steven
        self.rect = self.image.get_rect()

        # Position de la plateforme principale -steven
        self.rect.x = 0
        self.rect.y = 700


# Creation de plateforme (pas entièrement fonctionnel) -tremisabdoul
class Plateform(pygame.sprite.Sprite, Game):

    def __init__(self):
        super().__init__()

        # Définit l'élément visuel en tant que variable -steven
        self.image = pygame.image.load("Assets/Visual/plateforme_base.png")

        # Transforme l'image sol en la resolution indiquée -tremisabdoul
        self.image = pygame.transform.scale(self.image, (320, 20))

        # Définit la hitbox de sol -steven
        self.rect = self.image.get_rect()

        # Position de la plateforme -steven
        self.rect.x = 400
        self.rect.y = 520

    # Création de nouvelles plateformes (semi-fonctionnel)
    def NewPlateform(self, Screen, x1, x2, y):
        P = [x1, y]
        self.image = pygame.transform.scale(self.image, (x2 - x1, 20))
        self.rect.x = x1
        self.rect.y = y
        Screen.blit(self.image, P)


"""=====  Game.Mouse [4]  ====="""


# Sourie -tremisabdoul
class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #pygame.mouse.set_visible(False)

        self.image = pygame.image.load("Assets/Visual/UI/Mouse.png")
        self.image = pygame.transform.scale(self.image, (33, 33))

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)


"""=====  Game.UI [5]  ====="""


# Interface -tremisabdoul
class UI:

    def __init__(self):
        super().__init__()

        # Font grisé -tremisabdoul
        self.baselayer = pygame.image.load("Assets/Visual/UI/baselayer.png")
        self.baselayer = pygame.transform.scale(self.baselayer, (1280, 720))

        # Boutton "JOUER" -tremisabdoul
        self.playbuttun = pygame.image.load("Assets/Visual/UI/bouton_JOUER.png")
        self.playbuttun = pygame.transform.scale(self.playbuttun, (82, 30))
        self.playbuttunrect = self.playbuttun.get_rect()
        self.playbuttunrect.x = 640 - 41
        self.playbuttunrect.y = 360 - 15 - 75

        # Boutton "REPRENDRE" -tremisabdoul
        self.resumebuttun = pygame.image.load("Assets/Visual/UI/bouton_REPRENDRE.png")
        self.resumebuttun = pygame.transform.scale(self.resumebuttun, (140, 30))
        self.resumebuttunrect = self.resumebuttun.get_rect()
        self.resumebuttunrect.x = 640 - 70
        self.resumebuttunrect.y = 360 - 15 - 25

        # Boutton "SAUVEGARDER" -tremisabdoul
        self.savebuttun = pygame.image.load("Assets/Visual/UI/bouton_SAUVEGARDER.png")
        self.savebuttun = pygame.transform.scale(self.savebuttun, (172, 30))
        self.savebuttunrect = self.savebuttun.get_rect()
        self.savebuttunrect.x = 640 - 86
        self.savebuttunrect.y = 360 - 15 + 25

        # Boutton "QUITER" -tremisabdoul
        self.quitbuttun = pygame.image.load("Assets/Visual/UI/bouton_QUITTER.png")
        self.quitbuttun = pygame.transform.scale(self.quitbuttun, (100, 30))
        self.quitbuttunrect = self.quitbuttun.get_rect()
        self.quitbuttunrect.x = 640 - 50
        self.quitbuttunrect.y = 360 - 15 + 75
