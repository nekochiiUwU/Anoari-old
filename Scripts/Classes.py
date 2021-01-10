import pygame


class Game:
	def __init__(self):
		self.Player = Player()
		self.pressed = {}

class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 3

		self.Visual = pygame.image.load("Assets/Visual/mystique.png")
		self.HitBox = self.Visual.get_rect()
		self.rect = self.HitBox

		self.HitBox.x = 50
		self.HitBox.y = 282

		self.MinX = -20
		self.MaxX = 550

		self.MinY = 0
		self.MaxY = 282

		self.Projectiles = pygame.sprite.Group()

	def Lunch_Projectile(self):
		self.Projectiles.add(Projectile())

	def Move_Right(self):
		self.HitBox.x += self.Speed

	def Move_Left(self):
		self.HitBox.x -= self.Speed

class Projectile(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.speed = 4

		self.image = pygame.image.load ("Assets/Visual/projectile.png")
		self.image = pygame.transform.scale(self.image, (15, 15))
		self.HitBox = self.image.get_rect()
		self.rect = self.HitBox