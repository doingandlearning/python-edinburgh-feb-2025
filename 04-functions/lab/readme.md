# Lab: Functions

## Refactoring the Number Guessing Game with Functions

In this lab, you will improve the structure of your number guessing game by **extracting functionality into reusable functions**. This will make your code cleaner, more readable, and easier to maintain.

## Requirements

Modify your existing number guessing game so that:
- Different responsibilities (e.g., getting input, checking the guess, displaying messages) are split into **separate functions**.
- The game logic remains clear and structured.
- The game still supports replay functionality and keeps a history of guesses.

## Suggested Functions

1. **`initialize_game()`**: Initializes game variables and returns a dictionary with initial values.
2. **`display_welcome_message()`**: Prints the welcome message at the start of the game.
3. **`get_guess(min, max)`**: Prompts the user for a guess, validates input, and returns an integer.
4. **`check_guess(guess, number_to_guess)`**: Compares the guess to the target number and returns feedback.
5. **`play_game()`**: Manages the game loop and orchestrates the game flow using the extracted functions.

## Sample Output
```
Welcome to the number guess game!
Please guess a number between 1 and 10: 5
Whoops! You were too low!
You've already guessed: [5]
Please guess again: 7
Whoops! You were too high!
You've already guessed: [5, 7]
Please guess again: 6
Well done! You guessed it!
You guessed it in 3 tries!
Your guess history: [(5, 'Whoops! You were too low!'), (7, 'Whoops! You were too high!'), (6, 'Well done! You guessed it!')]
Do you want to play again? (y/n): n
Game over!
```

## Extension Points

### 1. Cheat Mode
- Allow the user to enter `-1` to see the correct number (without affecting attempts).

### 2. Improved Guess History
- Store each guess along with its feedback using a **tuple**.
- Display the full history at the end of the game.

### 3. Statistics
- Track and display:
  - **Lowest guess**
  - **Highest guess**
  - **Average guess**

**Example Output:**
```
The lowest value entered: 5
The highest value entered: 10
Average value is: 7.75
```

---

This lab reinforces **functions, modular programming, and structured game logic** in Python.
