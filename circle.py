from manim import *

BH_DARKGREEN = '#455D3E'
config.background_color = BH_DARKGREEN

class circle(Scene):
    def construct(self):
        
        e1=MathTex(r"x^2+y^2=a^2", tex_template=TexFontTemplates.french_cursive)
        e2=MathTex(r"(x-h)^2 + y^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e3=MathTex(r"(x-h)^2 + (y-k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e4=MathTex(r"x^2 + (y-k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e5=MathTex(r"(x+h)^2 + (y-k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e6=MathTex(r"(x+h)^2 + y^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e7=MathTex(r"(x+h)^2 + (y+k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e8=MathTex(r"x^2 + (y+k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)
        e9=MathTex(r"(x-h)^2 + (y+k)^2 = a^2", tex_template=TexFontTemplates.french_cursive)     
                   
        c1 = ImplicitFunction(
            lambda x, y: x ** 2 + y ** 2 - 1,
        )
        c2 = ImplicitFunction(
            lambda x, y: (x-2) ** 2 + y ** 2 - 1,
        )

        c3 = ImplicitFunction(
            lambda x, y: (x-2) ** 2 + (y-2) ** 2 - 1,
        )
        c4 = ImplicitFunction(
            lambda x, y: x ** 2 + (y-2) ** 2 - 1,
        )
        c5 = ImplicitFunction(
            lambda x, y: (x+2) ** 2 + (y-2) ** 2 - 1,
        )
        c6 = ImplicitFunction(
            lambda x, y: (x+2) ** 2 + y ** 2 - 1,
        )
        c7 = ImplicitFunction(
            lambda x, y: (x+2) ** 2 + (y+2) ** 2 - 1,
        )
        c8 = ImplicitFunction(
            lambda x, y: x ** 2 + (y+2) ** 2 - 1,
        )
        c9 = ImplicitFunction(
            lambda x, y: (x-2) ** 2 + (y+2) ** 2 - 1,
        )

        circles=[c2,c3,c4,c5,c6,c7,c8,c9]
        eqs=[e2,e3,e4,e5,e6,e7,e8,e9]

        e1.to_edge(UP, buff=0.1)
        for k in eqs:
            k.to_edge(UP, buff=0.1)
        
        ax=Axes(tips=False)

        bigc=Circle(radius=3.0, color=WHITE)
        end=Tex("Thanks \n for \n Watching")
        intro=Tex("Circles?")

        self.play(Write(intro))
        self.play(FadeOut(intro))
        self.play(Create(ax))
        self.play(Create(c1), Create(e1))
        self.wait(2)
        for i,j in zip(circles,eqs):
            self.play(Transform(c1,i), Transform(e1,j))
            self.wait(2)
        self.play(Transform(c1,bigc), Unwrite(e1), Uncreate(ax))
        self.play(Write(end))
        self.wait(2)
