from numpy import sqrt
from manim import *

class Love(Scene):
    def construct(self):
        intro=Text("What is Equation of Love?")
        equation= MathTex(r"x^2 + \left(y - \sqrt{|x|}\right)^2 = 2")
        
        graph = ImplicitFunction(
            lambda x, y: x ** 2 + (y- sqrt(abs(x)))**2 - 2,
            color=RED, fill_opacity=0.8
        )
        plane=NumberPlane()

        self.play(Write(intro))
        self.play(FadeOut(intro))
        self.play(FadeIn(equation))
        self.wait(1)
        self.play(equation.animate.to_edge(UP))
        self.play(Create(plane))
        self.play(DrawBorderThenFill(graph), run_time=5)
        self.play(FadeOut(plane))
        self.play(Indicate(graph))
        self.wait()
        self.play(FadeOut(equation,graph))
        