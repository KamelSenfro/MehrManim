#course
from manim import *

class Getters(Scene):
    def construct(self):
        rect = Rectangle(height=1, width=3, color=WHITE).to_edge(UL)
        self.wait(1)
        circ = Circle(radius=1, color=BLUE).to_edge(DOWN)
        arrow = Arrow(start=rect.get_bottom(), end=circ.get_top(), color=WHITE) 
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait(1)
        #manim -pql course.py Getters