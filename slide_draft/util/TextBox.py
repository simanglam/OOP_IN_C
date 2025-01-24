from manim import *

class TextBox(VGroup):
    def __init__(self,
            text: Mobject, 
            buff = 0.3,
            fill_color = ManimColor.from_hex("#222222"),
            stroke_color = WHITE,
            corner_radius = 0.2,
            stroke_width = 1,
            fill_opacity = 1
        ):
        
        super().__init__()
        box = SurroundingRectangle(text,
            buff = buff,
            fill_color = fill_color,
            stroke_color = stroke_color,
            corner_radius = corner_radius,
            stroke_width = stroke_width,
            fill_opacity = fill_opacity
        )
        text.move_to(box.get_center())
        self.add(box, text)
