# -*- coding: utf-8 -*-

# import pygame
from Scripts.Classes import *


Game = Game()
Mob1 = Mob1()

def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    Screen = pygame.display.set_mode((640, 480))
    return Screen


# Execute les fonctions (On va déplacer ca plus tard dans un autre fichier)
Screen = Display()

# Definit les éléments visuels en tant que variable (On va déplacer ca plus tard dans un autre fichier)
font = pygame.image.load("Assets/Visual/background_cave.png")
ground = pygame.image.load("Assets/Visual/ground.jpg")


Running = True


while Running:


    for Projectile in Game.Player.Projectiles:
        Projectile.move()
        print("Nombre de Projectiles éfféctifs:", Game.Player.Projectiles)

    Screen.blit(font, (-1000, -1000))
    Screen.blit(ground, (0, 400))
    Game.Player.Projectiles.draw(Screen)
    Game.Mobs.draw(Screen)
    Screen.blit(Game.Player.image, Game.Player.rect)

    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:

        Game.Player.Move_Right()

    elif Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:

        Game.Player.Move_Left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                Game.Player.Lunch_Projectile()

        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False
