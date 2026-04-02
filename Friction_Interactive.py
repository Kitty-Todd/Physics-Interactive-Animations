from manim import *
import json
import os

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
       
        fs = m*g*s/10
        fk = m*g*k/10
        n = m*g/10
        F_app = F_app/10

        ground = Line(start = LEFT*7 + DOWN*2, end = RIGHT*7 + DOWN*2, stroke_width = 6, color = BLUE_C) #ground
        gr = NumberPlane().set_opacity(0.2).shift(DOWN*2) #grid
        gr2 = NumberPlane().set_opacity(0.2).shift(RIGHT*7 + DOWN*2) #grid
        gru = NumberPlane().set_opacity(0.2).shift(UP*4) #grid
        gr2u = NumberPlane().set_opacity(0.2).shift(UP*4 + RIGHT*7) #grid
        r = Rectangle(height = 3, width = 6.2, color = WHITE, fill_color = WHITE, fill_opacity = 1).move_to(UP*1.5) #fbd background
        d = Dot(point = r.get_center(), color = BLACK) #fbd dot
        aN = Arrow(start = d, end = UP*(1.5+n), color = BLACK, stroke_width = 4) #normal force arrow
        N = Text("N", color = BLACK).next_to(aN.get_end(), RIGHT).scale(0.5) #normal force label
        ag = Arrow(start = d, end = UP*(1.5-n), color = BLACK, stroke_width = 4) #gravity arrow
        G = Text("g", color = BLACK).next_to(ag.get_end(), RIGHT).scale(0.5) #gravity label
        l1 = Line(start = aN.get_left(), end = aN.get_right(), color = BLACK) #equality line normal
        l2 = Line(start = ag.get_left(), end = ag.get_right(), color = BLACK) #equality line gravity

        b = Square(side_length = 1, color = WHITE).move_to(DOWN*1.45) #box
        a = Arrow(start = b.get_right(), end = RIGHT*fs + DOWN * 1.45, color = BLUE, stroke_width = 4) #starting applied force on box
        aa = Arrow(start = b.get_right(), end = RIGHT*F_app + DOWN * 1.45, color = BLUE, stroke_width = 4) #final applied force on box
        a1 = Arrow(start = d.get_right(), end = RIGHT*(fs/3*2) + UP*1.5, color = BLUE, stroke_width = 4) #starting applied force fbd
        a1a = Arrow(start = d.get_right(), end = RIGHT*(F_app/3*2) + UP*1.5, color = BLUE, stroke_width = 4) #final applied force fbd
        Fa = Text("Fa", color = BLUE).scale(0.25).next_to(a.get_end(), RIGHT).shift(UP*0.1) #box Fa label
        App = Text("Applied Force", color = BLUE).scale(0.35).next_to(a1.get_end(), RIGHT).shift(UP*0.2) #fbd Fa label
        a2 = Arrow(start = b.get_left(), end = LEFT*fs + DOWN*1.45, color = RED, stroke_width = 4) #static frictional force on box
        a2a = Arrow(start = b.get_left(), end = LEFT*fk + DOWN*1.45, color = RED, stroke_width = 4) #kinetic frictional force on box
        a3 = Arrow(start = d.get_left(), end = LEFT*(fs/3*2) + UP*1.5, color = RED, stroke_width = 4) #static frictional force on fbd
        a3a = Arrow(start = d.get_left(), end = LEFT*(fk/3*2) + UP*1.5, color = RED, stroke_width = 4) #kinetic frictional force on fbd
        Fsf = Text("Fsf", color = RED).scale(0.25).next_to(a2.get_end(), LEFT).shift(UP*0.1) #box static friction label
        Fkf = Text("Fkf", color = RED).scale(0.25).next_to(a2.get_end(), LEFT).shift(UP*0.1) #box kinetic friction label
        Stat = Text("Static Friction", color = RED).scale(0.35).next_to(a3.get_end(), LEFT).shift(UP*0.2) #fbd static friction label
        Kin = Text("Kinetic Friction", color = RED).scale(0.35).next_to(a3.get_end(), LEFT).shift(UP*0.2) #fbd kinetic friction label
        va = Arrow(start =b.get_left(), end = RIGHT*1.5 + DOWN*1.45, color = GREEN, stroke_width = 4).shift(UP*0.6 + RIGHT*1) #velocity vector
        v = Text("Velocity", color = GREEN).scale(0.25).next_to(va.get_top()).shift(UP*0.05 + LEFT*0.8) #velocity label
        

        self.add(gr, gr2, gru, gr2u, ground, b, r, aN, ag, d, l1, l2, N, G)
        self.wait(1)
        self.play(GrowArrow(a), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), Write(Fa), Write(App), Write(Fsf), Write(Stat), run_time = 2)
        self.wait(1)
        self.play(Transform(a, aa), Transform(a1, a1a), Transform(a2, a2a), Transform(a3, a3a), 
                  GrowArrow(va), Write(v), Transform(Fsf, Fkf), Transform(Stat, Kin), 
                  gr.animate.shift(LEFT*2), gr2.animate.shift(LEFT*2), gru.animate.shift(LEFT*2), gr2u.animate.shift(LEFT*2), run_time=3)
