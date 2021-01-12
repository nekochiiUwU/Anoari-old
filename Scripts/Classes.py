import pygame


"""=====  Game [1]  ====="""


class Game:

	# Fonction éxécuté au démarrage de Game
	def __init__(self):

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
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 3

		# Definit l'élément visuels en tant que variable
		self.image = pygame.image.load("Assets/Visual/mystique.png")
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
