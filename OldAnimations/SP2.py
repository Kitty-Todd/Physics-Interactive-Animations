from manim import *
from manim_physics import *

class Superposition(Scene): 
    def construct(self):

        c1 = Charge(1)
        f1 = ElectricField(c1)
        g = NumberPlane()

        self.add(c1, f1)
        self.wait(1)
        self.add(g)
        self.wait(2)