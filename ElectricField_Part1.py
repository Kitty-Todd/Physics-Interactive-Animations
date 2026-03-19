from manim import *
import manim_physics as mp
import numpy as np

# Globalsssss

def wind_field(point):
    x, y, _ = point
    x -= 1  # Fan origin in x-axis
    y -= 0   # Fan origin in y-axis

    # Compute the magnitude and direction of airflow
    distance = np.sqrt(x**2 + y**2)
    if distance == 0:
        return np.array([0, 0, 0])

    # Magnitude decreases with distance from the fan
    magnitude = 1 / (1 + 0.2 * distance)

    # Flow primarily in x-direction with some spreading in y-direction
    direction = np.array([-1, y / (distance + 0.1), 0])

    # Normalize and scale with magnitude
    return magnitude * direction

class ElectricFields(Scene):
    def construct(self):
        # The first part of the video is showcasing the 3 charges

        # Create the charges and set the position
        charge1 = mp.Charge(magnitude=1, point=np.array([-4, -1, 0]))
        charge2 = mp.Charge(magnitude=1, point=np.array([4, 1, 0]))

        charge3 = mp.Charge(magnitude=-1, point=np.array([0, 3, 0]))

        # Add to the scene
        self.add(charge1, charge2, charge3)

        # Create the lines that connect the charges
        line1 = Line(start = charge1.get_center(), end=charge3.get_center())
        line2 = Line(start = charge1.get_center(), end=charge2.get_center())
        line3 = Line(start = charge2.get_center(), end=charge3.get_center())

        # Add to the scene
        self.add(line1, line2, line3)

        # Create the Force arrows
        # Charge 1 arrows
        q1_f1_arrow = LabeledArrow(MathTex("\\vec{F_1}"), start=charge1.get_center(), end=charge3.get_center(), color=GREEN)
        
        # Reverse the direction of q1_f2_arrow while keeping the same magnitude
        q1_f2_start = charge1.get_center()
        q1_f2_end = charge2.get_center()
        q1_f2_magnitude = q1_f2_end - q1_f2_start
        reversed_q1_f2_end = q1_f2_start - q1_f2_magnitude
        q1_f2_arrow = LabeledArrow(MathTex("\\vec{F_2}"), start=charge1.get_center(), end=reversed_q1_f2_end, color=GREEN)

        q1_f1_arrow.scale(0.25, about_point=q1_f1_arrow.get_start())
        q1_f2_arrow.scale(0.25, about_point=q1_f2_arrow.get_start())


        # Charge 2 arrows
        q2_f3_arrow = LabeledArrow(MathTex("\\vec{F_3}"), start=charge2.get_center(), end=charge3.get_center(), color=GREEN)
        
        # Reverse the direction of q2_f2_arrow while keeping the same magnitude
        q2_f2_start = charge2.get_center()
        q2_f2_end = charge1.get_center()
        q2_f2_magnitude = q2_f2_end - q2_f2_start
        reversed_q2_f2_end = q2_f2_start - q2_f2_magnitude
        q2_f2_arrow = LabeledArrow(MathTex("\\vec{F_2}"), start=charge2.get_center(), end=reversed_q2_f2_end, color=GREEN)

        q2_f3_arrow.scale(0.25, about_point=q2_f3_arrow.get_start())
        q2_f2_arrow.scale(0.25, about_point=q2_f2_arrow.get_start())

        # Charge 3 arrows
        q3_f1_arrow = LabeledArrow(MathTex("\\vec{F_1}"), start=charge3.get_center(), end=charge1.get_center(), color=GREEN)
        q3_f3_arrow = LabeledArrow(MathTex("\\vec{F_3}"), start=charge3.get_center(), end=charge2.get_center(), color=GREEN)

        q3_f1_arrow.scale(0.25, about_point=q3_f1_arrow.get_start())
        q3_f3_arrow.scale(0.25, about_point=q3_f3_arrow.get_start())

        # Add the arrows to the Scene
        self.add(q1_f1_arrow, q1_f2_arrow, q2_f2_arrow, q2_f3_arrow, q3_f1_arrow, q3_f3_arrow)

        # Equation time
        equation = MathTex(
            "\\vec{F_c}", "=", "k_c", "{q_1", "q_2", "\\over", "r^2}", "\\hat{r}"
        )
        equation.move_to(DOWN*1.5)

        #Add the equation
        self.add(equation)

        #Run the scene for as long as desired
        self.wait(2.5)

        #Prepare the next scene of the charges floating in space
        self.play(FadeOut(line1,line2,line3
                          ,equation))

        #Scene runtime
        self.wait(2.5)

        #Remove the charges for the next scene and add the kite and fan
        self.play(FadeOut(charge1, charge2, charge3,
                          q1_f1_arrow, q1_f2_arrow,
                          q2_f2_arrow, q2_f3_arrow,
                          q3_f1_arrow, q3_f3_arrow))
        
        #Create the Fan VGroup
        fan_center = Dot(radius=0.15, color=WHITE)
        fan_body = Circle(radius = 1.2, color=WHITE)
        fan_base = Ellipse(width = 1.8, height= 0.2, color=WHITE).shift(DOWN*3)
        fan_stand = Line(start=fan_body.get_bottom(), end=fan_base.get_top(), color=WHITE)
        
        # Create the fan blades
        blade1 = Polygon(
            ORIGIN, 
            [0.3, 0.3, 0], 
            [0.8, 0, 0], 
            [-0.3, -0.3, 0],
            color=WHITE,
            fill_opacity=0.6
        ).shift(UP * 0.6).rotate(PI / 6)

        # Clone blades and position them
        blade2 = blade1.copy().rotate(PI * 2 / 3, about_point=fan_center.get_center())
        blade3 = blade1.copy().rotate(-PI * 2 / 3, about_point=fan_center.get_center())

        # Group the blades and center
        fan_blades = VGroup(blade1, blade2, blade3)
        fan = VGroup(fan_center, fan_blades, fan_body, fan_base, fan_stand).shift(RIGHT*3)

        #Create the kite
        kite_top = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).scale(2).shift(LEFT*3)
                
        # Create the string 
        kite_string = VMobject() 
        kite_string.set_points_as_corners( [[-0.6, -1, 0], 
                                            [-0.7, -1.1, 0], 
                                            [-0.5, -1.2, 0], 
                                            [-0.6, -1.3, 0], 
                                            [-0.5, -1.4, 0], 
                                            [-0.6, -1.5, 0]] 
                                        ).scale(3).shift(LEFT*3) 
        
        kite = VGroup(kite_top, kite_string)

        # Store the initial position of the kite
        kiteIP = kite.get_center()

        #Add the Fan and Kite to the scene
        self.play(FadeIn(fan, kite))

        #Running the scene for set time
        self.wait(5)

    #Next part of the scene is to add the streamlines/wind

    #Create the corner covers (hard coded)

        corner_cover1 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*5+RIGHT*7)
        corner_cover2 = Circle(radius=5, color=BLACK, fill_opacity=1).shift(UP*-5+RIGHT*7)

        
    # Create streamlines from the vector field
    # I define 3 different streamlines that will represent a slow/medium/fast fan speed.
    # I also slightly adjust the virtual_time variable for each, making it a bit larger for faster fields.

            # If things in the animation look a little bad, try changing the 'virtual time' paramenter by a couple.

        stream_lines_slow = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=2 # 
            )

        stream_lines_med = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=8 # 
            )

        stream_lines_fast = StreamLines(
                wind_field,
                stroke_width=2, # Make the lines wider
                max_anchors_per_line=30,
                virtual_time=12 # 
            )

        # This line adds an updater to the fan blades so that they will continue to rotate
        # throughout the animations.  
        # Multiplying the angle by 'speed' allows us to adjust the speed of the fan below.
        fan_blades.add_updater(lambda mob, dt: mob.rotate(angle=speed*dt*PI, 
                                                            about_point=fan_center.get_center())
                                )

    # Here we create the force vector that will illustrate the wind force.
    # Set vector parameters here:
        vec_color = PURE_GREEN
        vec_magnitude = 5
    # Function to compute vector direction and inverse distance magnitude
        def get_vector():
            direction = kite_top.get_center() - fan.get_center()  # Direction from red to blue
            distance = np.linalg.norm(direction)  # Compute distance
                
            if distance == 0:  # Avoid division by zero
                return Vector([0, 0, 0]).set_color(vec_color)

            unit_direction = direction / distance  # Normalize direction
            magnitude = vec_magnitude / distance  # Inverse proportionality (scaled factor for visibility)

            return Vector(unit_direction * magnitude).set_color(vec_color).move_to(kite_top.get_center()).shift(unit_direction * magnitude / 2)  # Shift for proper positioning

        # Create initial vector
        vec = get_vector()
            
        # Updater to dynamically adjust vector direction and magnitude
        def update_vector(mob):
            new_vec = get_vector()
            mob.put_start_and_end_on(new_vec.get_start(), new_vec.get_end())

        vec.add_updater(update_vector)

    # Start animations

        # Medium Wind Field

        speed = 1 # Change this to make the fan spin faster or slower
        vec_magnitude = 5 # Change this to update the base size of the force vector to account for wind strength.
        # Add in all scene elements
        self.add(stream_lines_med, corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        self.add(vec)
        # Start the StreamLines animation bit
        # Flow speed determines how quickly the stream lines will move
        stream_lines_med.start_animation(warm_up=False, flow_speed=1.5)
        # Wait a moment until moving on
        self.wait(3)
        self.play(kite.animate.move_to(RIGHT*2+DOWN*1), run_time=3)
        self.play(kite.animate.move_to(LEFT*2+UP*1), run_time = 3)

        # Slow Wind field
        speed = 0.5
        vec_magnitude = 2
        self.remove(stream_lines_med)
        self.add(stream_lines_slow,fan)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand, fan)
        stream_lines_slow.start_animation(warm_up=False, flow_speed=.5)
        self.wait(3)

        # Move the kite in this new field
        self.play(kite.animate.move_to(RIGHT*2 + UP*2), run_time = 2)
        self.play(kite.animate.move_to(LEFT*4 + DOWN*2), run_time = 2)
        self.play(kite.animate.move_to(RIGHT*2 + DOWN*2), run_time = 2)
        self.play(kite.animate.move_to(LEFT*2 + UP*2), run_time = 2)

        # Fast Wind field
        speed = 2.0
        vec_magnitude = 8
        self.remove(stream_lines_slow)
        self.add(stream_lines_fast,fan)
        self.add(corner_cover1, corner_cover2)
        self.add(fan_base,fan_stand)
        stream_lines_fast.start_animation(warm_up=False, flow_speed=3.5)
        self.wait(3)

        # Move the kite again
        self.play(kite.animate.move_to(fan.get_center() + LEFT*2), run_time = 2)
        self.play(kite.animate.move_to(UP * 2), run_time=2)
        self.play(kite.animate.move_to(DOWN * 2), run_time=2)

    #Fade everything out but the fan
        self.play(FadeOut(
            kite, stream_lines_fast, corner_cover1, corner_cover2, vec
        ))

    #Fade In new arrows for a vector field
    
    # Create a line of large arrows on the left side of the fan
        left_arrows = VGroup()
        left_num_arrows = 6
        right_num_arrows = 2
        arrow_length = 1
        spacing = arrow_length + 0.5  # Adjust spacing based on arrow size
        for i in range(left_num_arrows):
            start_point = LEFT * (i * spacing) + fan_center.get_center() + LEFT * 1.5 # Position on the left
            end_point = start_point + LEFT * arrow_length
            arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(2)
            left_arrows.add(arrow)

    # Create a line of large arrows on the right side of the fan
        right_arrows = VGroup()
        for i in range(right_num_arrows):
            start_point = RIGHT * (i * spacing) + fan_center.get_center() + RIGHT * 2.35  # Position on the right
            end_point = start_point + LEFT * arrow_length
            arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(2)
            right_arrows.add(arrow)

    # Create a ring of arrows centered above the fan
        up_arrows = VGroup()
        num_arrows = 10  # Number of arrows in the ring
        radius = 4  # Radius of the ring
        for i in range(num_arrows):
            if i == 8: # Skips creating the 8th arrow (the one inside the fan)
                continue
            angle = i * TAU / num_arrows
            start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0]) + fan_center.get_center() + UP * radius
            end_point = np.array([radius * np.cos(angle - PI/6), radius * np.sin(angle - PI/6), 0]) + fan_center.get_center() + UP * radius
            arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(0.65)
            up_arrows.add(arrow)

    # Create a ring of arrows centered below the fan
        down_arrows = VGroup()
        for i in range(num_arrows):
            if i == 2: # Skipping the arrow in the fan
                continue
            angle = i * TAU / num_arrows
            start_point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0]) + fan_center.get_center() + DOWN * radius
            end_point = np.array([radius * np.cos(angle + PI/6), radius * np.sin(angle + PI/6), 0]) + fan_center.get_center() + DOWN * radius
            arrow = Arrow(start=start_point, end=end_point, color=GREEN).scale(0.65)
            down_arrows.add(arrow)

    #Create arrow Vgroup for them all to play at once
        all_arrows = VGroup(left_arrows, right_arrows)
        self.play(FadeIn(all_arrows,
                            up_arrows,
                            down_arrows
        ))
            
        self.wait(5)
    #Add new kites to different positions in the vector field

    # Start grabbing the position to put the kite at
        left_arrow_kite = left_arrows[3]
        right_arrow_kite = right_arrows[1]
        up_arrow_kite = up_arrows[6]
            
        # Create the kites and move them to their respective arrows
        left_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(left_arrow_kite.get_center())
            
        right_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(right_arrow_kite.get_center())
            
        up_kite = Polygon( [-0.6, 0, 0], 
                           [-1, 0.5, 0], 
                           [-0.6, 1, 0], 
                           [-0.2, 0.5, 0], 
                           color=WHITE, 
                           fill_opacity=0.6
                        ).move_to(up_arrow_kite.get_center())
            
    # Add arrows to the kites
        left_kite_arrow = Arrow(start=left_kite.get_center(), end=left_kite.get_center() + LEFT * 2, color=YELLOW, stroke_width=6)
        right_kite_arrow = Arrow(start=right_kite.get_center(), end=right_kite.get_center() + LEFT * 2, color=YELLOW, stroke_width=6)
        up_kite_arrow = Arrow(start=up_kite.get_center(), end=up_kite.get_center() + UP * 1.5 + LEFT * 0.5, color=YELLOW, stroke_width=6)

    # Create VGroups for each kite and arrow
        left_kite_group = VGroup(left_kite, left_kite_arrow)
        right_kite_group = VGroup(right_kite, right_kite_arrow)
        up_kite_group = VGroup(up_kite, up_kite_arrow)

        # Animate the VGroups
        self.play(FadeIn(left_kite_group, right_kite_group, up_kite_group))

        self.wait(2.5)
    
    #Remove the kite and arrows
        self.play(FadeOut(left_kite_group, right_kite_group, up_kite_group,
                          all_arrows, up_arrows, down_arrows))

    #Animate the kite moving in a semi-circle around the origin and then back to its initial position
        self.play(FadeIn(kite, vec))
        radius = 3
        angle = PI # Semi-circle
        path = Arc(radius=radius, angle=angle, start_angle=PI/2).shift(kite.get_center()) 
        self.play(MoveAlongPath(kite, path), run_time=10)
        self.play(kite.animate.move_to(kiteIP), run_time=2)
        kite_top.set_color(RED)

    #Make the kite grow and the vector shrink
        self.play(kite.animate.scale(2),
                  vec.animate.scale(0.5), run_time=5)

    #Make the kite shrink
        self.play(kite.animate.scale(0.25), 
                  vec.animate.scale(4), run_time=5)
        
    #Reset the scale and move the kite away
        self.play(kite.animate.scale(2), run_time=5)
        self.play(kite.animate.shift(LEFT*2), run_time=5)

        self.play(kite.animate.shift(RIGHT*2), run_time=5)

    # Create the objects to transition to
        kite_charge = mp.Charge(magnitude=1, point=kite.get_center())
        fan_charge = mp.Charge(magnitude=5, point=fan_blades.get_center())



    # Transform!
        self.add(kite)
        self.add(fan)
        self.wait(2)

        self.play(Transform(kite, kite_charge))
        self.play(Transform(fan, fan_charge))
        self.wait(2)

    #Move the kite charge around
        self.play(kite_charge.animate.move_to(RIGHT*2 + UP*2),
                  kite.animate.move_to(RIGHT*2 + UP*2), run_time = 2)
        self.play(kite_charge.animate.move_to(LEFT*2 + DOWN*2), 
                  kite.animate.move_to(LEFT*2 + DOWN*2), run_time = 2)
        self.play(kite_charge.animate.move_to(RIGHT*2 + DOWN*2),
                  kite.animate.move_to(RIGHT*2 + DOWN*2), run_time = 2)
        self.play(kite_charge.animate.move_to(LEFT*2 + UP*2),
                  kite.animate.move_to(LEFT*2 + UP*2), run_time = 2)
    
    #Move the kite and fan towards the Origin
        self.play(kite_charge.animate.move_to(ORIGIN + LEFT),
                  kite.animate.move_to(ORIGIN + LEFT))
        self.play(fan_charge.animate.move_to(ORIGIN + RIGHT),
                  fan.animate.move_to(ORIGIN + RIGHT))

    #Remove the background objects to prepare for the electric field
        self.play(FadeOut(fan, kite, vec))

    # Create the electric field of the fan charge
        field1 = mp.ElectricField(fan_charge)
        self.play(FadeIn(field1))
        self.wait(5)

    #New scene
        self.play(FadeOut(field1))
        self.play(FadeOut(kite_charge, fan_charge,
                    kite, fan))


    # Go back to the 3 charge system
        field2 = mp.ElectricField(charge1, charge2, charge3)

        self.play(FadeIn(charge1, charge2, charge3))
        self.play(FadeIn(field2))

        self.wait(10)
