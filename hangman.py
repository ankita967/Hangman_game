
import random

# Word collection
WORDS = [
    "python", "computer", "keyboard", "developer",
    "programming", "internet", "science", "school",
    "software", "hardware", "database", "variable",
    "function", "algorithm", "technology", "notebook",
    "elephant", "butterfly", "mountain", "rainbow",
    "football", "cricket", "hospital", "universe",
    "education", "artificial", "intelligence",
    "network", "security", "learning", "terminal"
]

MAX_WRONG_GUESSES = 6

# Hangman drawing stages
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Score records
score = {
    "games": 0,
    "wins": 0,
    "losses": 0
}


# Display current score
def display_score():
    print("\n========== SCORE RECORD ==========")
    print("Total Games :", score["games"])
    print("Wins        :", score["wins"])
    print("Losses      :", score["losses"])
    print("==================================")


# Display word with blanks
def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


# Get a valid guess
def get_guess(guessed_letters):
    while True:
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")

        elif guess in guessed_letters:
            print("You already guessed this letter!")

        else:
            return guess


# Play one round
def play_game():

    # Computer selects a random word
    word = random.choice(WORDS)

    guessed_letters = []
    wrong_guesses = 0

    print("\n========== HANGMAN GAME ==========")
    print("Guess the hidden word!")
    print("You have 6 incorrect guesses.")
    print("==================================")

    while wrong_guesses < MAX_WRONG_GUESSES:

        # Display Hangman drawing
        print(HANGMAN_STAGES[wrong_guesses])

        # Display current word
        print("Word:", display_word(word, guessed_letters))

        # Display guessed letters
        if guessed_letters:
            print("Guessed Letters:",
                  " ".join(sorted(guessed_letters)))
        else:
            print("Guessed Letters: None")

        # Display remaining chances
        print("Wrong Guesses:", wrong_guesses)
        print("Remaining Chances:",
              MAX_WRONG_GUESSES - wrong_guesses)

        # Take player's guess
        guess = get_guess(guessed_letters)

        guessed_letters.append(guess)

        # Check whether the guess is correct
        if guess in word:
            print("\nCorrect guess!")

        else:
            wrong_guesses += 1
            print("\nWrong guess!")

        # Check winning condition
        if all(letter in guessed_letters for letter in word):

            print(HANGMAN_STAGES[wrong_guesses])
            print("Word:", display_word(word, guessed_letters))

            print("\nCONGRATULATIONS! YOU WON!")
            print("The word was:", word)

            score["wins"] += 1
            score["games"] += 1

            return

    # Losing condition
    print(HANGMAN_STAGES[MAX_WRONG_GUESSES])

    print("\nGAME OVER! YOU LOST!")
    print("The correct word was:", word)

    score["losses"] += 1
    score["games"] += 1


# Main program
def main():

    print("\n***********************************")
    print("       WELCOME TO HANGMAN")
    print("***********************************")

    while True:

        play_game()

        # Display updated score
        display_score()

        # Ask to play again
        replay = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if replay not in ["yes", "y"]:
            print("\nThank you for playing!")
            display_score()
            print("Goodbye!")
            break


# Start the game
if __name__ == "__main__":
    main()
