#course
from manim import *

class Course(Scene):
    def construct(self):
        name = Text("Kamel", font="Arial", color=GOLD).to_edge(center_of_mass,buff=0.5) 
        sq = Square(side_length=0.5, fill_color=GREEN).shift(LEFT * 3)
        tri = Triangle().scale(0.5).to_edge(DR)
        self.play(Write(name))
        self.wait(1.5)
        self.play(DrawBorderThenFill(sq))
        self.wait(1.5)
        self.play(DrawBorderThenFill(tri))
        self.play(name.animate.to_edge(UR), run_time=2)
        self.wait(1.5)
        self.play(sq.animate.scale(2).shift(UP * 2), run_time=2)
        

#manim -pql course.py Course