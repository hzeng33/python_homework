# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter.lower())
        word_display = ""
        for char in secret_word:
            if char.lower() in guesses:
                word_display += char
            else:
                word_display += "_"
                
        print("Current word: ", word_display)
        if "_" not in word_display:
            return True
        else:
            return False
    return hangman_closure

def play_hangman():
    print("Welcome to Hangman game!\n")
    secret_word = input("Enter the secret word: ")
    hangman = make_hangman(secret_word)
    guess_count = 0
    while True:
        letter_guess = input("Guess a letter: ")
        if len(letter_guess) != 1 or not letter_guess.isalpha():
            print("Please enter a single letter.")
            continue
        guess_count += 1
        if hangman(letter_guess):
            print(f"\n🎉 Congratulations! You guessed the word!")
            print(f"The word was: {secret_word.upper()}")
            print(f"It took you {guess_count} guesses.")
            break
        else:
            print("Keep guessing!\n")

play_hangman()
        
