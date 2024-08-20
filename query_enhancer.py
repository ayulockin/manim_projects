import random

from manim import (
    MovingCameraScene,
    Scene,
    VGroup,
    Rectangle,
    Text,
    BLUE,
    DOWN,
    LEFT,
    FadeIn,
    GREEN,
    Square,
    Circle,
    UP,
    DOWN,
    RIGHT,
    Cutout,
    Write,
    RED,
    PI,
    Rotate,
    linear,
    Dot,
    ORIGIN,
    Arrow,
    GrowArrow,
    Create,
    SurroundingRectangle,
    YELLOW,
    MED_LARGE_BUFF,
    Line,
)


class QueryEnhancer(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # User Query
        user_query = VGroup(
            Rectangle(width=1.0, height=3.5, fill_color=BLUE, fill_opacity=0.5),
            Text("W\nh\na\nt\n \ni\ns\n \nt\nh\ne\n.\n.\n?", font_size=16).move_to(
                [0, 0, 0]
            ),
        )
        user_query_label = Text("User Query", font_size=20, color="#FAC13C").next_to(
            user_query, DOWN, buff=0.1
        )
        user_query_group = VGroup(user_query, user_query_label).shift(LEFT * 4)
        self.play(FadeIn(user_query_group))

        # Query Enhancer
        s1 = Square().scale(1.5)

        arrow_query_enhancer = Arrow(user_query.get_right(), s1.get_left(), buff=0.1)
        self.play(GrowArrow(arrow_query_enhancer))

        s2 = Circle().shift(UP - 0.2 + RIGHT - 0.2).scale(0.5)
        c = Cutout(s1, s2, fill_opacity=1, color=BLUE, stroke_color=RED)
        query_enhancer_label = Text(
            "Query Enhancer", font_size=20, color="#FAC13C"
        ).next_to(c, DOWN, buff=0.1)
        self.play(Write(c), run_time=2)
        self.play(Write(query_enhancer_label))

        # Keyword Extraction
        keywords = (
            Text("'Keyword 1', 'Keyword 2', ...", line_spacing=1, font_size=22)
            .next_to(c, RIGHT, buff=0.1)
            .shift(UP * 2.5)
            .shift(RIGHT * 1.3)
        )
        box_keywords = SurroundingRectangle(keywords, color=YELLOW, buff=MED_LARGE_BUFF)
        self.play(Create(keywords))
        self.play(Create(box_keywords))

        # Sub Queries
        sub_queries = (
            Text(
                "'Sub Query 1',\n'Sub Query 2',\n'Sub Query 3'\n...",
                line_spacing=1,
                font_size=22,
            )
            .next_to(c, RIGHT, buff=0.1)
            .shift(RIGHT * 1.3)
        )
        box_sub_queries = SurroundingRectangle(
            sub_queries, color=YELLOW, buff=MED_LARGE_BUFF
        )
        self.play(Create(sub_queries))
        self.play(Create(box_sub_queries))

        # Language Detection
        lang_detection = (
            Text("{'language': 'en'}", font_size=22)
            .next_to(c, RIGHT, buff=0.1)
            .shift(DOWN * 2.5)
            .shift(RIGHT * 1.3)
        )
        box_lang_dect = SurroundingRectangle(
            lang_detection, color=YELLOW, buff=MED_LARGE_BUFF
        )
        self.play(Create(lang_detection))
        self.play(Create(box_lang_dect))

        arrow_qe_to_keywords = VGroup(
            Line(c.get_top(), c.get_top() + UP * 1.0, color=BLUE),
            Arrow(
                c.get_top() + UP * 1.0, box_keywords.get_left(), color=BLUE, buff=0.01
            ),
        )
        self.play(Create(arrow_qe_to_keywords))

        arrow_qe_to_sub_queries = Arrow(
            c.get_right(), box_sub_queries.get_left(), color=BLUE, buff=0.01
        )
        self.play(Create(arrow_qe_to_sub_queries))

        arrow_qe_to_lang = VGroup(
            Line(
                query_enhancer_label.get_bottom(),
                query_enhancer_label.get_bottom() + DOWN * 0.65,
                color=BLUE,
            ),
            Arrow(
                query_enhancer_label.get_bottom() + DOWN * 0.65,
                box_lang_dect.get_left(),
                color=BLUE,
                buff=0.01,
            ),
        )
        self.play(Create(arrow_qe_to_lang))

        self.play(self.camera.frame.animate.scale(0.5).move_to(c))

        self.wait(2)
