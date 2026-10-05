# Number Guessing Game

## Description

This project is a simple Number Guessing Game developed using Python.

The program generates a random number, and the user continues guessing until the correct number is found. After each incorrect guess, the program tells the user whether the guess is too high or too low.

## Objective

- Learn how to use loops and conditions.
- Learn random number generation.
- Understand user interaction and input handling.
- Implement an attempt counter.

## Tools Used

- Python
- `random` module

## Features

- Generates a random number using `random.randint()`.
- Allows the user to keep guessing until the correct number is found.
- Gives a "Too high" or "Too low" hint.
- Counts the number of attempts.
- Stops the game when the correct number is guessed.

## How the Game Works

1. The program generates a random number.
2. The user enters a guess.
3. The program compares the guess with the secret number.
4. If the guess is lower than the secret number, it displays **"Too low"**.
5. If the guess is higher than the secret number, it displays **"Too high"**.
6. The user continues guessing until the correct number is found.
7. The program displays the total number of attempts.

## Sample Gameplay Output

```text

Enter the guess number: 24
Yay! You guessed it correct!
Number of attempts: 3
```

## Concepts Learned

- `random.randint()`
- `while` loop
- `if-elif-else` conditions
- User input using `input()`
- Attempt counting
- `break` statement

##
