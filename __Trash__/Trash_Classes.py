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

#"""=====  Curseur [9]  ====="""
#class Cursor(UI, Game):
#    def __init__(self):
#        super().__init__()
#
#        self.cursor_image = pygame.image.load("Assets/Visual/plateforme_base.png")
#        self.cursor_image = pygame.transform.scale(self.cursor_image, (20, 20))
#
#        self.cursor_imagerect = self.cursor_image.get_rect()
#        self.cursor_imagerect.x = 1000 - 30
#        self.cursor_imagerect.y = 330
#
#       self.state = 'JOUER'
#       self.staterect = self.staterect.x, self.staterect.y = self.lobby_playbuttonrect.x, self.lobby_loadbuttonrect.y
#
#
#   def Mouvement(self):
#
#       Screen.blit(self.cursor_image, self.cursor_imagerect)
#
#       for event in pygame.event.get():
#
#            if event.type == pygame.KEYDOWN:
#
#                if Game.pressed.get(pygame.K_DOWN):
#                    if self.state == 'JOUER' :
#                        self.cursor_imagerect = self.lobby_loadbutton.x - 30, self.lobby_loadbuttonrect.y
#                        self.state == 'CHARGER'
#                    elif self.state == 'CHARGER' :
#                        self.cursor_imagerect = self.lobby_quitbuttonrect.x - 30, self.lobby_quitbuttonrect.y
#                        self.state == 'QUITTER'
#                    elif self.state == 'QUITTER' :
#                        self.cursor_imagerect = self.lobby_playbuttonrect.x - 30, self.lobby_playbuttonrect.y
#                        self.state == 'JOUER'
#
#                if Game.pressed.get(pygame.K_UP) :
#                    if self.state == 'JOUER' :
#                        self.cursor_imagerect = self.lobby_quitbuttonrect.x - 30, self.lobby_quitbuttonrect.y
#                        self.state == 'QUITTER'
#                    elif self.state == 'CHARGER' :
#                        self.cursor_imagerect = self.lobby_playbuttonrect.x - 30, self.lobby_playbuttonrect.y
#                        self.state == 'JOUER'
#                    elif self.state == 'QUITTER' :
#                        self.cursor_imagerect = self.lobby_loadbuttonrect.x - 30, self.lobby_loadbuttonrect.y
#                        self.state == 'CHARGER'
#
#                if event.type == pygame.START :
#                    if self.state == 'JOUER' :
#                        self.Lobby = False
#                        self.InGame = True
#                    elif self.state == 'CHARGER':
#                        self.Lobby = False
#                        self.InGame = True
#                    elif self.state == 'QUITTER':
#                        self.Running = False
#                        pygame.quit()

"""
# Gravité kassé

def Gravity(self, Game0, Target):
    Collide = Game0.Player.check_collisions(Target, Game0.all_plateform)

    for item in Collide:

        if item and Target.YVector < 0 and (Target.rect.bottom < item.rect.top + 33):
            Target.SpeedY = 0
            Target.Base_Gravity = 0
            Replace = item.rect.y - (Target.rect.bottom)
            print(Replace)
            Target.YVector -= Replace
            return Replace + 1

    if not Collide:
        if Target.Base_Gravity < 33:
            Target.Base_Gravity += 0.66
            return Target.Base_Gravity

        else:
            Target.Base_Gravity = 33  # Force de sol = 0
            return 33
    return 0

"""