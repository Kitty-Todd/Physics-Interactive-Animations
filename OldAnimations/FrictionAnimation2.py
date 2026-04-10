from xml.dom.minidom import Text
from manim import *
from manim.opengl import *

class Friction(Scene):
    def construct(self):
        mass = int(input("Enter the mass of the block (kg): "))
        mu_s = float(input("Enter the coefficient of static friction: "))
        mu_k = float(input("Enter the coefficient of kinetic friction: "))
        def interact(mass, mu_s, mu_k):
            sf = mu_s * mass
            kf = mu_k * mass
            g = Line(start = LEFT*7 + DOWN*2, end = RIGHT*7 + DOWN*2, stroke_width = 6, color = BLUE_C) #ground
            b = Square(side_length = 1, color = WHITE).move_to(DOWN*1.45) #block
            r = Rectangle(height = 3, width = 6.2, color = WHITE, fill_color = WHITE, fill_opacity = 1).move_to(UP*1.5 + LEFT*3.5) #bg
            d = Dot(point = r.get_center(), color = BLACK) #fb dot
            aN = Arrow(start = d, end = UP*3 + LEFT*3.5, color = BLACK, stroke_width = 4) #N force
            N = Text("N", color = BLACK).next_to(aN.get_end(), RIGHT).scale(0.5) #N label
            ag = Arrow(start = d, end = UP*0 + LEFT*3.5, color = BLACK, stroke_width = 4) #G force
            G = Text("g", color = BLACK).next_to(ag.get_end(), RIGHT).scale(0.5) # G label
            l1 = Line(start = aN.get_left(), end = aN.get_right(), color = BLACK) #equality dash
            l2 = Line(start = ag.get_left(), end = ag.get_right(), color = BLACK) #equality dash
            a = Arrow(start = b.get_right(), end = RIGHT*sf + DOWN * 1.45, color = BLUE, stroke_width = 4) #block applied force start!!
            aa = Arrow(start = b.get_right(), end = RIGHT*kf + DOWN * 1.45, color = BLUE, stroke_width = 4) #block applied force end!!
            a1 = Arrow(start = d.get_right(), end = LEFT*(sf/7) + UP*1.5, color = BLUE, stroke_width = 4) #dot applied force start!!
            a1a = Arrow(start = d.get_right(), end = LEFT*(kf/7) + UP*1.5, color = BLUE, stroke_width = 4) #dot applied force end!!
            Fa = Text("Fa", color = BLUE).scale(0.25).next_to(a.get_end(), RIGHT).shift(UP*0.1) #A force label
            App = Text("Applied Force", color = BLUE).scale(0.35).next_to(a1.get_end(), RIGHT).shift(UP*0.2) #A force label
            a2 = Arrow(start = b.get_left(), end = LEFT*sf + DOWN*1.45, color = RED, stroke_width = 4) #block static friction!!
            a2a = Arrow(start = b.get_left(), end = LEFT*kf + DOWN*1.45, color = RED, stroke_width = 4) #block kinetic friction!!
            a3 = Arrow(start = d.get_left(), end = LEFT*(sf*2.5/1.25) + UP*1.5, color = RED, stroke_width = 4) #dot static friction!!
            a3a = Arrow(start = d.get_left(), end = LEFT*(kf*2.5/1.25) + UP*1.5, color = RED, stroke_width = 4) #dot kinetic friction!!
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

            self.add(gr, gr2, gru, gr2u, g, b, r, aN, ag, d, l1, l2, N, G, s, l3, l4, f, App2)
            self.wait(1)
            self.play(GrowArrow(a), GrowArrow(a1), GrowArrow(a2), GrowArrow(a3), Write(Fa), Write(App), Write(Fsf), Write(Stat), GrowFromPoint(l5, l5.get_start()), Write(st), run_time = 2)
            self.add(dl, dl2)
            self.wait(1)
            self.play(Transform(a, aa), Transform(a1, a1a), Transform(a2, a2a), Transform(a3, a3a), GrowArrow(va), Write(v), Transform(Fsf, Fkf), Transform(Stat, Kin), gr.animate.shift(LEFT*2), gr2.animate.shift(LEFT*2), gru.animate.shift(LEFT*2), gr2u.animate.shift(LEFT*2), GrowFromPoint(l6, l6.get_start()), Write(ki), run_time=3)
        