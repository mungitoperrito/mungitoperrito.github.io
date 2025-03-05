# Crossword Puzzle Generator

This project creates a crossword puzzle based on a theme that you supply.

The sample code creates a puzzle based on the Harry Potter stories. If you want
to use a different subject, just change the training data to match your theme.

The first notebook shows you how to create a collection that you can use to
generate the clue-answer pairs. The collection gives the LLM additional
information that improves the [generative
AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) steps.

The second notebook generates the puzzle.

## Prepare the LLM

The [`crossword-setup.ipynb`](crossword-setup.ipynb) notebook uses the Simple
English Wikipedia data set from Cohere. It does the following:

- Connects you to an LLM hosted by Cohere
- Sets up a collection

## Generate the Puzzle

The [`crossword-create-puzzle.ipynb`](crossword-create-puzzle.ipynb) notebook
does these things:

- Creates a list of puzzle answers
- Creates clues for each answer
- Uses the clue-answer pairs to generate a puzzle

## Requirements

This project uses [Cohere](https://cohere.com/) for the data set and LLM. You
need a Cohere API key to run the code in `crossword-create-puzzle.ipynb`.

## Credits

The code that generates the puzzle grid is a lightly modified version of the
[crossword_helmig](https://github.com/jeremy886/crossword_helmig) project.

