from manim import *

class Normal_Vector(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        space = Square(6, fill_color=BLUE_D, fill_opacity=0.5, stroke_color=WHITE, stroke_width=1)
        tl1 = Line(start=space.get_corner(UP + LEFT), end=(-3, 3, -2), color=WHITE)
        tl2 = Line(start=space.get_corner(UP + RIGHT), end=(3, 3, -2), color=WHITE)
        tl3 = Line(start=space.get_corner(DOWN + LEFT), end=(-3, -3, -2), color=WHITE)
        tl4 = Line(start=space.get_corner(DOWN + RIGHT), end=(3, -3, -2), color=WHITE)
        vector = Arrow3D(start=space.get_center(), end=(0, 0, 1), color=YELLOW_E)


        self.play(Write(space), Write(tl1), Write(tl2), Write(tl3), Write(tl4))
        self.wait(1)

        self.play(Create(vector))
        self.wait(1)

        self.play(vector.animate.shift(RIGHT * 2 + UP * 2))
        self.play(vector.animate.shift(DOWN *2))
        self.play(vector.animate.shift(LEFT * 3 + UP * 1))
        self.play(vector.animate.shift(LEFT * 2 + DOWN * 2))
        self.play(vector.animate.shift(RIGHT * 3 + UP * 1))

        self.move_camera(phi=0, theta=-90*DEGREES, run_time=2)
        self.play(Rotate(vector, angle=-PI/2, axis=RIGHT, run_time=1))
        self.wait(1)

        self.play(Rotate(vector, angle=2*PI, run_time=3))

        self.move_camera(phi=75*DEGREES, theta=-45*DEGREES)
        self.play(Rotate(vector, angle=PI/2, axis=RIGHT))
        self.wait(1)