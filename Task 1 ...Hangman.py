#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

HANGMAN_STAGES = [
    # 0 incorrect guesses
    """
   -----
   |   |
       |
       |
       |
       |
==========""",
    # 1
    """
   -----
   |   |
   O   |
       |
       |
       |
==========""",
    # 2
    """
   -----
   |   |
   O   |
   |   |
       |
       |
==========""",
    # 3
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
==========""",
    # 4
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
==========""",
    # 5
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
==========""",
    # 6 — dead
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
==========""",
]

WORD_LIST = ["python", "hangman", "keyboard", "monitor", "algorithm","jewellery"]

MAX_WRONG = 6


def display_state(wrong_guesses: list, guessed_letters: set, secret: str) -> None:
    """Print the current hangman figure, word progress, and hint info."""
    print(HANGMAN_STAGES[len(wrong_guesses)])
    # Show blanks / correctly guessed letters
    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in secret
    )
    print(f"\n  Word : {display_word}")
    print(f"  Wrong guesses ({len(wrong_guesses)}/{MAX_WRONG}) : {', '.join(wrong_guesses) or '-'}")
    remaining = MAX_WRONG - len(wrong_guesses)
    print(f"  Lives remaining : {remaining}\n")


def play_hangman() -> None:
    secret = random.choice(WORD_LIST)
    guessed_letters: set = set()
    wrong_guesses: list = []

    print("\n" + "=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  The word has {len(secret)} letters. Good luck!\n")

    while len(wrong_guesses) < MAX_WRONG:
        display_state(wrong_guesses, guessed_letters, secret)

        if all(letter in guessed_letters for letter in secret):
            print(f"  🎉  You won! The word was '{secret.upper()}'.")
            return

        while True:
            guess = input("  Enter a letter: ").strip().lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("    Please enter a single alphabetic character.")

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"    You already tried '{guess}'. Pick another.")
            continue

        guessed_letters.add(guess)

        if guess in secret:
            print(f"  ✅  '{guess}' is in the word!")
        else:
            wrong_guesses.append(guess)
            print(f"  ❌  '{guess}' is NOT in the word.")

    display_state(wrong_guesses, guessed_letters, secret)
    print(f"  💀  Game over! The word was '{secret.upper()}'.\n")


def main() -> None:
    while True:
        play_hangman()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()


# In[ ]:




