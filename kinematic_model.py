from __future__ import print_function

import math

class KinematicModel(object):
    def __init__(self, x, y, psi, v, f_len):
        self.x = x
        self.y = y
        self.psi = psi
        self.v = v

        self.f_len = f_len

    def get_state(self):
        return self.x, self.y, self.psi, self.v

    def update_state(self, a, delta, dt):
        beta = math.atan((1./2) * math.tan(delta))

        self.x = self.x + self.v * math.cos(self.psi * beta) * dt
        self.y = self.y + self.v * math.sin(self.psi * beta) * dt
        self.psi = self.psi + (self.v/self.f_len) * math.sin(beta) * dt
        self.v = self.v + a * dt
        return self.x, self.y, self.psi, self.v
