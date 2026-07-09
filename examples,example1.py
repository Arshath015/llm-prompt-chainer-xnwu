from llm_chainer import LLMChainer, Prompt

class Example1:
    def __init__(self):
        self.chainer = LLMChainer()

    def run(self):
        prompt1 = Prompt(text="Title Slide")
        prompt2 = Prompt(text="Content Slide")
        self.chainer.add_prompt(prompt1)
        self.chainer.add_prompt(prompt2)
        composition = self.chainer.generate_composition()
        print(composition)

if __name__ == "__main__":
    example = Example1()
    example.run()