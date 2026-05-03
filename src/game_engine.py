import random

from src.difficulty import choose_difficulty
from src.hints import get_hint
from src.scoreboard import Scoreboard
from src.utils import get_valid_number, ask_play_again


class GameEngine:
    def __init__(self):
        self.scoreboard = Scoreboard()

    def start(self):
        print("================================")
        print("     Welcome to GuessIQ CLI      ")
        print("================================")

        while True:
            won = self.play_round()
            self.scoreboard.update_score(won)
            self.scoreboard.show_scoreboard()

            if not ask_play_again():
                print("\nThanks for playing GuessIQ CLI!")
                break

    def play_round(self):
        difficulty = choose_difficulty()

        low = difficulty["low"]
        high = difficulty["high"]
        max_attempts = difficulty["max_attempts"]
        level = difficulty["level"]

        secret_number = random.randint(low, high)
        attempts = 0
        guessed_numbers = []

        print(f"\nDifficulty: {level}")
        print(f"I have selected a number between {low} and {high}.")
        print(f"You have {max_attempts} attempts.\n")

        while attempts < max_attempts:
            guess = get_valid_number(
                f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "
            )

            if guess < low or guess > high:
                print(f"Please guess a number between {low} and {high}.")
                continue

            if guess in guessed_numbers:
                print("You already guessed this number. Try another number.")
                continue

            guessed_numbers.append(guess)
            attempts += 1

            if guess == secret_number:
                print("\nCongratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Attempts used: {attempts}")
                print(f"Your guesses: {guessed_numbers}")
                return True

            print(get_hint(secret_number, guess))
            print(f"Previous guesses: {guessed_numbers}\n")

        print("\nGame Over!")
        print(f"The correct number was: {secret_number}")
        print(f"Your guesses: {guessed_numbers}")
        return False