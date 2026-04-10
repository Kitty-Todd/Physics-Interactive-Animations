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
        c2 = Charge(1)
        c2.shift(RIGHT * 3.5)
        f2 = ElectricField(c2)

        self.add(c1, f1, g, a1, a1a, a2, a2a, a3, a3a, a4, a4a, a5, a5a, a6, a6a, a7, a7a)
        self.wait(2)
        self.play(c1.animate.shift(LEFT*3.5), f1.animate.shift(LEFT*3.5), a1.animate.shift(LEFT*3.5), a1a.animate.shift(LEFT*3.5), a2.animate.shift(LEFT*3.5), a2a.animate.shift(LEFT*3.5), a3.animate.shift(LEFT*3.5), a3a.animate.shift(LEFT*3.5), a4.animate.shift(LEFT*3.5), a4a.animate.shift(LEFT*3.5), a5.animate.shift(LEFT*3.5), a5a.animate.shift(LEFT*3.5), a6.animate.shift(LEFT*3.5), a6a.animate.shift(LEFT*3.5), a7.animate.shift(LEFT*3.5), a7a.animate.shift(LEFT*3.5), run_time = 2)
        self.play(FadeIn(c2, f2))
        self.wait(2)