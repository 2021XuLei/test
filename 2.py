import math
import numpy as np
import time

class Ball:
    __pi = math.pi

    def __init__(self, p, r):
        self.pos = list(p)
        self.r = float(r)

    def __str__(self):
        return "(x-%.2f)^2+(y-%.2f)^2+(z-%.2f)^2=%.2f^2" % \
            (self.pos[0], self.pos[1], self.pos[2], self.r)
    
    def get_s(self):
        return 4 * self.__pi * math.pow(self.r, 2)

    def get_v(self):
        print((4 * self.__pi * math.pow(self.r, 3)) / 3 )
        # return (4 * self.__pi * math.pow(self.r, 3)) / 3

    def two_distance(self, other):
        return "The distance between two balls is %.2f" % \
            (math.hypot(self.pos[0] - other.pos[0], self.pos[1] -
             other.pos[1], self.pos[2] - other.pos[2]))

    def __2_dis(self, other):
        return math.hypot(self.pos[0] - other.pos[0], self.pos[1] - other.pos[1], self.pos[2] - other.pos[2]),

    def judge_2(self, other):
        pass


if __name__ == "__main__":
    a = Ball([0, 0, 0],4)
    print(a)