def sgn(val: float) -> int:
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0



class PID:
    def __init__(self, inkP: float, inkI: float, inkD: float):
        self.kP = inkP
        self.kI = inkI
        self.kD = inkD

    def changeVals(self, inkP: float, inkI: float, inkD: float):
        self.kP = inkP
        self.kI = inkI
        self.kD = inkD

    def update(self, sig: float, pos = None) -> float:
        error = sig - pos if pos is not None else 0

        if not hasattr(self, 'start'):
            self.prevError = error
            self.start = 1
        self.integral += error
        self.derivative = error - self.prevError
        output =  self.kP * error + self.kI * self.integral + self.kD * self.derivative
        self.prevError = error

        if sgn(error) != sgn(self.prevError):
            self.integral = 0

        if abs(error) < 0.5:
            self.integral = 0

        return output
    

    def reset(self):
        self.integral = 0
        self.start = 0
        self.prevError = 0
        self.out = 0
        self.derivative = 0