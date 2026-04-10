from manim import *
from manim_physics import *

class Superposition(Scene): 
    def construct(self):

        c1 = Charge(1)
        f1 = ElectricField(c1)

        self.add(c1, f1)
        self.wait(2)