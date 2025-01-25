import random

def number_guessing_game():
    
    num_to_guess = random.randint(1, 100)
    atte = 0

    while True:
        user_guess = input("Enter your guess (1-100): ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            atte += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            elif user_guess < num_to_guess:
                print("Too Low! Try again.")
            elif user_guess > num_to_guess:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
        else:
            print("Invalid input. Please enter a valid number.")


number_guessing_game()
