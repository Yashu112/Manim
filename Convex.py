from manim import *
import random

#BH_DARKGREEN = '#455D3E'
#config.background_color = BH_DARKGREEN

class convex(Scene):
    def construct(self):

        l1= Text("Convex Sets", font_size=40)
        l1.shift(UP*2)
        l2= Text("A set is called Convex, if the line segment joining any 2 points lies in the set", font_size=30)
        l2.next_to(l1, DOWN)
        l3= Text("Let's understand this Geometrically...", font_size=30)
        l3.next_to(l2, DOWN)

        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(FadeOut(l1,l2, l3))

class circle(Scene):
    def construct(self):

        circle = Circle(radius=2.5, color=BLUE, fill_opacity=0.4)  

        e1=MathTex(r"S = \{(x,y) : x^2+y^2 \le a^2 \} ")
        e1.next_to(circle, UP*1.5)

        self.play(Write(e1))
        self.play(Create(circle)) 
                
        for i in range(0,5):

            p1=[random.uniform(-2,2), random.uniform(-2,2), 0]
            p2=[random.uniform(-2,2), random.uniform(-2,2), 0]
              
            d1=Dot(p1, color=YELLOW)
            d2=Dot(p2, color=YELLOW)

            l1=Line(start=p1, end=p2)

            self.play(FadeIn(d1,d2), Create(l1))
            self.play(FadeOut(d1,d2,l1))
        
        self.wait(2)
        self.play(FadeOut(e1, circle))

class hyperbola(Scene):
    def construct(self):
        hyper= ImplicitFunction(lambda x,y: -x**2/2 + y**2/2 - 0.5, color=GREEN, fill_color=GREEN, fill_opacity=0.4)
        
        eq=MathTex(r"S = \{(x,y) : y^2 - x^2 \ge a^2 \} ")      

        self.play(Write(eq))
        self.play(Create(hyper))

        for i in range(0,5):

            p1=[random.uniform(-1,1), random.uniform(-4,-1), 0]
            p2=[random.uniform(-1,1), random.uniform(1,4), 0]
              
            d1=Dot(p1, color=YELLOW)
            d2=Dot(p2, color=YELLOW)

            l1=Line(start=p1, end=p2)

            self.play(FadeIn(d1,d2), Create(l1))
            self.play(FadeOut(d1,d2,l1))

        self.wait(2)
        self.play(FadeOut(eq, hyper))

        bigc=Circle(radius=3.0, color=WHITE)  
        end=Tex("Thanks \n for \n Watching")

        self.play(Create(bigc), Write(end))
        self.wait(2)

            


