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
    Ellipse,
    ORANGE,
    ORIGIN,
    MathTex,
    ReplacementTransform,
    Line,
)

config.background_color = "#1A1D24"


class DataRetrievalAndGeneration(Scene):
    def construct(self):
        # Title
        title_input = Text("User Input", font_size=40, color="#FAC13C").to_edge(UP)

        ### User Query
        user_query = VGroup(
            Rectangle(width=2.5, height=2.5, fill_color=BLUE, fill_opacity=0.5),
            Text("What\n is\n the\n...?", font_size=22).move_to(
                [0, 0, 0]
            ),
        )
        user_query_label = Text("User Query", font_size=20, color="#FAC13C").next_to(
            user_query, DOWN, buff=0.1
        )
        user_query_group = VGroup(user_query, user_query_label).shift(LEFT * 4)
        self.play(FadeIn(user_query_group))

        ### Embedding Model
        embedding_model = Ellipse(
            width=1.5, height=2.5, fill_color=ORANGE, fill_opacity=0.5
        )
        embedding_model_label = Text(
            "Embedding Model", font_size=20, color="#FAC13C"
        ).next_to(embedding_model, DOWN, buff=0.1)
        embedding_model_group = VGroup(embedding_model, embedding_model_label)
        embedding_model_group.next_to(user_query_group, RIGHT, buff=2.5)
        self.play(FadeIn(embedding_model_group))

        ### Arrow from User Query to Embedding Model
        arrow_user_to_model = Arrow(
            user_query.get_right(), embedding_model.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_user_to_model))

        ### Embedding the Query
        embed_query = Rectangle(
            width=1.0, height=3.5, fill_color=GREEN, fill_opacity=0.5
        )
        embed_values_texts = [
            Text(f"{random.uniform(0, 1):.2f}", font_size=16) for _ in range(4)
        ]
        embed_values_texts.append(Text("...", font_size=16))
        embed_values = VGroup(*embed_values_texts)
        embed_values.arrange(DOWN, center=False, aligned_edge=LEFT)
        embed_values.move_to(embed_query.get_center())

        embed_query_label = Text(
            "Embedded Query", font_size=20, color="#FAC13C"
        ).next_to(embed_query, DOWN, buff=0.1)
        embed_query_group = VGroup(embed_query, embed_values, embed_query_label)
        embed_query_group.next_to(embedding_model_group, RIGHT, buff=2.5)
        self.play(FadeIn(embed_query_group))

        arrow_model_to_query = Arrow(
            embedding_model.get_right(), embed_query.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_model_to_query))

        ### Remove the other components including arrows and move the embed_query to the left
        self.play(
            FadeOut(user_query_group),
            FadeOut(embedding_model_group),
            FadeOut(arrow_user_to_model),
            FadeOut(arrow_model_to_query),
        )
        self.play(embed_query_group.animate.to_edge(LEFT).shift(LEFT * 0.5))

        # Title
        title_retriever = Text(
            "Retrieve Top-k Context", font_size=40, color="#FAC13C"
        ).to_edge(UP)

        self.play(ReplacementTransform(title_input, title_retriever))

        ### Vector DB
        vector_db_svg = SVGMobject("database-svgrepo-com-2.svg")
        vector_db_svg.set(width=2, height=2)  # Adjust the size as needed
        vector_db_label = Text(
            "Query Vector Store", font_size=20, color="#FAC13C"
        ).next_to(vector_db_svg, DOWN, buff=0.1)
        vector_db_group = VGroup(vector_db_svg, vector_db_label)
        vector_db_group.next_to(embed_query_group, RIGHT, buff=1.5)
        self.play(FadeIn(vector_db_group))

        arrow_query_to_vectordb = Arrow(
            embed_query.get_right(), vector_db_svg.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_query_to_vectordb))

        ### Retrieved Chunks
        chunks = (
            VGroup(
                *[
                    VGroup(
                        Rectangle(
                            width=2.5, height=0.5, fill_color=BLUE, fill_opacity=0.5
                        ),
                        Text("Lorem ipsum dolor sit", font_size=16).move_to([0, 0, 0]),
                    )
                    for _ in range(5)
                ]
                + [Text("...", font_size=20)]
            )
            .arrange(DOWN, buff=0.2)
            .shift(DOWN * 0.5)
        )
        chunks_label = Text("Retrieved Chunks", font_size=20, color="#FAC13C").next_to(
            chunks, DOWN, buff=0.3
        )
        chunks_group = VGroup(chunks, chunks_label)
        chunks_group.next_to(vector_db_group, RIGHT, buff=1.5)

        arrow_vector_db_to_chunks = Arrow(
            vector_db_svg.get_right(), chunks.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_vector_db_to_chunks))
        searched_label = Text("Search", font_size=20, color="#FAC13C").next_to(
            arrow_vector_db_to_chunks, UP, buff=0.1
        )
        self.play(FadeIn(searched_label))

        self.play(FadeIn(chunks_group))

        ### Top-k chunks
        tok_k_chunks = VGroup(
            *[
                VGroup(
                    Rectangle(width=2.5, height=0.5, fill_color=BLUE, fill_opacity=0.5),
                    Text("Lorem ipsum dolor sit", font_size=16).move_to([0, 0, 0]),
                )
                for _ in range(3)
            ]
        ).arrange(DOWN, buff=0.2)
        top_k_chunks_label = Text(
            "Retrieved Top-K Chunks", font_size=20, color="#FAC13C"
        ).next_to(tok_k_chunks, DOWN, buff=0.3)
        top_k_chunks_group = VGroup(tok_k_chunks, top_k_chunks_label).shift(UP * 1.5)
        top_k_chunks_group.next_to(chunks_group, RIGHT, buff=1.5)

        arrow_chunks_to_top_chunks = Arrow(
            chunks.get_right(), tok_k_chunks.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_chunks_to_top_chunks))
        filtered_label = Text("Filter", font_size=20, color="#FAC13C").next_to(
            arrow_chunks_to_top_chunks, UP, buff=0.1
        )
        self.play(FadeIn(filtered_label))
        self.play(FadeIn(top_k_chunks_group))

        ### Remove the other components including arrows and move the top-k chunks to the left
        self.play(
            FadeOut(title_retriever),
            FadeOut(embed_query_group),
            FadeOut(vector_db_group),
            FadeOut(chunks_group),
            FadeOut(arrow_query_to_vectordb),
            FadeOut(arrow_vector_db_to_chunks),
            FadeOut(searched_label),
            FadeOut(arrow_chunks_to_top_chunks),
            FadeOut(filtered_label),
        )
        self.play(top_k_chunks_group.animate.to_edge(LEFT).shift(DOWN * 2.2))

        # Title
        response_input = Text("Response Synthesis", font_size=40, color="#FAC13C").to_edge(
            UP
        )
        self.play(ReplacementTransform(title_retriever, response_input))

        user_query = VGroup(
            Rectangle(width=1.5, height=1.5, fill_color=BLUE, fill_opacity=0.5),
            Text("What\n is\n the\n...?", font_size=16).move_to(
                [0, 0, 0]
            ),
        )
        user_query_label = Text("User Query", font_size=20, color="#FAC13C").next_to(
            user_query, DOWN, buff=0.1
        )
        user_query_group = VGroup(user_query, user_query_label).shift(LEFT * 4)
        self.play(
            user_query_group.animate.to_edge(LEFT).shift(RIGHT * 0.8).shift(UP * 2.2)
        )

        # System Prompt
        system_prompt = VGroup(
            Rectangle(width=1.2, height=1.2, fill_color=BLUE, fill_opacity=0.5),
            Text("You are \nsmart bot...", font_size=12).move_to([0, 0, 0]),
        )
        system_prompt_label = Text(
            "System Prompt", font_size=20, color="#FAC13C"
        ).next_to(system_prompt, DOWN, buff=0.1)
        system_prompt_group = (
            VGroup(system_prompt, system_prompt_label)
            .next_to(user_query_group, RIGHT, buff=1)
            .shift(DOWN * 2)
            .shift(LEFT * 0.5)
        )

        self.play(Create(system_prompt_group))

        plus_circle_location = ORIGIN - 0.5
        # Add symbol inside a tiny circle (moved outside the system prompt box)
        add_symbol = MathTex("+").move_to(plus_circle_location).scale(0.5)
        add_circle = Circle(radius=0.25, color=WHITE).move_to(plus_circle_location)
        add_circle_group = VGroup(add_circle, add_symbol).shift(UP * 0.5)

        arrow_query = Arrow(
            start=user_query.get_right(), end=add_circle_group.get_left(), color=BLUE
        )
        arrow_chunks = Arrow(
            start=top_k_chunks_group.get_right(),
            end=add_circle_group.get_left(),
            color=BLUE,
        )
        arrow_prompt = Arrow(
            start=system_prompt.get_right(), end=add_circle_group.get_left(), color=BLUE
        )

        self.play(
            Create(arrow_query),
            Create(arrow_chunks),
            Create(arrow_prompt),
            Create(add_circle_group),
        )

        concat_label = Text("Concatenation", font_size=20, color="#FAC13C").next_to(
            add_circle_group, UP, buff=0.3
        )
        self.play(FadeIn(concat_label))

        llm = Circle(radius=1.0, fill_color=ORANGE, fill_opacity=0.5)
        llm_label = Text("LLM", font_size=20).move_to(llm)
        llm_group = VGroup(llm, llm_label)
        llm_group.next_to(add_circle_group, RIGHT, buff=1.5)
        self.play(FadeIn(llm_group))

        arrow_llm = Arrow(
            start=add_circle_group.get_right(), end=llm.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_llm))

        response = VGroup(
            Rectangle(width=2.5, height=2.5, fill_color=BLUE, fill_opacity=0.5),
            Text("The\n ans\n is\n...", font_size=10).move_to(
                [0, 0, 0]
            ),
        )
        response_label = Text("Response", font_size=20).next_to(
            response, DOWN, buff=0.1
        )
        response_group = VGroup(response, response_label)
        response_group.next_to(llm_group, RIGHT, buff=1.5).shift(DOWN * 0.2)
        self.play(FadeIn(response_group))

        arrow_response = Arrow(
            start=llm.get_right(), end=response.get_left(), color=BLUE
        )
        self.play(GrowArrow(arrow_response))

        self.play(
            FadeOut(response_input),
            FadeOut(user_query_group),
            FadeOut(system_prompt_group),
            FadeOut(top_k_chunks_group),
            FadeOut(add_circle_group),
            FadeOut(arrow_query),
            FadeOut(arrow_chunks),
            FadeOut(arrow_prompt),
            FadeOut(concat_label),
            FadeOut(llm_group),
            FadeOut(arrow_llm),
            FadeOut(response_group),
            FadeOut(arrow_response),
        )

        # Create a group of all pipeline components

        _full_pipeline_group = VGroup(
            user_query_group,
            embed_query_group,
            vector_db_group,
            top_k_chunks_group,
            add_circle_group,
            llm_group,
            response_group,
        ).arrange(RIGHT, buff=1.5).move_to(ORIGIN)

        full_pipeline_group = VGroup(
            _full_pipeline_group,
            system_prompt_group
        ).arrange(DOWN, buff=1.5).move_to(ORIGIN)

        # Adjust scale to fit the entire pipeline in view
        self.play(full_pipeline_group.animate.scale_to_fit_width(self.camera.frame_width * 0.97))

        title_last = Text("Simple RAG Pipeline", font_size=40, color="#FAC13C").to_edge(UP)
        self.play(Create(title_last))
        
        # Left to right arrows
        arrow_user_to_embed = Arrow(user_query.get_right(), embed_query.get_left(), color=BLUE)
        arrow_embed_to_db = Arrow(embed_query.get_right(), vector_db_svg.get_left(), color=BLUE)
        arrow_db_to_chunks = Arrow(vector_db_svg.get_right(), tok_k_chunks.get_left(), color=BLUE)

        # Arrows to LLM
        arrow_user_to_concat = VGroup(
            Line(user_query.get_top(), user_query.get_top() + UP*1.0, color=BLUE),
            Line(user_query.get_top() + UP*1.0, add_circle_group.get_top()+UP*1.5, color=BLUE),
            Arrow(add_circle_group.get_top()+UP*1.6, add_circle_group.get_top(), color=BLUE, buff=0.1)
        ) 

        arrow_top_k_to_concat = Arrow(top_k_chunks_group.get_right(), add_circle_group.get_left(), color=BLUE)

        arrow_system_prompt_to_concat = VGroup(
            Line(system_prompt_group.get_right(), add_circle_group.get_bottom() + DOWN*2.6, color=BLUE),
            Arrow(add_circle_group.get_bottom() + DOWN*2.7, add_circle_group.get_bottom(), color=BLUE, buff=0.1)
        )

        # Arrow from LLM to Response
        arrow_concat_to_llm = Arrow(add_circle_group.get_right(), llm.get_left(), color=BLUE)
        arrow_llm_to_response = Arrow(llm.get_right(), response.get_left(), color=BLUE)
        
        # Display arrows
        self.play(GrowArrow(arrow_user_to_embed))
        self.play(GrowArrow(arrow_embed_to_db))
        self.play(GrowArrow(arrow_db_to_chunks))
        self.play(Create(arrow_user_to_concat))
        self.play(GrowArrow(arrow_top_k_to_concat))
        self.play(Create(arrow_system_prompt_to_concat))
        self.play(GrowArrow(arrow_concat_to_llm))
        self.play(GrowArrow(arrow_llm_to_response))

        self.wait(2)
