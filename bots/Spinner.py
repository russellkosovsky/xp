#Xpilot-AI Team 2012
#Run: python3 Spinner.py

import libpyAI as ai

def AI_loop():

    ai.thrust(0)
    ai.turnLeft(0)
    ai.turnRight(0)
    
    ai.turnLeft(1)
    ai.thrust(1)
    ai.fireShot()
    
ai.start(AI_loop,["-name","Spinner"])
