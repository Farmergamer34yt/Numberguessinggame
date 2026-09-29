# Number Guessing Game

A simple Python number-guessing game I made while learning Python.

The program randomly chooses a number between **1 and 100**, and the player keeps guessing until they get the correct number. After each incorrect guess, the program tells the player whether their guess was too high or too low.

## How It Works

1. The program generates a random number from 1–100.
2. You enter your guess.
3. The program tells you:

   * **"Its lower"** if your guess is too high.
   * **"Its higher"** if your guess is too low.
4. You keep guessing until you get the number.
5. The program tells you how many guesses you made.

## Requirements

* Python 3
* No external libraries are required.

## How to Run

Run the Python file from a terminal:

```bash
python classwrkagn.py
```

Then follow the prompts.

## Example

```text
what is the number im thinking of 1-100 50
Its lower
what is the number im thinking of 75
Its higher
what is the number im thinking of 63
Correct
Your guessed 3 times
```

## Notes

This is a beginner Python project. It's nothing fancy, but it works and was made to practice:

* `random`
* Variables
* User input
* `if` / `elif`
* `while` loops
* Counting attempts

There are definitely things that could be improved, but this is where the project is at right now.
