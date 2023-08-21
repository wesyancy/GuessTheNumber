from art import logo
import random

def game():
    number = random.randint(1, 100)

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    user_lives = 0

    if difficulty == 'easy':
        user_lives = 10
        print ("You have 10 guesses remaining")

    elif difficulty == 'hard':
        user_lives = 5
        print ("You have 5 guesses remaining")

    else:
        print("You have typed an invalid respons \n The game is over")

    while user_lives != 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You Win! The number was {number}")
            user_lives = 0
        elif guess > number:
            print("Too high \n Guess again")
            user_lives -= 1
            print(f"You have {user_lives} guesses remaining")
        elif guess < number:
            print("Too low \n Guess again")
            user_lives -= 1
            print(f"You have {user_lives} guesses remaining")

    if user_lives == 0:
        print("You lose, better luck next time.")

while input("Would you like to play a number game? Type 'y' or 'n': ") == 'y':
    game()