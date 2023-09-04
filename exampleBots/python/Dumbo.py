import libpyAI as ai
def AI_loop():
    #Release keys
    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)
    #Set variables
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())
    frontWall = ai.wallFeeler(1000, heading)
    leftWall = ai.wallFeeler(1000, heading - 90)
    rightWall = ai.wallFeeler(1000, heading + 90)
    backWall = ai.wallFeeler(1000, heading - 180)
    trackWall = ai.wallFeeler(1000, tracking)
    #Thrust rules
    if ai.selfSpeed() <= 5 and frontWall >= 500:
        ai.thrust(1)
    elif backWall < 350 and ai.wallFeeler(500, heading) == 500:
        ai.thrust(1)
    #Turn rules
    if leftWall > rightWall:
        ai.turnRight(1)
    else:
        ai.turnLeft(1)
    #Just keep shooting
    ai.fireShot()
ai.start(AI_loop,["-name","Dumbo"])
