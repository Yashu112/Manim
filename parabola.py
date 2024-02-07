from manim import *
    
class parabola(Scene):
        
    def construct(self):
        grid = Axes(x_range=[-8,8],
                    y_range=[-8,8])
        
        title=Text('4 Types of Parabola')
        
        f1= MathTex(r"x^2=4y")
        f1.to_corner(UP+RIGHT)
        
        f2=MathTex(r"x^2=-4y")
        f2.to_corner(DOWN+LEFT)
        
        f3=MathTex(r"y^2=4x")
        f3.to_corner(DOWN+RIGHT)
        
        f4=MathTex(r"y^2=-4x")
        f4.to_corner(UP+LEFT)
        
        p1= grid.plot(lambda x: (x**2)/4, color=GREEN)
        p2= grid.plot(lambda x: -(x**2)/4, color=RED)
        p3= ImplicitFunction(lambda x,y: y**2 - 4*x, color=BLUE)
        p4= ImplicitFunction(lambda x,y: y**2 + 4*x, color=YELLOW)
        
        end=Text("Thanks for Watching!!!", font_size=58)


        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.play(Create(grid), run_time=3)   
        
        self.play(Create(p1), Write(f1))
        self.wait(2)
        self.play(Transform(p1,p2), Transform(f1,f2))
        
        self.wait(2)
        self.play(Transform(p1,p3), Transform(f1,f3))
        
        self.wait(2)
        self.play(Transform(p1,p4), Transform(f1,f4))
        
        self.wait(2)
        self.play(FadeOut(grid,p1,f1))
        self.play(FadeIn(end))
        self.wait(2)      
        
            