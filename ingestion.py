import random

from manim import *
from manim import (
    Scene,
    Text,
    VGroup,
    Rectangle,
    DOWN,
    UP,
    RIGHT,
    LEFT,
    BLUE,
    GREEN,
    YELLOW,
    RED,
    PURPLE,
    TEAL,
    Arrow,
    FadeIn,
    FadeOut,
    Write,
    GrowArrow,
    Create,
    Transform,
    Animation,
    Circle,
    SVGMobject,
    config,
    WHITE,
)

config.background_color = "#1A1D24"


class DataIndexing(Scene):
    def construct(self):
        # Title
        title = Text("Data Indexing", font_size=40, color="#FAC13C").to_edge(UP)
        self.play(Write(title))

        # Components
        documents = VGroup(
            *[SVGMobject("document-pagel-svgrepo-com.svg", height=1.5, width=1.0).set_color(WHITE) for _ in range(3)]
        ).arrange(DOWN, buff=0.2)
        documents_label = Text("Documents", font_size=24, color="#FAC13C").next_to(documents, DOWN)
        documents_group = VGroup(documents, documents_label)

        # Adding lorem ipsum text to the text chunks
        lorem_ipsum = "Lorem ipsum dolor sit"
        text_chunks = VGroup(
            *[
                VGroup(
                    Rectangle(width=3, height=0.5, fill_color=BLUE, fill_opacity=0.5),
                    Text(lorem_ipsum, font_size=16).move_to([0, 0, 0]),
                )
                for i in range(4)
            ]
        ).arrange(DOWN, buff=0.2)
        text_chunks_label = Text("Text Chunks", font_size=24, color="#FAC13C").next_to(
            text_chunks, DOWN
        )
        text_chunks_group = VGroup(text_chunks, text_chunks_label)

        # Adding random float values to the vector embeddings
        vector_embeddings = VGroup(
            *[
                VGroup(
                    Rectangle(width=3, height=0.5, fill_color=GREEN, fill_opacity=0.5),
                    Text(
                        ", ".join([f"{random.uniform(0, 1):.2f}" for _ in range(5)]),
                        font_size=16,
                    ).move_to([0, 0, 0]),
                )
                for _ in range(4)
            ]
        ).arrange(DOWN, buff=0.2)
        vector_embeddings_label = Text(
            "Vector Embeddings", font_size=24, color="#FAC13C"
        ).next_to(vector_embeddings, DOWN)
        vector_embeddings_group = VGroup(vector_embeddings, vector_embeddings_label)

        # Vector DB
        vector_db_svg = SVGMobject(
            "database-svgrepo-com-2.svg"
        )  # Replace with the correct path
        vector_db_svg.set(width=2, height=2)  # Adjust the size as needed
        vector_db_label = Text("Vector DB", font_size=24, color="#FAC13C").next_to(vector_db_svg, DOWN)
        vector_db_group = VGroup(vector_db_svg, vector_db_label)

        # Arrange components
        components = VGroup(
            documents_group, text_chunks_group, vector_embeddings_group, vector_db_group
        ).arrange(RIGHT, buff=1)
        components.next_to(title, DOWN, buff=1)

        # Arrows between the stages (created dynamically during animations)
        arrow1 = Arrow(
            documents_group.get_right(), text_chunks_group.get_left(), buff=0.1
        )
        arrow2 = Arrow(
            text_chunks_group.get_right(), vector_embeddings_group.get_left(), buff=0.1
        )
        arrow3 = Arrow(
            vector_embeddings_group.get_right(), vector_db_group.get_left(), buff=0.1
        )

        # Animations
        self.play(Create(documents_group))
        self.play(Transform(documents.copy(), text_chunks))
        self.play(Create(arrow1))
        self.play(Write(text_chunks_label))

        self.play(Transform(text_chunks.copy(), vector_embeddings))
        self.play(Create(arrow2))
        self.play(Write(vector_embeddings_label))

        self.play(Transform(vector_embeddings.copy(), vector_db_svg))
        self.play(Create(arrow3))
        self.play(Write(vector_db_label))

        self.wait(2)