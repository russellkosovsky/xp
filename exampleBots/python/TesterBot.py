#Justin Anderson - May 2012
#Run: python3 TesterBot.py
import libpyAI as TEST
import math
def AI_loop():
    #TEST.turnLeft(1)
    #TEST.turnRight(1)
    #TEST.turn(20)
    #TEST.turnToDeg(20)
    #TEST.thrust(1)
    #TEST.setTurnSpeed(1)
    #TEST.setPower(1)
    #TEST.fasterTurnrate()
    #TEST.slowerTurnrate()
    #TEST.morePower()
    #TEST.lessPower()
    #TEST.fireShot()
    #TEST.fireMissile()
    #TEST.fireTorpedo()
    #TEST.fireHeat()
    #TEST.dropMine()
    #TEST.detachMine()
    #TEST.detonateMines()
    #TEST.fireLaser()
    #TEST.tankDetach()
    #TEST.cloak()
    #TEST.ecm()
    #TEST.transporter()
    #TEST.tractorBeam(1)
    #TEST.pressorBeam(1)
    #TEST.phasing()
    #TEST.shield()
    #TEST.emergencyShield()
    #TEST.hyperjump()
    #TEST.nextTank()
    #TEST.prevTank()
    #TEST.toggleAutopilot()
    #TEST.emergencyThrust()
    #TEST.deflector()
    #TEST.selectItem()
    #TEST.loseItem()
    #TEST.lockNext()
    #TEST.lockPrev()
    #TEST.lockClose()
    #TEST.lockNextClose()
    #TEST.loadLock1()
    #TEST.loadLock2()
    #TEST.loadLock3()
    #TEST.loadLock4()
    #TEST.toggleNuclear()
    #TEST.togglePower()
    #TEST.toggleVelocity()
    #TEST.toggleCluster()
    #TEST.toggleMini()
    #TEST.toggleSpread()
    #TEST.toggleLaser()
    #TEST.toggleImplosion()
    #TEST.toggleUserName()
    #TEST.loadModifiers1()
    #TEST.loadModifiers2()
    #TEST.loadModifiers3()
    #TEST.loadModifiers4()
    #TEST.clearModifiers()
    #TEST.connector(1)
    #TEST.dropBall()
    #TEST.refuel(1)
    #TEST.keyHome()
    #TEST.selfDestruct()
    #TEST.pauseAI()
    #TEST.swapSettings()
    #TEST.quitAI()
    #TEST.talkKey()
    #TEST.toggleCompass()
    #TEST.toggleShowMessage()
    #TEST.toggleShowItems()
    #TEST.repair()
    #TEST.reprogram()
    #TEST.talk('Hello')
    #print ('scanMsg:',TEST.scanMsg(0))
    #print ('selfX:',TEST.selfX())
    #print ('selfY:',TEST.selfY())
    #print ('selfRadarX:',TEST.selfRadarX())
    #print ('selfRadarY:',TEST.selfRadarY())
    #print ('selfVelX:',TEST.selfVelX())
    #print ('selfVelY:',TEST.selfVelY())
    #print ('selfSpeed:',TEST.selfSpeed())
    #print ('lockHeadingDeg:',TEST.lockHeadingDeg())
    #print ('lockHeadingRad:',TEST.lockHeadingRad())
    #print ('selfLockDist:',TEST.selfLockDist())
    #print ('selfReload:',TEST.selfReload())
    #print ('selfID:',TEST.selfID())
    #print ('selfAlive:',TEST.selfAlive())
    #print ('selfTeam:',TEST.selfTeam())
    #print ('selfLives:',TEST.selfLives())
    #print ('selfTrackingRad:',TEST.selfTrackingRad())
    #print ('selfTrackingDeg:',TEST.selfTrackingDeg())
    #print ('selfHeadingDeg:',TEST.selfHeadingDeg())
    #print ('selfHeadingRad:',TEST.selfHeadingRad())
    #print ('hudName:',TEST.hudName())
    #print ('hudScore:',TEST.hudScore())
    #print ('hudTimeLeft:',TEST.hudTimeLeft())
    #print ('getTurnSpeed:',TEST.getTurnSpeed())
    #print ('getPower:',TEST.getPower())
    #print ('selfShield:',TEST.selfShield())
    #print ('selfName:',TEST.selfName())
    #print ('selfScore:',TEST.selfScore())
    #print ('closestRadarX:',TEST.closestRadarX())
    #print ('closestRadarY:',TEST.closestRadarY())
    #print ('closestItemX:',TEST.closestItemX())
    #print ('closestItemY:',TEST.closestItemY())
    #print ('closestShipId:',TEST.closestShipId())
    #print ('enemySpeedId:',TEST.enemySpeedId(TEST.closestShipId()))
    #print ('enemyTrackingRadId:',TEST.enemyTrackingRadId(TEST.closestShipId()))
    #print ('enemyTrackingDegId:',TEST.enemyTrackingDegId(TEST.closestShipId()))
    #print ('enemyReloadId:',TEST.enemyReloadId(TEST.closestShipId()))
    #print ('screenEnemyXId:',TEST.screenEnemyXId(TEST.closestShipId()))
    #print ('screenEnemyYId:',TEST.screenEnemyYId(TEST.closestShipId()))
    #print ('enemyHeadingDegId:',TEST.enemyHeadingDegId(TEST.closestShipId()))
    #print ('enemyHeadingRadId:',TEST.enemyHeadingRadId(TEST.closestShipId()))
    #print ('enemyShieldId:',TEST.enemyShieldId(TEST.closestShipId()))
    #print ('enemyLivesId:',TEST.enemyLivesId(TEST.closestShipId()))
    #print ('enemyNameId:',TEST.enemyNameId(TEST.closestShipId()))
    #print ('enemyScoreId:',TEST.enemyScoreId(TEST.closestShipId()))
    #print ('enemyTeamId:',TEST.enemyTeamId(TEST.closestShipId()))
    #print ('enemyDistanceId:',TEST.enemyDistanceId(TEST.closestShipId()))
    #print ('enemyDistance:',TEST.enemyDistance(0))
    #print ('enemySpeed:',TEST.enemySpeed(0))
    #print ('enemyReload:',TEST.enemyReload(0))
    #print ('enemyTrackingRad:',TEST.enemyTrackingRad(0))
    #print ('enemyTrackingDeg:',TEST.enemyTrackingDeg(0))
    #print ('screenEnemyX:',TEST.screenEnemyX(0))
    #print ('screenEnemyY:',TEST.screenEnemyY(0))
    #print ('enemyHeadingDeg:',TEST.enemyHeadingDeg(0))
    #print ('enemyHeadingRad:',TEST.enemyHeadingRad(0))
    #print ('enemyShield:',TEST.enemyShield(0))
    #print ('enemyLives:',TEST.enemyLives(0))
    #print ('enemyTeam:',TEST.enemyTeam(0))
    #print ('enemyName:',TEST.enemyName(0))
    #print ('enemyScore:',TEST.enemyScore(0))
    #print ('degToRad:',TEST.degToRad(180))
    #print ('radToDeg:',TEST.radToDeg(math.pi/2))
    #print ('angleDiff:',TEST.angleDiff(1,3))
    #print ('angleAdd:',TEST.angleAdd(1,3))
    #print ('wallFeeler:',TEST.wallFeeler(100,0,1,1))
    #print ('wallFeelerRad:',TEST.wallFeelerRad(100,0.0,1,1))
    #print ('wallBetween:',TEST.wallBetween(87,600,87,1000,1,1))
    #print ('shotAlert:',TEST.shotAlert(0))
    #print ('shotX:',TEST.shotX(0))
    #print ('shotY:',TEST.shotY(0))
    #print ('shotDist:',TEST.shotDist(0))
    #print ('shotVel:',TEST.shotVel(0))
    #print ('shotVelDir:',TEST.shotVelDir(0))
    #print ('aimdir:',TEST.aimdir(0))
    #print ('ballX:',TEST.ballX())
    #print ('ballY:',TEST.ballY())
    #print ('connectorX0:',TEST.connectorX0())
    #print ('connectorX1:',TEST.connectorX1())
    #print ('connectorY0:',TEST.connectorY0())
    #print ('connectorY1:',TEST.connectorY1())
    print("Test Complete...yeah!")
TEST.start(AI_loop,["-name","Tester Bot"])
