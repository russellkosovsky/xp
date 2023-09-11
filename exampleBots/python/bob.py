import libpyAI as ai
import math
import statistics



# main loop for this agent --- a rule-based expert system
def AI_loop():

    # release keys
    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)

    nearDanger = 170 # distance for close object (distance units)
    shotDanger = 130 # distance for close bullets (distance units)
    speedLimit = 5 
    alertDistance = 275 # backup distance threshold
    
    # handicap
    ai.setTurnSpeedDeg(20)

    # get information
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())

    # store in array so we can easily find the shortest
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

     # if the closest threat is a bullet
    if priority == 1:

        p1, p2 = (ai.selfX(), ai.selfY()), (ai.shotX(0), ai.shotY(0))
        #Compute the angle between two cartesian points, relative to horizontal
        dx = p1[0] - p2[0]
        dy = p2[1] - p1[1]
        m = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
        #Measures the difference between two headings
        m = ((m - ai.selfHeadingDeg()) + 180) % 360 - 180
        if m >= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)
        if ai.shotAlert(0) < shotDanger:
            ai.thrust(1)       


    # if the closest threat is a wall
    elif priority == 2:
        
        #finds difference the heading and the tracking
        head_track_diff = int(180 - abs(abs(heading - tracking) - 180))
        
        # thrust
        if ai.selfSpeed() <= speedLimit:
            ai.thrust(1)
        elif trackWall < nearDanger and head_track_diff > 90:
            ai.thrust(1)
        elif rearWall < nearDanger and head_track_diff > 90:
            ai.thrust(1)
        
        ### (production system) ###
        # turn
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
        elif frontWall <= alertDistance and (frontLeftWall < frontRightWall) and ai.selfSpeed() > 1: 
            ai.turnRight(1)
        elif frontWall <= alertDistance and (frontLeftWall > frontRightWall) and ai.selfSpeed() > 1:
            ai.turnLeft(1)
        elif leftWall <= alertDistance and ai.selfSpeed() > 1:
            ai.turnRight(1) 
        elif rightWall <= alertDistance and ai.selfSpeed() > 1:
            ai.turnLeft(1)
 
    # if the closest threat is a player
    elif priority == 3:
       
        p1, p2 = (ai.selfX(), ai.selfY()), (ai.shotX(0), ai.shotY(0))
        #Compute the angle between self and nearest shot, relative to horizontal
        dx = p1[0] - p2[0]
        dy = p2[1] - p1[1]
        m = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
        
        #Measures the difference between 'm' and selfs heading
        m = ((m - ai.selfHeadingDeg()) + 180) % 360 - 180
        if m <= 0:
            ai.turnRight(1)
        else:
            ai.turnLeft(1)

        p3, p4 = (ai.selfX(), ai.selfY()), (ai.screenEnemyX(0), ai.screenEnemyY(0))
        #Compute the angle between self and nearest enemy, relative to horizontal
        dx = p3[0] - p4[0]
        dy = p4[1] - p3[1]
        m2 = -1 * (int(math.degrees(math.atan2(dy, dx))) + 180) % 360
        #Measures the difference between m2 and selfs heading
        m2 = ((m2 - ai.selfHeadingDeg()) + 180) % 360 - 180
        if ai.selfHeadingDeg() <= (5 + m2) and ai.selfHeadingDeg() >= (5 - m2):
            ai.fireShot()


ai.start(AI_loop,["-name","bob"])
