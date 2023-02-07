import math
import cmath

class Polar:
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    def __truediv__(self, otro):
        r = self.r / otro.r
        theta = self.theta - otro.theta
        return Polar(r, theta)




