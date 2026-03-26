from manim import *
import json
import os

class ProjectileSim(Scene):
    def construct(self):
        params = {"gravity": 9.8, "velocity": 5.0}

        if os.path.exists("params.json"):
            with open("params.json", "r") as f:
                params = json.load(f)

        g = params["gravity"]
        v = params["velocity"]

        ball = Dot(color=BLUE).shift(LEFT*5 + DOWN*3)
        target = Line(UP, DOWN).shift(RIGHT*5)

        label = MathTex(f"g = {g} m/s^2").to_corner(UL)

        self.add(ball, target, label)
        self.play(
            ball.animate.shift(RIGHT*10 + UP*(v/g)),
            rate_func=linear,
            run_time=2
        )
        self.wait()