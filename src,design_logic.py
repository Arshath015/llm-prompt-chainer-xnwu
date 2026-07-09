from typing import List
from llm_chainer import Composition

class DesignLogic:
    def __init__(self):
        self.composition = None

    def generate_composition(self, output: List[str]) -> Composition:
        # Generate the composition using the output
        title = output[0]
        slides = output[1:]
        return Composition(title=title, slides=slides)

    def get_composition(self) -> Composition:
        return self.generate_composition([])