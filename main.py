# -*- coding: utf-8 -*-

# import pygame
from Scripts.Classes import *


def Display():
	pygame.init()
	pygame.display.set_caption("Anatori")
	Screen = pygame.display.set_mode((640, 480))
	return Screen


# Execute les fonctions (On va déplacer ca plus tard dans un autre fichier)
Screen = Display()
Game = Game()

# Definit les éléments visuels en tant que variable (On va déplacer ca plus tard dans un autre fichier)
font = pygame.image.load("Assets/Visual/background_cave.png")
ground = pygame.image.load("Assets/Visual/ground.jpg")


Running = True


while Running:

	Screen.blit(font, (-1000, -1000))
	Screen.blit(ground, (0, 400))
	Screen.blit(Game.Player.Visual, Game.Player.HitBox)

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

pygame.quit()
