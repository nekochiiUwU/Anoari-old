#
#
#import pygame
#
#=====  Projectile [3]  =====
#
#
#class Projectile(pygame.sprite.Sprite):
#
#    def __init__(self):
#
#        self.speed = 4
#        self.Game = Game()
#        self.image = pygame.image.load("Assets/Visual/projectile.png")
#        self.image = pygame.transform.scale(self.image, (10, 10))
#        self.rect = self.image.get_rect()
#        self.rect.x = self.Game.Player.rect.x + 80
#        self.rect.y = self.Game.Player.rect.y + 45
#        self.origin_image = self.image
#        self.angle = 0
#
#    def rotation(self):
#        self.angle += 5
#        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
#        self.rect = self.image.get_rect(center=self.rect.center)
#
#    def remove(self):
#        Projectiles.remove(self)
#
#    def move(self):
#        self.rect.x += self.speed
#        self.rotation()
#
#        if self.rect.x > 640 or self.rect.x < 0 \
#                or self.rect.y > 480 or self.rect.y < 0:
#
#            self.remove()
#
#
#Projectiles = pygame.sprite.Group()
#
#Projectile = Projectile()
#
#
#def Lunch_Projectile(Projectile):
#
#   Projectiles.add(Projectile)
#
#
#=====  Mob [4]  =====
#
#
#class Mob1(pygame.sprite.Sprite):
#
#    def __init__(self):
#
#        super().__init__()
#        self.Pv = 10
#        self.MaxPv = 10
#        self.Damage = 6
#        self.Speed = 2
#        self.image = pygame.image.load("Assets/Visual/humain.png")
#        self.image = pygame.transform.scale(self.image, (100, 100))
#        self.rect = self.image.get_rect()
#
#        self.rect.x = 500
#        self.rect.y = 302
#
#        self.MinX = -20
#        self.MaxX = 550
#
#        self.MinY = 0
#        self.MaxY = 282
#
#        self.MovementCheck = 0
#
#    def walk1(self):
#        self.MovementCheck = self.rect.x
#        self.rect.x -= self.Speed
#        self.MovementCheck = self.MovementCheck - self.rect.x
#        return self.MovementCheck
#
#    def walk2(self):
#        self.MovementCheck = self.rect.x
#        self.rect.x += self.Speed
#        self.MovementCheck = self.MovementCheck - self.rect.x
#        return self.MovementCheck
#
#
#Mobs = pygame.sprite.Group()
#
#
#def spawn_Mob1():
#    NewMob1 = Mob1()
#    Mobs.add(NewMob1)
#
#
#spawn_Mob1()
