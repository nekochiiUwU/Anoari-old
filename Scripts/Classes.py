import pygame


"""=====  Game [1]  ====="""


class Game:

	# Fonction éxécuté au démarrage de Game
	def __init__(self):

		# Player deviens une sous-classe de Game
		self.Player = Player()

		# Contiens Les Touches Préssées
		self.pressed = {}

	def check_collisions(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


"""=====  Player [2]  ====="""


class Player(pygame.sprite.Sprite, Game):

	# Fonction éxécuté au démarrage de Player
	def __init__(self):
		super().__init__()

		self.Force = Force()
		self.Game = Game
		# Statistiques
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 2.5

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
		self.Force.x += self.Speed

	# Fonction de mouvement (Gauche)
	def Move_Left(self):
		self.Force.x -= self.Speed


#  Contient les vecteurs physiques
class Force:
	def __init__(self):

		self.x = float(0)
		self.y = float(0)
		self.StepX = float(0)
		self.StepY = float(0)
		self.lastx = float(0)
		self.lasty = float(0)

	def AccelerationFunctionX(self):

		# Forces appliquées + Forces appliquées lors de la dernière frame /1.2
		self.StepX = self.x + ((self.lastx/1.3) / 1.1)

		if round(self.StepX) == 0 :
			self.StepX = 0
			self.lastx = self.StepX
			self.x = 0
			return 0

		else:
			self.lastx = self.StepX
			print(self.StepX, "=", (self.x/2), "+", (self.lastx/5)/1.1)
			self.x = 0
			return self.StepX

	def AccelerationFunctionY(self):

		self.StepY = self.y + self.lasty / 2

		if -1 < self.StepY < 1:
			self.StepY = 0
			self.lasty = self.StepY
			self.y = 0
			return 0
		else:
			self.lasty = self.StepY
			self.y = 0
			return self.StepY
