# Jupyter Notebooks

These projects use Jupyter notebooks to combine explanatory text and code.

## Crossword Puzzle Generators

There are two versions of this project. Both of them start with a theme and use
that theme to create a crossword puzzle. The questions, clues, and puzzle grid
are all created by the scripts.

Other than a change of topic, the difference between the projects is in the
[generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence)
steps. One version uses a locally hosted LLM, [Ollama](https://ollama.com/). The
other version uses the [Cohere](https://cohere.com/) online API.

- [Local, Ollama version](xword_ollama/crossword_ollama.md)
- [Online, Cohere API version](xword_online/crossword_online.md)

## Tutorial Walkthrough

This project is a guided walkthrough of the Weaviate Multi-tenancy tutorial. It
expands on the tutorial to provide background and examples that are missing from
the original.

- [Weaviate multi-tenancy walkthrough](multi_tenant_walkthrough.ipynb)