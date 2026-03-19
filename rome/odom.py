from venice import V5Motor
#import math
#import vasyncio


class Tracking:
    def __init__(self, x: float, y: float, theta: float, sS: float):
        self.coords = [x,y,theta]
        self.thetaDelta = 0.0
        self.horizDelta = 0.0
        self.vertDelta = 0.0
        self.prev = [0.0, 0.0, 0.0, 0.0]
        self.vert = 0.0
        self.horiz = 0.0
        self.sS = sS
        self.sV = 0.0

    def __str__(self):
        return f"{self.coords}"
'''
    def Update(self, vert_mL: V5Motor, vert_mR: V5Motor, diameter: float, driveRatio: float):
            self.horiz = 0
            self.vertL = vert_mL.raw_position() * (diameter * 3.14159) * driveRatio / 360  # I used 4 inch wheels, so the 4 would be changed to what every size wheels And the 3/5 is the gear ratio
            self.vertR = vert_mR.raw_position() * (diameter * 3.14159) * driveRatio / 360
            #self.theta = imu.get_heading() * (math.pi / 180)

            self.vertDeltaL = self.vertL - self.prev[1]
            self.vertDeltaR = self.vertR - self.prev[2]

            self.horizDelta = self.horiz - self.prev[0]

            self.thetaDelta = (self.vertDeltaL - self.vertDeltaR) / (self.sS + self.sS); #// if we lacked a IMU we could use this

            self.theta += self.thetaDelta
            
            if abs(self.thetaDelta) > 0.0174533:
                DeltaCoords = [2*math.sin(self.thetaDelta/2)*((self.horizDelta/self.thetaDelta) + self.sS), 2*math.sin(self.thetaDelta/2)*((self.vertDeltaL/self.thetaDelta) + self.sV)]
            else:
                DeltaCoords = [self.horizDelta, self.vertDelta]; 


            rot = self.prev[3] + (self.thetaDelta/2)
            #rot = rot*(180/M_PI)

            self.coords[0] += DeltaCoords[0]*math.cos(rot) - DeltaCoords[1]*math.sin(rot)
            self.coords[1] += DeltaCoords[0]*math.sin(rot) + DeltaCoords[1]*math.cos(rot)

            self.prev[3] = self.theta
            self.prev[1] = self.vertL
            self.prev[2] = self.vertR
            self.prev[0] = self.horiz

            return (self.coords[0], self.coords[1], self.coords[2])'''
