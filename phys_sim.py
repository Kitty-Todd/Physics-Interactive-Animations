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

        
class Friction(Scene):
    def construct(self):
        params = {"mass": 1.0, "gravity": 9.8, "s_friction_coefficient": 0.5, "k_friction_coefficient": 0.3,"final_applied_force": 10.0}
        
        if os.path.exists("params.json"):
            with open("params.json", "r") as f:
                params = json.load(f)

        m = params["mass"]
        g = params["gravity"]
        s = params["s_friction_coefficient"]
        k = params["k_friction_coefficient"]
        F_app = params["final_applied_force"]

        if k > s:
            raise ValueError("Kinetic friction coefficient cannot be greater than static friction coefficient.")
       
        fs = m*g*s/10
        fk = m*g*k/10
        n = m*g/10
        F_app = F_app/10


        ground = Line(start = LEFT*7 + DOWN*2, end = RIGHT*7 + DOWN*2, stroke_width = 6, color = BLUE_C) #ground
        b = Square(side_length = 1, color = WHITE).move_to(DOWN*1.45) #block
        r = Rectangle(height = 3, width = 6.2, color = WHITE, fill_color = WHITE, fill_opacity = 1).move_to(UP*1.5 + LEFT*3.5) #bg
        d = Dot(point = r.get_center(), color = BLACK) #fb dot
        aN = Arrow(start = d, end = UP*(1.5+n) + LEFT*3.5, color = BLACK, stroke_width = 4) #N force
        N = Text("N", color = BLACK).next_to(aN.get_end(), RIGHT).scale(0.5) #N label
        ag = Arrow(start = d, end = UP*(1.5-n) + LEFT*3.5, color = BLACK, stroke_width = 4) #G force
        G = Text("g", color = BLACK).next_to(ag.get_end(), RIGHT).scale(0.5) # G label
        l1 = Line(start = aN.get_left(), end = aN.get_right(), color = BLACK) #equality dash
        l2 = Line(start = ag.get_left(), end = ag.get_right(), color = BLACK) #equality dash
        a = Arrow(start = b.get_right(), end = RIGHT*fs + DOWN * 1.45, color = BLUE, stroke_width = 4) #block applied force start!!
        aa = Arrow(start = b.get_right(), end = RIGHT*fk + DOWN * 1.45, color = BLUE, stroke_width = 4) #block applied force end!!
        a1 = Arrow(start = d.get_right(), end = LEFT*(fs/7) + UP*1.5, color = BLUE, stroke_width = 4) #dot applied force start!!
        a1a = Arrow(start = d.get_right(), end = LEFT*(fk/7) + UP*1.5, color = BLUE, stroke_width = 4) #dot applied force end!!
        Fa = Text("Fa", color = BLUE).scale(0.25).next_to(a.get_end(), RIGHT).shift(UP*0.1) #A force label
        App = Text("Applied Force", color = BLUE).scale(0.35).next_to(a1.get_end(), RIGHT).shift(UP*0.2) #A force label
        a2 = Arrow(start = b.get_left(), end = LEFT*fs+ DOWN*1.45, color = RED, stroke_width = 4) #block static friction!!
        a2a = Arrow(start = b.get_left(), end = LEFT*fk + DOWN*1.45, color = RED, stroke_width = 4) #block kinetic friction!!
        a3 = Arrow(start = d.get_left(), end = LEFT*(fs/7-3.5) + UP*1.5, color = RED, stroke_width = 4) #dot static friction!!
        a3a = Arrow(start = d.get_left(), end = LEFT*(fk/7-3.5) + UP*1.5, color = RED, stroke_width = 4) #dot kinetic friction!!
        Fsf = Text("Fsf", color = RED).scale(0.25).next_to(a2.get_end(), LEFT).shift(UP*0.1) #SF force label
        Fkf = Text("Fkf", color = RED).scale(0.25).next_to(a2.get_end(), LEFT).shift(UP*0.1) #KF force label
        Stat = Text("Static Friction", color = RED).scale(0.35).next_to(a3.get_end(), LEFT).shift(UP*0.2) #SF force label
        Kin = Text("Kinetic Friction", color = RED).scale(0.35).next_to(a3.get_end(), LEFT).shift(UP*0.2) #KF force label
        va = Arrow(start =b.get_left(), end = RIGHT*1.5 + DOWN*1.45, color = GREEN, stroke_width = 4).shift(UP*0.6 + RIGHT*1) #velocity arrow
        v = Text("Velocity", color = GREEN).scale(0.25).next_to(va.get_top()).shift(UP*0.05 + LEFT*0.8) #velocity label
        gr = NumberPlane().set_opacity(0.2).shift(DOWN*2) #grid
        gr2 = NumberPlane().set_opacity(0.2).shift(RIGHT*7 + DOWN*2) #grid
        gru = NumberPlane().set_opacity(0.2).shift(UP*4) #grid
        gr2u = NumberPlane().set_opacity(0.2).shift(UP*4 + RIGHT*7) #grid
        s = Square(side_length=3, color = WHITE, fill_color = WHITE, fill_opacity = 1).move_to(RIGHT*3.4 + UP*1.5) #bg
        l3 = Line(start = RIGHT*2.1 + UP*0.3, end = UP*0.3 + RIGHT*4.7, color = PURE_RED) #axis
        l4 = Line(start = RIGHT*2.2 + UP*0.2, end = UP*2.8 + RIGHT*2.2, color = PURE_RED) #axis
        dl = DashedLine(start = RIGHT*2.2 + UP*2, end = UP*2 + RIGHT*3.4, color = PURE_RED) #static boundaries
        dl2 = DashedLine(start = RIGHT*3.4 + UP*2, end = UP*0.3 + RIGHT*3.4, color = PURE_RED) #static boundaries
        l5 = Line(start = RIGHT*2.2 + UP*0.3, end = RIGHT*3.4 + UP*2, color = PURE_RED) #graph static friction
        l6 = Line(start = RIGHT*3.4 + UP*0.9, end = RIGHT*4.7 + UP*0.9, color = PURE_RED)   #graph kinetic friction
        f = Text("Friction", color = PURE_RED).scale(0.35).move_to(s.get_center()).shift(UP*1.42 + LEFT*1) #graph label
        App2 = Text("Applied Force", color = PURE_RED).scale(0.35).move_to(s.get_center()).shift(DOWN*1.4) #A force label
        st = Text("Static", color = PURE_RED).scale(0.25).move_to(dl.get_top()).shift(UP*0.2) #SF force label
        ki = Text("Kinetic", color = PURE_RED).scale(0.25).move_to(dl.get_top()).shift(RIGHT*1 + UP*0.2) #KF force label

        self.add(gr, gr2, gru, gr2u, ground, b, r, aN, ag, d, l1, l2, N, G, s, l3, l4, f, App2)
        self.wait(1)
        self.play(GrowArrow(a), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), Write(Fa), Write(App), Write(Fsf), Write(Stat), GrowFromPoint(l5, l5.get_start()), Write(st), run_time = 2)
        self.add(dl, dl2)
        self.wait(1)
        if fs < F_app:
            self.play(Transform(a, aa), Transform(a1, a1a), Transform(a2, a2a), Transform(a3, a3a), GrowArrow(va), Write(v), Transform(Fsf, Fkf), Transform(Stat, Kin), gr.animate.shift(LEFT*2), gr2.animate.shift(LEFT*2), gru.animate.shift(LEFT*2), gr2u.animate.shift(LEFT*2), GrowFromPoint(l6, l6.get_start()), Write(ki), run_time=3)
        