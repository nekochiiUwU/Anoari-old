# -*- coding: utf-8 -*-

# Importe le fichier Classes et Time
from Scripts.Classes import *
import time

# Execute les Classes
Game = Game()

frame = 0

# Crée l'écran
def Display():
    pygame.init()
    pygame.display.set_caption("Anatori")
    screen = pygame.display.set_mode((640, 480))
    return screen


# L'écran est stockée dans une variable
Screen = Display()

# Definit les éléments visuels en tant que variable
font = pygame.image.load("Assets/Visual/background_cave.png")
ground = pygame.image.load("Assets/Visual/ground.jpg")


Running = True

# Contient tout ce qui est fait pendant que le jeu est run
while Running:

    tick = time.time()


    # Affiche a l'écran des éléments
    Screen.blit(font, (-1000, -1000))
    Screen.blit(ground, (0, 400))
    Screen.blit(Game.Player.image, Game.Player.rect)

    # Déplacement du joueur (x)
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:

        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        # On doit pouvoir simplifier "Game.pressed.get(pygame.K_)" en le définissant comme un truc plus court,
        # ça pourrait être pratique▒ rect > pos
        Game.Player.Move_Left()

    # Met a jour l'affichage > rafraîchissement de l'écran en language professionnel
    pygame.display.flip()

    # Check les input et instances
    for event in pygame.event.get():

        # Touches enfoncées
        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

        # Touches relachées
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Programme de pause: Touche "p"
        if Game.pressed.get(pygame.K_p):
            Pause = True
            print("Pause")

            while Pause:

                # Programme d'Unpause: Touche "p"
                for event in pygame.event.get():

                    if Game.pressed.get(pygame.K_p):
                        time.sleep(0.2)
                        Pause = False
                        print("UnPause")
                    else:
                        print("[p] for unpause")

        # Bouton croix en haut a droite (Fermer le Programme)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Debug des input clavier
    # print(Game.pressed)


    if not Game.Player.Force.x:
        x = 0

        if Game.Player.Actual_image == 1:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
            Game.Player.Actual_image = 2
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 2:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame3.png")
            Game.Player.Actual_image = 3
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 3:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame4.png")
            Game.Player.Actual_image = 4
            Game.Player.rect.y += 1

        elif Game.Player.Actual_image == 4:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame5.png")
            Game.Player.Actual_image = 5
            Game.Player.rect.y -= 1

        elif Game.Player.Actual_image == 5:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame6.png")
            Game.Player.Actual_image = 6
            Game.Player.rect.y -= 1

        elif Game.Player.Actual_image == 6:

            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame1.png")
            Game.Player.Actual_image = 1
            Game.Player.rect.y -= 1
    else:
        x = 0

#        elif Game.Player.Actual_image == -1:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2
#
#        elif Game.Player.Actual_image == -2:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2
#
#        elif Game.Player.Actual_image == -3:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2
#
#        elif Game.Player.Actual_image == -4:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2
#
#        elif Game.Player.Actual_image == -5:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2
#
#        elif Game.Player.Actual_image == -5:
#            Game.Player.image = pygame.image.load("Assets/Visual/Mystique_resp/Frame2.png")
#            Game.Player.Actual_image == 2

    Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Player.rect.y += Game.Player.Force.AccelerationFunctionY()

    tickcheck = time.time()
    tickchecker = tick - tickcheck

    print("FPS =", frame)

    while tickchecker < 0.019:
        tickcheck = time.time()
        tickchecker =  tickcheck - tick
    frame = 1
    frame = frame / tickchecker



