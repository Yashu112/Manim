from manim import *

BH_DARKGREEN = '#455D3E'
config.background_color = BH_DARKGREEN

class log(Scene):
    def construct(self):
        eq=MathTex(r"\log{a} - \log{b} = \log{\frac{a}{b}}", )
        eq.shift(UP*3.4)
        p1=eq.copy()
        p1.next_to(eq, DOWN)
        proof=MathTex("Proof :").next_to(p1, LEFT*2).set_color("YELLOW")

        proof_eq=MathTex(r"\log{a} - \log{b} = x",
                         r"e^{\log{a} - \log{b}} = e^{x}",
                         r"\frac{e^{\log{a}}} {e^{\log{b}}} = e^{x}",
                         r"\frac{a}{b} = e^{x}",
                         r"\log{\frac{a}{b}} = x",
                         r"\log{a} - \log{b} = \log{\frac{a}{b}}")
                   
        box=SurroundingRectangle(proof_eq[5], color="YELLOW")

        self.play(Write(eq))
        self.play(Write(proof), Write(p1))
        self.play(Transform(p1,proof_eq[0].next_to(eq, DOWN)))
        self.play(Write(proof_eq[1].next_to(proof_eq[0], DOWN)))
        self.wait()
        self.play(Write(proof_eq[2].next_to(proof_eq[1], DOWN)))
        self.wait()
        self.play(Write(proof_eq[3].next_to(proof_eq[2], DOWN)))
        self.wait()
        self.play(Write(proof_eq[4].next_to(proof_eq[3], DOWN)))
        self.wait()
        self.play(Write(proof_eq[5].next_to(proof_eq[4], DOWN*2)))
        box.move_to(proof_eq[5])
        self.play(Create(box))
        self.play(FadeOut(eq, proof, p1))
        self.play(FadeOut(proof_eq[0],proof_eq[1], proof_eq[2], proof_eq[3], proof_eq[4]))
        self.play(proof_eq[5].animate.center(), box.animate.center())
        self.wait()

    