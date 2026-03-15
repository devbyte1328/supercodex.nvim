import random


def print_intro():
    print("===================================")
    print("     WELCOME TO GUESS THE NUMBER   ")
    print("===================================")
    print("I'm thinking of a number.")
    print("You have to guess it!")
    print()


def choose_difficulty():
    print("Select difficulty (Easy, Medium, Hard):")
    print("1 - Easy (1 to 10)")
    print("2 - Medium (1 to 50)")
    print("3 - Hard (1 to 100)")
    print()

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return 10
    elif choice == "2":
        return 50
    elif choice == "3":
        return 100
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 10


def generate_secret_number(max_number):
    return random.randint(1, max_number)


def get_player_guess():
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        return None

    return int(guess)


def check_guess(secret_number, guess):
    if guess < secret_number:
        print("Too low!")
        return False
    elif guess > secret_number:
        print("Too high!")
        return False
    else:
        print("Correct! You guessed it!")
        return True


def play_game():
    print_intro()

    max_number = choose_difficulty()
    secret_number = generate_secret_number(max_number)

    attempts = 0
    guessed_correctly = False

    print()
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print()

    while not guessed_correctly:
        guess = get_player_guess()

        if guess is None:
            continue

        attempts += 1
        guessed_correctly = check_guess(secret_number, guess)
        print()

    print(f"You won in {attempts} attempts!")
    print("Game Over.")


def main():
    play_game()


main()
