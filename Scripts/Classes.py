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

		self.Projectiles = pygame.sprite.Group()

	def Lunch_Projectile(self):
		self.Projectiles.add(Projectile(self))

	def Move_Right(self):
		self.rect.x += self.Speed

	def Move_Left(self):
		self.rect.x -= self.Speed


"""=====  Projectile [3]  ====="""


class Projectile(pygame.sprite.Sprite):

	def __init__(self, Player):
		super().__init__()

		self.speed = 4
		self.Player = Player
		self.image = pygame.image.load("Assets/Visual/projectile.png")
		self.image = pygame.transform.scale(self.image, (10, 10))
		self.rect = self.image.get_rect()
		self.rect.x = Player.rect.x + 80
		self.rect.y = Player.rect.y + 45
		self.origin_image = self.image
		self.angle = 0

	def rotation(self):
		self.angle += 5
		self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
		self.rect = self.image.get_rect(center = self.rect.center)

	def remove(self):
		self.Player.Projectiles.remove(self)


	def move(self):
		self.rect.x += self.speed
		self.rotation()

		if self.rect.x > 640 or self.rect.x < 0 \
				or self.rect.y > 480 or self.rect.y < 0:

			self.remove()


"""=====  Mob [4]  ====="""


class Mob1(pygame.sprite.Sprite):

	def __init__(self):

		super().__init__()
		self.Pv = 10
		self.MaxPv = 10
		self.Damage = 6
		self.Speed = 2

		self.image = pygame.image.load("Assets/Visual/mystique.png")
		self.rect = self.image.get_rect()

		self.rect.x = 50
		self.rect.y = 282

		self.MinX = -20
		self.MaxX = 550

		self.MinY = 0
		self.MaxY = 282