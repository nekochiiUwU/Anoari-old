"""
for Monster in Game.all_Monster:
    Monster.Life(Screen, Game)
    if Game.Monster.LeftDirection :
        Monster.Move_Left()
        if Game.Player.check_collisions(Monster, Game.all_platformsub) :
             Game.Monster.LeftDirection = False
    else :
        Monster.Move_Right()
        if Game.Player.check_collisions(Monster, Game.all_platformsub) :
            Game.Monster.LeftDirection = True
            Game.Monster.RightDirection = False


            # wall tp across (movement())
            if Wall.rect.right > Target.rect.left > Wall.rect.left:
                print("Gauche")
                Game.Position = Wall.rect.left - (Target.rect.right + 1)
            elif Wall.rect.right > Target.rect.right > Wall.rect.left:
                print("Droite")
                Game.Position = Wall.rect.right - (Target.rect.left - 1)
"""