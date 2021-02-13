def resp_sorciere(Game):

    if not Game.Player.Force.x:

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

for Monster in Game.all_Monster:
    Monster.Life(Screen)
    if Game.Monster.LeftDirection :
        Monster.Move_Left()
        if Game.Player.check_collisions(Monster, Game.all_platformsub) :
             Game.Monster.LeftDirection = False
    else :
        Monster.Move_Right()
        if Game.Player.check_collisions(Monster, Game.all_platformsub) :
            Game.Monster.LeftDirection = True
            Game.Monster.RightDirection = False