import libpyAI as ai
import math

#finds difference between two angles
def angleDifference(a, b):    
    return int(180 - abs(abs(a - b) - 180))


speedLimit = 5 # (xp speed units)
nearLimit = 150 # threshold for a relatively "close" object (xp distance units)
speedAlertValue = 1

def AI_loop():
 
    #Release keys
    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)

    ## Get values of variables for Wall Feelers, Head & Tracking 
    heading = int(ai.selfHeadingDeg())
    tracking = int(ai.selfTrackingDeg())

    feelers = []
    frontWall = ai.wallFeeler(500,heading)
    left45Wall = ai.wallFeeler(500,heading+45)
    right45Wall = ai.wallFeeler(500,heading-45)
    left90Wall = ai.wallFeeler(500,heading+90)
    right90Wall = ai.wallFeeler(500,heading-90)
    left135Wall = ai.wallFeeler(500,heading+135)
    right135Wall = ai.wallFeeler(500,heading-135)
    backWall = ai.wallFeeler(500,heading-180) 
    trackWall = ai.wallFeeler(500,tracking)
  
    feelers.append(frontWall)
    feelers.append(left45Wall )
    feelers.append(right45Wall )
    feelers.append(left90Wall )
    feelers.append(right90Wall )
    feelers.append(left135Wall )
    feelers.append(right135Wall )
    feelers.append(backWall )
    feelers.append(trackWall )
    
    ##Find the closest ennemys distance and closest bullets distance
    closestPlayerDistance = ai.enemyDistanceId(ai.closestShipId())
    closestBulletDistance = ai.shotDist(0)
    ##Find the closest ennemy
    enemy = ai.lockClose()
    ## Get the lockheadingdeg of enemy 
    head = ai.lockHeadingDeg()
    ## Get the dstance from enemy 
    enemyDist = ai.selfLockDist()

    shortest_feeler = min(feelers)
    dist_Nearest_Threat = min(closestPlayerDistance, closestBulletDistance)
    

    ##### Production System Rules ######
    ## turn
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
    ## thrust
    elif ai.selfSpeed() <= speedLimit:
        ai.thrust(1)
    elif trackWall < nearLimit and angleDifference(heading, tracking) > 90:
        ai.thrust(1)
    elif rearWall < nearLimit and angleDifference(heading, tracking) > 90:
        ai.thrust(1)
    ## bullet Avoidance Commands
    elif ai.shotAlert(0) >= 0 and ai.shotAlert(0) <= 45:
        if ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() <= speedAlertValue:
            ai.turnLeft(1)
            ai.thrust(1)
        elif ai.angleDiff(heading, ai.shotVelDir(0)) < 0 and ai.selfSpeed() <= speedAlertValue: 
            ai.turnRight(1)
            ai.thrust(1)
        elif ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() > speedAlertValue:
            ai.turnLeft(1)
        else:
            ai.turnRight(1)
    ## shooting Ennemy Commands
    elif enemyDist <= 1300 and heading > (head) and ai.selfSpeed() > speedAlertValue:
        ai.turnRight(1)
        ai.fireShot()
    elif enemyDist <= 1300 and heading < (head) and ai.selfSpeed() > speedAlertValue:
        ai.turnLeft(1)
        ai.fireShot()
    elif ai.selfSpeed() < speedAlertValue:
        ai.thrust(1)
    else:
        ai.thrust(1)

ai.start(AI_loop,["-name","Russell"])
