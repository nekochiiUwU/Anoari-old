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

		self.Force = Force()

		# Statistiques
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 3

		# Definit l'élément visuels en tant que variable
		self.image = pygame.image.load("Assets/Visual/mystique.png")
		self.Position = self.image.get_rect()

		# Position de Player
		self.Position.x = 50
		self.Position.y = 282

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x)
		self.MinX = -20
		self.MaxX = 550

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y)
		self.MinY = 0
		self.MaxY = 282

	# Fonction de mouvement (Droite)
	def Move_Right(self):
		self.Force.x += self.Speed

	# Fonction de mouvement (Gauche)
	def Move_Left(self):
		self.Force.x -= self.Speed


#  Contient les vecteurs physiques
class Force:
	def __init__(self):

		self.x = 0
		self.y = 0
		self.stepX = 0
		self.stepY = 0
		self.lastx = 0
		self.lasty = 0

	def AccelerationFunctionX(self):

		self.StepX = self.x + self.lastx / 2

		if -1 < self.StepX < 1:
			self.StepX = 0
			self.lastx = self.StepX
			return 0
		else:
			self.lastx = self.StepX
			return self.StepX

	def AccelerationFunctionY(self):

		self.StepY = self.y + self.lasty / 2

		if -1 < self.StepY < 1:
			self.StepY = 0
			self.lasty = self.StepY
			return 0
		else:
			self.lasty = self.StepY
			return self.StepY