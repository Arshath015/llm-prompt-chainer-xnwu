import pytest
from llm_chainer import LLMChainer, Prompt

class TestLLMChainer:
    def test_generate_composition(self):
        chainer = LLMChainer()
        prompt1 = Prompt(text="Title Slide")
        prompt2 = Prompt(text="Content Slide")
        chainer.add_prompt(prompt1)
        chainer.add_prompt(prompt2)
        composition = chainer.generate_composition()
        assert composition.title == "Title Slide"
        assert composition.slides == ["Content Slide"]

    def test_get_composition(self):
        chainer = LLMChainer()
        prompt1 = Prompt(text="Title Slide")
        prompt2 = Prompt(text="Content Slide")
        chainer.add_prompt(prompt1)
        chainer.add_prompt(prompt2)
        composition = chainer.get_composition()
        assert composition.title == "Title Slide"
        assert composition.slides == ["Content Slide"]