import pytest
from prompt_orchestrator import PromptOrchestrator, Prompt

class TestPromptOrchestrator:
    def test_generate_output(self):
        orchestrator = PromptOrchestrator()
        prompt1 = Prompt(text="Prompt 1")
        prompt2 = Prompt(text="Prompt 2")
        orchestrator.add_prompt(prompt1)
        orchestrator.add_prompt(prompt2)
        output = orchestrator.generate_output()
        assert output == ["Prompt 1", "Prompt 2"]