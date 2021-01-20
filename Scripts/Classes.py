import pygame

"""=====  Game [1]  ====="""


class Game:

	# Fonction éxécuté au démarrage de Game -tremisabdoul
	def __init__(self):

		# Player deviens une sous-classe de Game -tremisabdoul
		self.Player = Player()
		# Sol deviens une sous-classe de Game -Steven
		self.Sol = Sol()

		#Création du groupe composé de tous les joueurs -Steven
		self.all_Player = pygame.sprite.Group()
		self.all_Player.add(self.Player)

		#Création du groupe composé de toutes les plateformes -Steven
		self.all_platform = pygame.sprite.Group()
		self.all_platform.add(self.Sol)

		# Contiens Les Touches Préssées -tremisabdoul
		self.pressed = {}


"""=====  Player [2]  ====="""


class Player(pygame.sprite.Sprite, Game):

	# Fonction éxécuté au démarrage de Player -tremisabdoul
	def __init__(self):
		super().__init__()

		self.pop = False

		# Force deviens une sousclasse de Player et Game est load en tant que super-classe
		self.Force = Force()
		self.Game = Game

		# Statistiques
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 7
		self.SpeedY = 0

		self.Level = 0
		self.Gold = 0

		# Definit l'élément visuels en tant que variable -tremisabdoul
		self.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame1.png")
		self.Actual_image = 1
		self.rect = self.image.get_rect()
		self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

		# Position de Player -tremisabdoul
		self.rect.x = 50
		self.rect.y = 82

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x) -tremisabdoul
		self.MinX = +10
		self.MaxX = 1280

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y) -tremisabdoul
		self.MinY = -40
		self.MaxY = 440

	def check_collisions(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	# Fonction de mouvement (Droite) -tremisabdoul
	def Move_Right(self):
		self.Force.x += self.Speed

	# Fonction de mouvement (Gauche) -tremisabdoul
	def Move_Left(self):
		self.Force.x -= self.Speed


"""=====  Player.Force [2.1]  ====="""


#  Contient les vecteurs physiques -tremisabdoul
class Force:
	def __init__(self):

		self.x = float(0)
		self.y = float(0)
		self.StepX = float(0)
		self.StepY = float(0)
		self.lastx = float(0)
		self.lasty = float(0)

		self.Base_Gravity = 100
		self.Game = Game

	def AccelerationFunctionX(self):

		# Forces appliqués + ((Forces appliqués lors de la dernière frame / 1.3) /1.1) -tremisabdoul
		self.StepX = self.x + ((self.lastx/1.3) / 1.1)

		if round(self.StepX) == 0:
			self.StepX = 0
			self.lastx = self.StepX
			self.x = 0
			return 0

		else:
			# Debug du mouvement de player
			print(self.StepX)

			self.lastx = self.StepX
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

	def Gravity(self, Game):

		if not Game.Player.check_collisions(Game.Player, Game.all_platform):
			if self.Base_Gravity < 100:
				self.Base_Gravity += 4
			return self.Base_Gravity
		else:
			y = Game.Player.check_collisions(Game.Player, Game.all_platform)[0].rect[1] - Game.Player.rect[1] -115
			self.Base_Gravity = 10
			return y


"""=====  Terrain [3]  ====="""

class Sol(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()

		# Définit l'élément visuel en tant que variable
		self.image = pygame.image.load("Assets/Visual/ground.jpg")
		self.rect = self.image.get_rect()

		# Position de la plateforme principale
		self.rect.x = 0
		self.rect.y = 700


