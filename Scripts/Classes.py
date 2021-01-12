import pygame


"""=====  Game [1]  ====="""


class Game:
	def __init__(self):
		self.Player = Player()
		self.pressed = {}


"""=====  Player [2]  ====="""


class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 3

		self.image = pygame.image.load("Assets/Visual/mystique.png")
		self.rect = self.image.get_rect()

		self.rect.x = 50
		self.rect.y = 282

		self.MinX = -20
		self.MaxX = 550

		self.MinY = 0
		self.MaxY = 282

	def Move_Right(self):
		self.rect.x += self.Speed

	def Move_Left(self):
		self.rect.x -= self.Speed
