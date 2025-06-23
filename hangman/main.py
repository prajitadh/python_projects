import random
import task.hangman.hangman_words as hangman_words
import task.hangman.hangman_art as hangman_art
from task.hangman.hangman_words import word_list
print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for dash in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
lives = 6
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters.append(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is: {chosen_word}")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        print(f"The correct word is: {chosen_word}")

    print(hangman_art.stages[lives])
