# LLM Prompt Chainer for Strategic Slide Generation

[![Python Version](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/downloads/release/python-390/) [![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT) [![Build Status](https://img.shields.io/badge/Build-passing-green)](https://github.com/) [![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-black)](https://peps.python.org/pep-0008/)

The LLM Prompt Chainer submodule is designed to automate the process of generating strategic slide compositions for startups, agencies, and enterprises. By leveraging LLM prompt orchestration and chaining, this submodule converts raw ideas, outlines, or briefs into bespoke high-contrast visual slide compositions.

## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Studies](#case-studies)
* [Testing](#testing)
* [Performance Considerations or Limitations](#performance-considerations-or-limitations)
* [Roadmap](#roadmap)
* [License](#license)

## Overview
The LLM Prompt Chainer submodule addresses the need for automated strategic slide generation. By leveraging design-logic and constraint solving, this submodule generates structured JSON layouts for various slide types, including bento grids, KPI dashboards, and editorial layouts.

## Tech Stack
* Python 3.9
* numpy
* opencv-python
* pillow
* requests
* pydantic
* dataclasses

## Architecture
```
+---------------+
|  LLM Prompt  |
|  Chainer API  |
+---------------+
       |
       |
       v
+---------------+
|  Prompt Or-   |
|  chestrator   |
+---------------+
       |
       |
       v
+---------------+
|  Design Logic |
|  and Constraint|
|  Solver       |
+---------------+
       |
       |
       v
+---------------+
|  JSON Layout   |
|  Generator     |
+---------------+
```
The LLM Prompt Chainer submodule consists of four main components: the LLM Prompt Chainer API, the Prompt Orchestrator, the Design Logic and Constraint Solver, and the JSON Layout Generator. The LLM Prompt Chainer API provides a simple interface for users to input their raw ideas, outlines, or briefs. The Prompt Orchestrator is responsible for orchestrating and chaining LLM prompts to generate the desired output. The Design Logic and Constraint Solver generates structured JSON layouts based on the output from the Prompt Orchestrator. Finally, the JSON Layout Generator takes the structured JSON layouts and generates the final slide compositions.

## Theoretical Background
The LLM Prompt Chainer submodule leverages LLM prompt orchestration and chaining to generate bespoke high-contrast visual slide compositions. This technique involves using a series of LLM prompts to generate a sequence of outputs, each of which is used as input to the next prompt. By carefully designing the prompts and the orchestration logic, it is possible to generate complex and coherent outputs that would be difficult or impossible to produce using a single prompt.

The design logic and constraint solver used in this submodule is based on a combination of graph theory and linear programming. The solver takes the output from the Prompt Orchestrator and generates a structured JSON layout that satisfies a set of constraints, such as the size and position of each element, the color scheme, and the font styles. The solver uses a graph-based approach to represent the relationships between the different elements in the layout, and then uses linear programming to optimize the layout and satisfy the constraints.

## Installation
To install the LLM Prompt Chainer submodule, run the following command:
```bash
pip install llm-prompt-chainer
```

## Usage
The LLM Prompt Chainer submodule provides a simple API for generating strategic slide compositions. Here is an example of how to use the API:
```python
from llm_prompt_chainer import LLMChainer

# Create an instance of the LLMChainer class
chainer = LLMChainer()

# Define the input prompts
prompts = [
    "Generate a title slide with the title 'Introduction' and a background image of a cityscape.",
    "Generate a content slide with the title 'Problem Statement' and a bullet list of three items.",
    "Generate a conclusion slide with the title 'Conclusion' and a summary of the main points."]

# Generate the slide composition
composition = chainer.generate_composition(prompts)

# Print the composition
print(composition)
```

## API Reference
The LLM Prompt Chainer submodule provides the following API:
* `LLMChainer`: The main class for generating strategic slide compositions.
* `generate_composition`: A method that takes a list of prompts and generates a slide composition.
* `add_prompt`: A method that adds a prompt to the list of prompts.
* `get_composition`: A method that returns the generated slide composition.

## Case Studies
Here are two case studies that demonstrate the use of the LLM Prompt Chainer submodule in real-world scenarios:
* **Case Study 1**: A startup company uses the LLM Prompt Chainer submodule to generate a pitch deck for a potential investor. The submodule is able to generate a professional-looking deck with a consistent design theme and a clear narrative flow.
* **Case Study 2**: A marketing agency uses the LLM Prompt Chainer submodule to generate a series of social media posts for a client. The submodule is able to generate a set of posts that are tailored to the client's brand voice and visual identity.

## Testing
To run the test suite, use the following command:
```bash
pytest tests/
```

## Performance Considerations or Limitations
The LLM Prompt Chainer submodule has several performance considerations and limitations:
* **Computational Complexity**: The submodule uses a combination of graph theory and linear programming to generate the structured JSON layouts. This can be computationally intensive, especially for large and complex layouts.
* **Memory Usage**: The submodule requires a significant amount of memory to store the intermediate results and the final composition.

## Roadmap
Here are four potential future developments for the LLM Prompt Chainer submodule:
* **Integration with Other Tools**: Integrate the submodule with other tools and platforms, such as presentation software and content management systems.
* **Improved Performance**: Optimize the performance of the submodule, especially for large and complex layouts.
* **New Features**: Add new features to the submodule, such as support for multiple design themes and layouts.
* **User Interface**: Develop a user-friendly interface for the submodule, making it easier for users to input their prompts and generate slide compositions.

## License
The LLM Prompt Chainer submodule is licensed under the MIT License.

---
**Last updated:** 2026-07-16


## Requirements

```
pip install -r requirements.txt
```
