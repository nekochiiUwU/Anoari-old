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
		self.Pv = 100 #> à définir en global
		self.MaxPv = 100 #> doit prendre en compte le niveau
		self.Damage = 10 #> formule prenant en compte le niveau et l'arme, rien à faire ici
		self.Speed = 3 #> à définir en global, à diviser en speedX et speedY

		# Definit l'élément visuels en tant que variable
		self.image = pygame.image.load("Assets/Visual/mystique.png")
		self.rect = self.image.get_rect()

		# Position de Player
		self.pos.x = 50 #rect = hitbox, pas position. donc j'ai modifié rect en pos et puis uwu▒à définir en global
		self.pos.y = 282 #rect = hitbox, pas position. donc j'ai modifié rect en pos et puis uwu▒à définir en global

		# Valeurs max et min que Player peut atteindre (Bords de l'écran x)
		self.MinX = -20 #inutile
		self.MaxX = 550 #à définir en global

		# Valeurs max et min que Player peut atteindre (Bords de l'écran y)
		self.MinY = 0 #à définir en global
		self.MaxY = 282 #inutile

	# Fonction de mouvement (Droite)
	def Move_Right(self):
		self.pos.x += self.Speed # rect > pos

	# Fonction de mouvement (Gauche)
	def Move_Left(self):
		self.pos.x -= self.Speed #rect > pos
