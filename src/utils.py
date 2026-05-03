def get_valid_number(prompt):
    while True:
        try:
            number=int(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def ask_play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice in ["yes", "y"]:
        return True

    return False
