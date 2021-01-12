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

		self.Visual = pygame.image.load("Assets/Visual/mystique.png")
		self.rect = self.Visual.get_rect()

		self.rect.x = 50
		self.rect.y = 282

		self.MinX = -20
		self.MaxX = 550

		self.MinY = 0
		self.MaxY = 282

		self.Projectiles = pygame.sprite.Group()

	def Lunch_Projectile(self):
		self.Projectiles.add(Projectile(self))

	def Move_Right(self):
		self.rect.x += self.Speed

	def Move_Left(self):
		self.rect.x -= self.Speed


"""=====  Projectile [3]  ====="""


class Projectile(pygame.sprite.Sprite):

	def __init__(self, player):

		super().__init__()

		self.speed = 4

		self.image = pygame.image.load("Assets/Visual/projectile.png")
		self.image = pygame.transform.scale(self.image, (10, 10))
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x + 80
		self.rect.y = player.rect.y + 45

	def move(self ):

		super().__init__()
		self.rect.x += self.speed

		if self.rect.x > 640 or self.rect.x < 0 \
			or self.rect.y > 480 or self.rect.y < 0:

			Player. Projectiles.remove(self)


"""=====   [4]  ====="""
