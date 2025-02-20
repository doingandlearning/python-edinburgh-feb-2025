# Lab: Containers

## Enhancing the Number Guessing Game

Modify your number guessing game to maintain a **history of guesses** made by the user. 
Once the game is over, print out the guesses in the order they were made. This will allow the user to review their gameplay.

### Requirements:
- Use a **list** to store the guess history.
- Maintain the order of guesses.
- Allow duplicates (since a user may enter the same guess more than once).

### Sample Output:
```
Welcome to the number guess game
Please guess a number between 1 and 10: 5
Sorry, wrong number
Your guess was lower than the number
Please guess again: 7
Sorry, wrong number
Your guess was lower than the number
Please guess again: 9
Sorry, wrong number
Your guess was lower than the number
Please guess again: 10
Well done, you won!
You took 4 tries to complete the game
Your guesses were:
[5, 7, 9, 10]
Game Over
```

## Extension Points

### 1. Storing Guess Results
Modify the program to store **both** the guess and the result (whether it was higher or lower than the target). A **tuple** could be useful for this.

**Example Output:**
```
Your guesses were:
[(5, 'Too low'), (7, 'Too low'), (9, 'Too low'), (10, 'Correct guess')]
```

### 2. Replay Option
Modify the game to **ask the user if they want to play again**. If they agree:
- Generate a new random number.
- Clear the guess history.

### 3. Analyzing Guesses
Enhance the game by computing additional statistics:
- **Lowest guess:** The smallest number entered.
- **Highest guess:** The largest number entered.
- **Average guess:** The mean value of all guesses.

**Example Output:**
```
The lowest value entered: 5
The highest value entered: 10
Average value is: 7.75
```

---

This lab helps reinforce **list operations, tuples, and data analysis** in Python.
