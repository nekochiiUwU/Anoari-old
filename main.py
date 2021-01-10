# -*- coding: utf-8 -*-

import pygame
import sys
sys.path.insert(1, '\Scripts')
import Classes

'''   !!!!   Faut que je refasse l'import   !!!!   '''


pygame.init()


pygame.display.set_caption("Ca Marche ?")
Screen = pygame.display.set_mode((640, 480))

font = pygame.image.load("Assets/Visual/background_cave.png")

ground = pygame.image.load("Assets/Visual/ground.jpg")
Game = Game()




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