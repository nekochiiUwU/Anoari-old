# -*- coding: utf-8 -*-

# Ecrivez une description de ce que vous codez
# avec votre pseudo pour qu'on puisse vous demander plus d'infos -tremisabdoul

# Importe le fichier Classes Functions et time -tremisabdoul
from Scripts.Classes import *
from Scripts.Functions import *
import time

# Execute les Classes -tremisabdoul
Game = Game()

# Valeurs qui vont servir plus tard
# (faites gaffe les valeurs peuvent crash si vous en supprimez certeines) -tremisabdoul
frame = 0
nbframe = 0
fps = 0
event = 0

# L'écran est stockée dans une variable -tremisabdoul
Screen = Display()

# Definit les éléments visuels en tant que variable -tremisabdoul
font = pygame.image.load("Assets/Visual/background_cave.png")
ground = pygame.image.load("Assets/Visual/ground.jpg")


Running = True

# Contient tout ce qui est fait pendant que le jeu est run -tremisabdoul
while Running:

    tick = time.time()
    nbframe += 1
    if nbframe % 10 == 0:
        nbframe10 = True
    else:
        nbframe10 = False

    # Affiche a l'écran des éléments -tremisabdoul
    Screen.blit(font, (-1000, -1000))
    Screen.blit(ground, (0, 400))
    Screen.blit(Game.Player.image, Game.Player.rect)

    #font = pygame.Surface.Font("Assets/Font/8-BIT WONDER.TTF", 30)
    #printfps = font.render(str(fps), 1, (255, 255, 255))
    #Screen.blit(printfps, (6, 32))

    # Check les input et instances -tremisabdoul
    for event in pygame.event.get():

        # Touches enfoncées -tremisabdoul
        if event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True

        # Touches relachées -tremisabdoul
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False

        # Programme de pause: Touche "p" -tremisabdoul
        if Game.pressed.get(pygame.K_p):
            Pause = True
            print("Pause")

            while Pause:

                # Programme d'Unpause: Touche "p" -tremisabdoul
                for event in pygame.event.get():

                    if Game.pressed.get(pygame.K_p):
                        time.sleep(0.2)
                        Pause = False
                        print("UnPause")
                    else:
                        print("[p] for unpause")

        # Bouton croix en haut a droite (Fermer le Programme) -tremisabdoul
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Déplacement du joueur (x) (Impossible aux limites de l'écran): Touche q / d et LEFT / RIGHT -tremisabdoul
    if Game.pressed.get(pygame.K_d) and Game.Player.rect.x < Game.Player.MaxX \
            or Game.pressed.get(pygame.K_RIGHT) and Game.Player.rect.x < Game.Player.MaxX:
        Game.Player.Move_Right()

    if Game.pressed.get(pygame.K_q) and Game.Player.rect.x > Game.Player.MinX \
            or Game.pressed.get(pygame.K_LEFT) and Game.Player.rect.x > Game.Player.MinX:
        Game.Player.Move_Left()

    # Opération éfféctuée toutes les 10 frames -tremisabdoul
    if not nbframe10 == 0:
        # Animation de respiration (sorcière)
        resp_sorciere(Game)
        # Debug des fps
        print("FPS =", round(fps), "/ 50.251")

    Game.Player.rect.x += Game.Player.Force.AccelerationFunctionX()
    Game.Player.rect.y += Game.Player.Force.AccelerationFunctionY()

    tickcheck = time.time()
    tickchecker = tick - tickcheck

    # Met a jour l'affichage (rafraîchissement de l'écran) -tremisabdoul
    pygame.display.flip()

    while tickchecker < 0.0199:
        tickcheck = time.time()
        tickchecker = tickcheck - tick

    if frame < 10:
        timeframe = + tickchecker
        frame = + 1
        fps = frame / tickchecker
    else:
        timeframe = tickchecker
        frame = 1
        fps = frame / tickchecker
