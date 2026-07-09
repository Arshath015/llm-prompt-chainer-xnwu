from typing import List
from llm_chainer import Prompt

class PromptOrchestrator:
    def __init__(self):
        self.prompts = []

    def add_prompt(self, prompt: Prompt):
        self.prompts.append(prompt)

    def generate_output(self) -> List[str]:
        # Generate the output using the prompts
        output = []
        for prompt in self.prompts:
            output.append(prompt.text)
        return output