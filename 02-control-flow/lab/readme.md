# Lab: Flow of Control and Iteration

## Overview
In this lab, you will create a simple number guessing game program, handling user input, using the `if` statement as well as looping constructs.

## Game Logic
The basic flow of the game is as follows:

- The program randomly selects a number between 1 and 10.
- It asks the player to enter their guess.
- If the guess matches the randomly generated number, the player wins.
- If the guess is incorrect:
  - The program informs the player whether their guess is too high or too low.
  - The player has **four attempts** to guess correctly.
- If the player does not guess the correct number within four attempts, they lose and are shown the correct number.

## Sample Output
```plaintext
Welcome to the number guess game
Please guess a number between 1 and 10: 5
Sorry, wrong number
Your guess was higher than the number
Please guess again: 3
Sorry, wrong number
Your guess was lower than the number
Please guess again: 4
Well done, you won!
You took 3 attempts to complete the game
Game Over
```

## Hints

### Initialising Variables
In Python, variables do not need to be declared before assignment, but they must have an initial value before being referenced. Example:

```python
count = count + 1  # This will cause an error if 'count' is not initialized first
```

Error message example:
```
NameError: name 'count_number_of_tries' is not defined
```

A correct approach:
```python
count = 0  # Initialize before usage
count += 1  # Equivalent to count = count + 1
```

### Generating a Random Number
You need to use Python's `random` module:

```python
import random
number_to_guess = random.randint(1, 10)
```

This generates a random integer between **1 and 10** (inclusive), which the player must guess.

### Obtaining User Input
To get the player's guess:

```python
guess = int(input('Please guess a number between 1 and 10: '))
```

This converts the input (which is a string) into an integer.

## Extension Points
If you have extra time, try implementing these additional features:

- **Cheat Mode**: If the user enters `-1`, reveal the correct number and allow another guess (without counting it as an attempt).
- **Near-Miss Hint**: If the player's guess is within **1** of the correct number, inform them.
- **Play Again Option**: At the end of the game, ask the user if they want to play again. If they say **yes**, restart the game.

---

This lab will help you practice control flow, conditionals, loops, and user input handling in Python.

