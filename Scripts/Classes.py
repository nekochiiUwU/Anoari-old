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
		self.Actual_image = 1
		self.rect = self.image.get_rect()
		self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

		# Position de Player -tremisabdoul
		self.rect.x = 50
		self.rect.y = 82

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x) -tremisabdoul
		self.MinX = +20
		self.MaxX = 1200

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y) -tremisabdoul
		self.MinY = -40
		self.MaxY = 440

	# Fonction de collisions en fonction du rect -tremisabdoul
	def check_collisions(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_rect)

	# Fonction de mouvement (Droite) -tremisabdoul
	def Move_Right(self):
		self.Force.x += self.Speed
		self.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame1.png")

	# Fonction de mouvement (Gauche) -tremisabdoul
	def Move_Left(self):
		self.Force.x -= self.Speed
		self.image = pygame.image.load("Assets/Visual/Mystique_resp/Left/1.png")


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
		self.StepX = self.x + ((self.lastx/1.3) / 1.1)

		if round(self.StepX) == 0:
			self.StepX = 0
			self.lastx = self.StepX
			self.x = 0
			return 0

		else:
			self.lastx = self.StepX
			self.x = 0
			return self.StepX

	""" vv Pour l'instent pas nessesaire vv """

	#def AccelerationFunctionY(self):
	#
	#	self.StepY = self.y + self.lasty / 2
	#
	#	if -1 < self.StepY < 1:
	#		self.StepY = 0
	#		self.lasty = self.StepY
	#		self.y = 0
	#		return 0
	#	else:
	#		self.lasty = self.StepY
	#		self.y = 0
	#		return self.StepY

	""" ^^ Pour l'instent pas nessesaire ^^ """

	# Faut se dire que la gravité a une force de 20 et que lorsque
	# Base_Gravity est a 0 c'est que la force appliquée par le sol est de -20
	def Gravity(self, Game):

		if not Game.Player.check_collisions(Game.Player, Game.all_platform):
			if self.Base_Gravity < 100:
				self.Base_Gravity += 0.6
			return self.Base_Gravity
		else:
			y = Game.Player.check_collisions(Game.Player, Game.all_platform)[0].rect[1] - Game.Player.rect[1] - 115
			self.Base_Gravity = 0
			return y


"""=====  Game.Sol [3]  ====="""


class Sol(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()

		# Définit l'élément visuel en tant que variable -steven
		self.image = pygame.image.load("Assets/Visual/plateforme_base.png")
		# Transforme l'image sol en la resolution indiquée vv vv -tremisabdoul
		self.image = pygame.transform.scale(self.image, (1280, 20))
		# Définit la hitbox de sol -steven
		self.rect = self.image.get_rect()

		# Position de la plateforme principale -steven
		self.rect.x = 0
		self.rect.y = 700
