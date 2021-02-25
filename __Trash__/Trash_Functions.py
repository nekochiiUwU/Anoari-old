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