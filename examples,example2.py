from llm_chainer import LLMChainer, Prompt

class Example2:
    def __init__(self):
        self.chainer = LLMChainer()

    def run(self):
        prompt1 = Prompt(text="Title Slide")
        prompt2 = Prompt(text="Content Slide")
        prompt3 = Prompt(text="Conclusion Slide")
        self.chainer.add_prompt(prompt1)
        self.chainer.add_prompt(prompt2)
        self.chainer.add_prompt(prompt3)
        composition = self.chainer.generate_composition()
        print(composition)

if __name__ == "__main__":
    example = Example2()
    example.run()