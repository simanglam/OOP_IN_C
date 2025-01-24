from pathlib import Path
from manim import *
from manim_slides.slide import Slide

from manim.mobject.text.text_mobject import remove_invisible_chars

from util.TextBox import TextBox

Text.set_default(font = "HanWangMingBlack")

class Inheritance(Slide, Scene):
    def construct(self):
        inheritance_text = Tex("\\textbf{Inheritance}").scale(3)
        inheritance_text.generate_target()
        inheritance_text.target.move_to((-5.25, 3.25, 0)).scale(0.25)
        
        self.play(Write(inheritance_text))
        self.next_slide()
        explain_text = Tex("one class is formed by extending the definition\\\\of another class to include additional fields\\\\or member functions.", tex_environment = "large")
        self.play(ReplacementTransform(inheritance_text, explain_text))
        self.next_slide()
        
        code_example = Code(Path("..", "code_snippet", "FileImage.java"))
        
        PNG_example = Code(Path("..", "code_snippet", "PNGImage.java")).scale(1.5)
        JPNG_example = Code(Path("..", "code_snippet", "JPNGImage.java")).scale(1.5)
        self.play(ReplacementTransform(explain_text, code_example))
        self.next_slide()
        
        self.play(ReplacementTransform(code_example, PNG_example))
        self.next_slide()
        
        self.play(ReplacementTransform(PNG_example, JPNG_example))
        self.next_slide()
        
        lines: list[Line] = []
        file_image_text = TextBox(Tex("FileImage")).scale(1.5).move_to((0, 2.5, 0))
        JPG_image_text = TextBox(Tex("JPGImage")).scale(1.5).move_to((2.5, -1, 0))
        PNG_image_text = TextBox(Tex("PNGImage")).scale(1.5).move_to((-2.5, -1, 0))
        lines.append(Line(file_image_text.get_bottom(), JPG_image_text.get_top()))
        lines.append(Line(file_image_text.get_bottom(), PNG_image_text.get_top()))
        
        self.play(ReplacementTransform(JPNG_example, file_image_text))
        self.next_slide()
        
        self.play(FadeIn(PNG_image_text, JPG_image_text, *lines))
        self.next_slide()
        
        inheritance_in_c_text = Tex("Inheritance in C").scale(3)
        
        self.play(FadeOut(file_image_text, JPG_image_text, PNG_image_text, *lines))
        self.play(Write(inheritance_in_c_text))
        self.next_slide()
        
        point_example = Code(Path("..", "code_snippet", "Point.c")).scale(1.5)
        label_point_example = Code(Path("..", "code_snippet", "LabelPoint.c")).scale(0.9)
        
        self.play(ReplacementTransform(inheritance_in_c_text, point_example))
        self.next_slide()
        
        self.play(ReplacementTransform(point_example, label_point_example))
        self.next_slide()
        
        code_snippet = Code(None, "b->x", language = "c", add_line_numbers = False).scale(4)
        label_point_struct = VGroup(SurroundingRectangle(TextBox(Tex("int x;"))))
        self.play(ReplacementTransform(label_point_example, code_snippet))