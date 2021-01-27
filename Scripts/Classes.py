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

		self.Plateform = Plateform()

		#Création du groupe composé de tous les joueurs -Steven
		self.all_Player = pygame.sprite.Group()
		self.all_Player.add(self.Player)

		#Création du groupe composé de toutes les plateformes -Steven
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

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x) -tremisabdoul
		self.MinX = +20
		self.MaxX = 1200

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y) -tremisabdoul
		self.MinY = -20
		self.MaxY = 740

	# Fonction de collisions en fonction du rect -tremisabdoul
	def check_collisions(self, sprite, group):
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
	def Gravity(self, Game0):
		Collide = Game0.Player.check_collisions(Game0.Player, Game0.all_platform)
		if not Collide:

			if self.Base_Gravity < 33:
				self.Base_Gravity += 0.66  # Diminution
				return self.Base_Gravity

			else:
				self.Base_Gravity = 33  # Vitesse max de gravité
				return 33

		else:
			Game0.Player.SpeedY = 0  # Cancel le saut
			Apply = Collide[0].rect.top - Game0.Player.rect.bottom + 1  # Y reset (dernier pixel du rect de plateforme)
			self.Base_Gravity = 0  # Reset la force du sol
			return Apply


"""=====  Game.Sol [3]  ====="""


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

	def NewPlateform(self, Screen, x, y):
		P = [x, y]
		self.rect.x = x
		self.rect.y = y
		Screen.blit(self.image, P)


"""=====  Game.Mouse [4]  ====="""


class Mouse(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()

		pygame.mouse.set_visible(False)

		self.image = pygame.image.load("Assets/Visual/UI/Mouse.png")
		self.image = pygame.transform.scale(self.image, (33, 33))

		self.rect = self.image.get_rect()
		self.rect = self.image.get_rect(center=self.rect.center)
