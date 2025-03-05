# Crossword Puzzle Generator

This project creates a crossword puzzle based on a theme that you supply.

The sample code creates a puzzle based on the Sherlock Holmes stories. If you
want to use a different subject, just change the training data to match your
theme.

The first notebook shows you how to import data and create a collection that
you can use to generate the clue-answer pairs. The collection gives the LLM
additional information that improves the [generative
AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) steps.

The second notebook generates the puzzle.

## Prepare the LLM

The [`crossword-setup.ipynb`](crossword-setup.ipynb) notebook does these things:

- Connects you to a locally hosted LLM
- Gathers prerequisites
- Sets up a collection
- Imports data

## Generate the Puzzle

The [`crossword-create-puzzle.ipynb`](crossword-create-puzzle.ipynb) notebook
does these things:

- Creates a list of puzzle answers
- Creates clues for each answer
- Uses the clue-answer pairs to generate a puzzle

## Requirements

This project requires a local installation of Ollama. If haven't already
installed Ollama, follow the instructions on the [Ollama
website](https://ollama.com/) to download and install it.

There are sample data files from [Project Gutenberg](https://www.gutenberg.org/)
in the [inputs](inputs) folder. If you want to change the data in the collection, you
need to change the input files.

## Credits

The code that generates the puzzle grid is a lightly modified version of the
[crossword_helmig](https://github.com/jeremy886/crossword_helmig) project.

The sample data is from [Project Gutenberg](https://www.gutenberg.org/).
