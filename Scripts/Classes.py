import pygame


class Game:
	def __init__(self):
		self.Player = Player()


class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.Pv = 100
		self.MaxPv = 100
		self.Damage = 10
		self.Speed = 5
		self.Visual = pygame.image.load("Assets/Visual/mystique.png")
		self.HitBox = self.Visual.get_rect()
		self.HitBox.x = 50
		self.HitBox.y = 282
		self.MinX = 0
		self.MaxX = 520
		self.MinY = 0
		self.maxY = 282
