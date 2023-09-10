import libpyAI as ai
import math

#finds difference between two angles
def angleDiff(m, n):    
    return int(180 - abs(abs(m - n) - 180))

#Measures the difference between two headings
#returns difference in degrees
def headingDiff(m, n):
    return ((m-n) + 180) % 360 - 180

#Compute the angle between two cartesian points, relative to horizontal
def angleToPointDeg(p1, p2):
    dx = p1[0] - p2[0]
    dy = p2[1] - p1[1]
    m = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
    return headingDiff(m, ai.selfHeadingDeg())

# main loop for this agent --- a rule-based expert system
def AI_loop():

    # release keys
    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)

    nearLimit = 150 # threshold for a relatively "close" object (xp distance units)
    nearLimitThreat = 300 # threshold for a "very close" object (xp distance units)
    shotDanger = 130 # threshold for relatively "close" bullets (xp distance units)

    speedLimit = 5 # (xp speed units)
    powerHigh = 45 # (xp thrust power units)
    powerLow = 20 # (xp thrust power units)
    targetingAccuracy = 5 # tolerance from heading within which firing is OK (degrees)

    # reset everything else
    ai.setTurnSpeedDeg(20) # handicap
    ai.setPower(powerLow)

    # acquire information
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())

    feelers = []
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())
    
    frontWall = ai.wallFeeler(500, heading)
    leftWall = ai.wallFeeler(500, heading + 90)
    rightWall = ai.wallFeeler(500, heading - 90)
    trackWall = ai.wallFeeler(500, tracking)
    rearWall = ai.wallFeeler(500, heading - 180)
    backLeftWall = ai.wallFeeler(500, heading + 135)
    backRightWall = ai.wallFeeler(500, heading - 135)
    frontLeftWall = ai.wallFeeler(500, heading + 45)
    frontRightWall = ai.wallFeeler(500, heading - 45)
    
    feelers.append(frontWall)
    feelers.append(leftWall)
    feelers.append(rightWall)
    feelers.append(trackWall)
    feelers.append(rearWall)
    feelers.append(backLeftWall)
    feelers.append(backRightWall)
    feelers.append(frontLeftWall)
    feelers.append(frontRightWall)

    # collect distances
    if ai.enemyDistanceId(ai.closestShipId()) > 0:
        closestPlayerDistance = ai.enemyDistanceId(ai.closestShipId())
    else:
        closestPlayerDistance = math.inf

    if ai.shotDist(0) > 0:
        closestBulletDistance = ai.shotDist(0)
    else:
        closestBulletDistance = math.inf

    feeler = min(feelers)
    distToNearestThreat = min(closestPlayerDistance, closestBulletDistance)

    # assign priority to nearest threat
    if closestBulletDistance <= feeler and closestBulletDistance <= closestPlayerDistance: # if closest threat is a bullet
        priority = 1
    elif feeler <= closestPlayerDistance and feeler <= closestBulletDistance: # if closest threat is a wall
        priority = 2
    else: # closest threat is a player
        priority = 3

    if distToNearestThreat < nearLimitThreat:
        ai.setPower(powerHigh)

    # if the closest threat is a bullet
    if priority == 1:
        m = angleToPointDeg((ai.selfX(), ai.selfY()), (ai.shotX(0), ai.shotY(0)))
        if m >= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)

        if ai.shotAlert(0) < shotDanger:
            ai.thrust(1)

    # if the closest threat is a wall
    elif priority == 2:
        # thrust
        if ai.selfSpeed() <= speedLimit:
            ai.thrust(1)
        elif trackWall < nearLimit and angleDiff(heading, tracking) > 90:
            ai.thrust(1)
        elif rearWall < nearLimit and angleDiff(heading, tracking) > 90:
            ai.thrust(1)

        # turn
        if trackWall < nearLimit and leftWall < rightWall:
            ai.turnRight(1)
        elif trackWall < nearLimit and rightWall < leftWall:
            ai.turnLeft(1)
        elif backLeftWall < nearLimit and rightWall > 50:
            ai.turnRight(1)
        elif backRightWall < nearLimit and leftWall > 50:
            ai.turnLeft(1)
        elif frontRightWall < nearLimit:
            ai.turnLeft(1)
        elif frontLeftWall < nearLimit:
            ai.turnRight(1)
    
    # if the closest threat is a player
    elif priority == 3:
        m = angleToPointDeg((ai.selfX(), ai.selfY()), (ai.shotX(0), ai.shotY(0)))
        if m <= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)

        ai.fireShot()

        #if ai.selfHeadingDeg() <= (targetingAccuracy + angleToPointDeg((ai.selfX(), 
        #                           ai.selfY()), (ai.screenEnemyX(0), 
        #                           ai.screenEnemyY(0)))) and ai.selfHeadingDeg() >= (targetingAccuracy - angleToPointDeg((ai.selfX(), 
        #                           ai.selfY()), (ai.screenEnemyX(0), ai.screenEnemyY(0)))):
        #    ai.fireShot()


ai.start(AI_loop,["-name","Russ"])
