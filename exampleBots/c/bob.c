
#include <math.h>
#include <stdio.h>

AI_loop() {
    // Release keys
    thrust(0);
    turnLeft(0);
    turnRight(0);
    int speedLimit = 5;
    // Distance for close object (distance units)
    int nearDanger = 170;
    // Distance for close bullets (distance units)
    int shotDanger = 130;
    // Backup distance threshold
    int alertDistance = 275;
    // Handicap
    setTurnSpeedDeg(20);
    setPower(20);

    // Get information
    int heading = (int)selfHeadingDeg();
    int tracking = (int)selfTrackingDeg();
    // Store in array so we can easily find the shortest feeler
    int feelers[9];
    int frontWall = wallFeeler(500, heading);
    int leftWall = wallFeeler(500, heading + 90);
    int rightWall = wallFeeler(500, heading - 90);
    int trackWall = wallFeeler(500, tracking);
    int rearWall = wallFeeler(500, heading - 180);
    int backLeftWall = wallFeeler(500, heading + 135);
    int backRightWall = wallFeeler(500, heading - 135);
    int frontLeftWall = wallFeeler(500, heading + 45);
    int frontRightWall = wallFeeler(500, heading - 45);
    feelers[0] = frontWall;
    feelers[1] = leftWall;
    feelers[2] = rightWall;
    feelers[3] = trackWall;
    feelers[4] = rearWall;
    feelers[5] = backLeftWall;
    feelers[6] = backRightWall;
    feelers[7] = frontLeftWall;
    feelers[8] = frontRightWall;

    // Get distances
    int closestPlayerDistance = (int)enemyDistanceId(closestShipId());
    int closestBulletDistance = (int)shotDist(0);

    // Shortest feeler
    int feeler = feelers[0];
    for (int i = 1; i < 9; i++) {
        if (feelers[i] < feeler) {
            feeler = feelers[i];
        }
    }
    // Nearest object (player or bullet)
    int distToNearestThreat = (closestPlayerDistance < closestBulletDistance) ? closestPlayerDistance : closestBulletDistance;

    // Reset power based on how close the nearest threat is
    if (feeler <= 100 || distToNearestThreat <= 100) {
        setPower(30);
    } else if (feeler <= 50 || distToNearestThreat <= 50) {
        setPower(45);
    }

    // Assign priority to nearest threat
    int priority;
    if (closestBulletDistance <= feeler && closestBulletDistance <= closestPlayerDistance) {
        priority = 1;
    } else if (feeler <= closestPlayerDistance && feeler <= closestBulletDistance) {
        priority = 2;
    } else {
        priority = 3;
    }

    // The closest threat is a bullet
    if (priority == 1) {
        double p1[] = {selfX(), selfY()};
        double p2[] = {shotX(0), shotY(0)};
        // Get the angle between self and nearest shot, relative to horizontal
        double dx = p1[0] - p2[0];
        double dy = p2[1] - p1[1];
        int m = -1 * ((int)(atan2(dy, dx) * 180.0 / M_PI) + 180) % 360;
        // Measure the difference between 'm' and self's heading
        m = ((m - selfHeadingDeg()) + 180) % 360 - 180;

        if (m >= 0) {
            turnRight(1);
        } else {
            turnLeft(1);
        }
        if (shotAlert(0) < shotDanger) {
            thrust(1);
        }
    }
    // The closest threat is a wall
    else if (priority == 2) {
        // Find the difference between heading and tracking
        int head_track_diff = 180 - abs(abs(heading - tracking) - 180);
        // Thrusting
        if (selfSpeed() <= speedLimit) {
            thrust(1);
        } else if (trackWall < nearDanger && head_track_diff > 90) {
            thrust(1);
        } else if (rearWall < nearDanger && head_track_diff > 90) {
            thrust(1);
        }
        // Turning
        if (trackWall < nearDanger && leftWall < rightWall) {
            turnRight(1);
        } else if (trackWall < nearDanger && rightWall < leftWall) {
            turnLeft(1);
        } else if (backLeftWall < nearDanger && rightWall > 50) {
            turnRight(1);
        } else if (backRightWall < nearDanger && leftWall > 50) {
            turnLeft(1);
        } else if (frontRightWall < nearDanger) {
            turnLeft(1);
        } else if (frontLeftWall < nearDanger) {
            turnRight(1);
        } else if (frontWall <= alertDistance && (frontLeftWall < frontRightWall) && selfSpeed() > 1) {
            turnRight(1);
        } else if (frontWall <= alertDistance && (frontLeftWall > frontRightWall) && selfSpeed() > 1) {
            turnLeft(1);
        } else if (leftWall <= alertDistance && selfSpeed() > 1) {
            turnRight(1);
        } else if (rightWall <= alertDistance && selfSpeed() > 1) {
            turnLeft(1);
        }
    }
    // The closest threat is a player
    else if (priority == 3) {
        double p1[] = {selfX(), selfY()};
        double p2[] = {screenEnemyX(0), screenEnemyY(0)};
        // Get the angle between self and nearest enemy, relative to horizontal
        double dx = p1[0] - p2[0];
        double dy = p2[1] - p1[1];
        int m = -1 * ((int)(atan2(dy, dx) * 180.0 / M_PI) + 180) % 360;
        // Get the difference between m and self's heading
        m = ((m - selfHeadingDeg()) + 180) % 360 - 180;

        if (m <= 0) {
            turnRight(1);
            fireShot();
        } else {
            turnLeft(1);
            fireShot();
        }
        if (selfHeadingDeg() <= (5 + m) && selfHeadingDeg() >= (5 - m)) {
            fireShot();
        }
    }
}

int main() {
    start(AI_loop, "-name bob");
}


