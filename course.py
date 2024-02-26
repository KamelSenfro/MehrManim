#course
from manim import *

class Course(Scene):
    def construct(self):
        
        circ = Circle( radius=2.3, color=BLUE, fill_opacity=0.5)
        self.play(Create(circ))
        #manim -p -ql course.py Course