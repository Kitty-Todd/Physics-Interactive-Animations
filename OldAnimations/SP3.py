from manim import *
from manim_physics import *

class Superposition(Scene): 
    def construct(self):

        c1 = Charge(1)
        f1 = ElectricField(c1)
        g = NumberPlane()
        a1 = Arrow(start = RIGHT * 0.5 + UP * 0.5, end = RIGHT * 0.8 + UP * 0.5)
        a1a = Arrow(start = RIGHT * 0.5 + UP * 0.5, end = RIGHT * 0.5 + UP * 0.85)
        a2 = Arrow(start = RIGHT * 1 + UP * 1, end = RIGHT * 1.25 + UP * 1)
        a2a = Arrow(start = RIGHT * 1 + UP * 1, end = RIGHT * 1 + UP * 1.25)
        a3 = Arrow(start = RIGHT * 1.5 + UP * 1.5, end = RIGHT * 1.7 + UP * 1.5)
        a3a = Arrow(start = RIGHT * 1.5 + UP * 1.5, end = RIGHT * 1.5 + UP * 1.75)
        a4 = Arrow(start = RIGHT * 2 + UP * 2, end = RIGHT * 2.2 + UP * 2)
        a4a = Arrow(start = RIGHT * 2 + UP * 2, end = RIGHT * 2 + UP * 2.2)
        a5 = Arrow(start = RIGHT * 2.5 + UP * 2.5, end = RIGHT * 2.65 + UP * 2.5)
        a5a = Arrow(start = RIGHT * 2.5 + UP * 2.5, end = RIGHT * 2.5 + UP * 2.65)
        a6 = Arrow(start = RIGHT * 3 + UP * 3, end = RIGHT * 3.15 + UP * 3)
        a6a = Arrow(start = RIGHT * 3 + UP * 3, end = RIGHT * 3 + UP * 3.15)
        a7 = Arrow(start = RIGHT * 3.5 + UP * 3.5, end = RIGHT * 3.6 + UP * 3.5)
        a7a = Arrow(start = RIGHT * 3.5 + UP * 3.5, end = RIGHT * 3.5 + UP * 3.6)

        self.add(c1, f1, g)
        self.wait(1)
        self.add(a1, a1a, a2, a2a, a3, a3a, a4, a4a, a5, a5a, a6, a6a, a7, a7a)
        self.wait(2)