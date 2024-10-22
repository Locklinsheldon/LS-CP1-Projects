import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    attempts += 1 #The attempts counter was not incrementing for the guesses, so the guesses stayed at zero (Logic error).
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #Guess was not an integer, so it wasn't counted as a number (Runtime error).
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess: #This was an if statement, which could cause the code to do both at once (Logic error)
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
#The continue command caused the attempt variable to not properly increment, and maybe not allow the game to end (Logic error).
    print("Game Over. Thanks for playing!")
start_game()
