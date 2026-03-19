import venice
import math
#import vasyncio


class Tracking:
    def __init__(self, x: float, y: float, theta: float, sS: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.deltaX = 0.0
        self.deltaY = 0.0
        self.thetaDelta = 0.0
        self.horizDelta = 0.0
        self.vertDelta = 0.0
        self.prevAngle = 0.0
        self.prevHoriz = 0.0
        self.prevVert = 0.0
        self.vert = 0.0
        self.horiz = 0.0
        self.sS = sS
        self.sV = 0.0

    def __str__(self):
        return f"({self.x}, {self.y}, {self.theta})"
    
    

    def Update(self, vert_mL: venice.V5Motor, vert_mR: venice.V5Motor, diameter: float, driveRatio: float):
            self.horiz = 0
            self.vertL = vert_mL.raw_position() * (diameter * math.pi) * driveRatio / 360  # I used 4 inch wheels, so the 4 would be changed to what every size wheels And the 3/5 is the gear ratio
            self.vertR = vert_mR.raw_position() * (diameter * math.pi) * driveRatio / 360
            #self.theta = imu.get_heading() * (math.pi / 180)

            self.vertDeltaL = self.vertL - self.prevVert
            self.vertDeltaR = self.vertR - self.prevVert

            self.horizDelta = self.horiz - self.prevHoriz

            self.thetaDelta = (self.vertDeltaL - self.vertDeltaR) / (self.sS + self.sS); #// if we lacked a IMU we could use this

            self.theta += self.thetaDelta
            
            if abs(self.thetaDelta) > 0.0174533:
                DeltaCoords = [2*math.sin(self.thetaDelta/2)*((self.horizDelta/self.thetaDelta) + self.sS), 2*math.sin(self.thetaDelta/2)*((self.vertDeltaL/self.thetaDelta) + self.sV)]
            else:
                DeltaCoords = [self.horizDelta, self.vertDelta]; 


            rot = self.prevAngle + (self.thetaDelta/2)
            #rot = rot*(180/M_PI)
            deltaX = DeltaCoords[0]*math.cos(rot) - DeltaCoords[1]*math.sin(rot)
            deltaY = DeltaCoords[0]*math.sin(rot) + DeltaCoords[1]*math.cos(rot)

            self.x += deltaX
            self.y += deltaY

            self.prevAngle = self.theta
            self.prevVert = self.vert
            self.prevHoriz = self.horiz

            return (self.x, self.y, self.theta)
