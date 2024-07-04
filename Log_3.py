from manim import *

BH_DARKGREEN = '#455D3E'
config.background_color = BH_DARKGREEN

class log(Scene):
    def construct(self):
        eq=MathTex(r"\log{a^b} = b\cdot\log{a}", )
        eq.shift(UP*3.4)
        p1=eq.copy()
        p1.next_to(eq, DOWN)
        proof=MathTex("Proof :").next_to(p1, LEFT*2).set_color("YELLOW")

        proof_eq=MathTex(r"\log{a^b} = x",
                         r"e^{\log{a^b}} = e^{x}",
                         r"a^b  = e^{x}",
                         r"a = e^{\frac{x}{b}}",
                         r"\log{a} = \frac{x}{b}",
                         r"b\cdot\log{a} = x",
                         r"\log{a^b} = b\cdot\log{a}")
                   
        box=SurroundingRectangle(proof_eq[6], color="YELLOW")

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
        self.play(Indicate(proof_eq[0]), Indicate(proof_eq[5]))
        self.wait()
        self.play(Write(proof_eq[6].next_to(proof_eq[5], DOWN*2)))
        box.move_to(proof_eq[6])
        self.play(Create(box))
        self.play(FadeOut(eq, proof, p1))
        self.play(FadeOut(proof_eq[0],proof_eq[1], proof_eq[2], proof_eq[3], proof_eq[4], proof_eq[5]))
        self.play(proof_eq[6].animate.center(), box.animate.center())
        self.wait()

    