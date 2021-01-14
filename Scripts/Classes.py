import pygame


"""=====  Game [1]  ====="""


class Game:

	# Fonction éxécuté au démarrage de Game
	def __init__(self):

		# Une condition qui va être exécuté seulement a la création du perso (a déplacer) [if Class == "SorcierInit":]
		self.Class = "SorcierInit"

		# Player deviens une sous-classe de Game
		self.Player = Player()

		# Contiens Les Touches Préssées
		self.pressed = {}


"""=====  Player [2]  ====="""


class Player(pygame.sprite.Sprite):

	# Fonction éxécuté au démarrage de Player
	def __init__(self):
		super().__init__()

		# Statistiques
		self.Level = 1

		self.Pv = 100
		self.MaxPv = 85 + self.Level * 15  # Level 1: 100Pv > Level 2: 115Pv > (etc.)
		self.Attack = 9 + self.Level * 1  # Level 1: 10Atk > Level 2: 11Atk > (etc.)
		self.Speed = 3

		#  Attributs
		self.Weapon = "Staff1"
		self.Armor = "ArmorWeak1"

		# Gold
		self.Gold = 7

		# Definit l'élément visuels en tant que variable
		self.image = pygame.image.load("Assets/Visual/mystique.png")

		# Récupérer l'origine de la hitbox de player(Position)
		self.rect = self.image.get_rect()

		# Position de Player
		self.rect.x = 50
		self.rect.y = 282

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x)
		self.MinX = -20
		self.MaxX = 550

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y)
		self.MinY = 0
		self.MaxY = 282

	# Fonction de mouvement (Droite)
	def Move_Right(self):
		self.rect.x += self.Speed

	# Fonction de mouvement (Gauche)
	def Move_Left(self):
		self.rect.x -= self.Speed
