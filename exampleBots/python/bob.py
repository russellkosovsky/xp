
import libpyAI as ai
import math

def AI_loop():
    # release keys
    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)
    speedLimit = 5
    # distance for close object (distance units)
    nearDanger = 170 
    # distance for close bullets (distance units)    
    shotDanger = 130 
    # backup distance threshold
    alertDistance = 275     
    # handicap
    ai.setTurnSpeedDeg(20)
    
    # get information
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())
    # store in array so we can easily find the shortest feeler
    feelers = []
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

    # get distances
    if ai.enemyDistanceId(ai.closestShipId()) > 0:
        closestPlayerDistance = ai.enemyDistanceId(ai.closestShipId())
    else:
        closestPlayerDistance = math.inf

    if ai.shotDist(0) > 0:
        closestBulletDistance = ai.shotDist(0)
    else:
        closestBulletDistance = math.inf

    # shortest feeler
    feeler = min(feelers)
    # nearest object (player or bullet)
    distToNearestThreat = min(closestPlayerDistance, closestBulletDistance)

    # assign priority to nearest threat
    # if closest threat is a bullet
    if closestBulletDistance <= feeler and closestBulletDistance <= closestPlayerDistance: 
        priority = 1
    # if closest threat is a wall
    elif feeler <= closestPlayerDistance and feeler <= closestBulletDistance: 
        priority = 2
    # closest threat is a player
    else: 
        priority = 3

    # the closest threat is a bullet
    if priority == 1:        
        p1, p2 = (ai.selfX(), ai.selfY()), (ai.shotX(0), ai.shotY(0))
        # get the angle between self and nearest shot, relative to horizontal
        dx = p1[0] - p2[0]
        dy = p2[1] - p1[1]
        m = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
        # measure the difference between 'm' and selfs heading
        m = ((m - ai.selfHeadingDeg()) + 180) % 360 - 180

        if m >= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)
        if ai.shotAlert(0) < shotDanger:
            ai.thrust(1)       

    # the closest threat is a wall
    elif priority == 2:
        #finds difference the heading and the tracking
        head_track_diff = int(180 - abs(abs(heading - tracking) - 180))
        # thrusting
        if ai.selfSpeed() <= speedLimit:
            ai.thrust(1)
        elif trackWall < nearDanger and head_track_diff > 90:
            ai.thrust(1)
        elif rearWall < nearDanger and head_track_diff > 90:
            ai.thrust(1)
        # turning ### (production system) ###
        if trackWall < nearDanger and leftWall < rightWall:
            ai.turnRight(1)
        elif trackWall < nearDanger and rightWall < leftWall:
            ai.turnLeft(1)
        elif backLeftWall < nearDanger and rightWall > 50:
            ai.turnRight(1)
        elif backRightWall < nearDanger and leftWall > 50:
            ai.turnLeft(1)
        elif frontRightWall < nearDanger:
            ai.turnLeft(1)
        elif frontLeftWall < nearDanger:
            ai.turnRight(1)
        elif frontWall <= alertDistance and (frontLeftWall < frontRightWall): 
            ai.turnRight(1)
        elif frontWall <= alertDistance and (frontLeftWall > frontRightWall):
            ai.turnLeft(1)
        elif leftWall <= alertDistance and ai.selfSpeed() > 1:
            ai.turnRight(1) 
        elif rightWall <= alertDistance and ai.selfSpeed() > 1:
            ai.turnLeft(1)
 
    # the closest threat is a player
    elif priority == 3:
        p1, p2 = (ai.selfX(), ai.selfY()), (ai.screenEnemyX(0), ai.screenEnemyY(0))
        # get the angle between self and nearest enemy, relative to horizontal
        dx = p1[0] - p2[0]
        dy = p2[1] - p1[1]
        m = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
        # get the difference between m2 and selfs heading
        m = ((m - ai.selfHeadingDeg()) + 180) % 360 - 180

        if m <= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)
        if ai.selfHeadingDeg() <= (5 + m) and ai.selfHeadingDeg() >= (5 - m):
            ai.fireShot()


ai.start(AI_loop,["-name","bob"])
