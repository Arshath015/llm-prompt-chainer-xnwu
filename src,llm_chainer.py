from typing import List
from pydantic import BaseModel
import json

class Prompt(BaseModel):
    text: str

class Composition(BaseModel):
    title: str
    slides: List[str]

class LLMChainer:
    def __init__(self):
        self.prompts = []

    def add_prompt(self, prompt: Prompt):
        self.prompts.append(prompt)

    def generate_composition(self) -> Composition:
        # Generate the composition using the prompts
        title = self.prompts[0].text
        slides = [prompt.text for prompt in self.prompts[1:]]
        return Composition(title=title, slides=slides)

    def get_composition(self) -> Composition:
        return self.generate_composition()