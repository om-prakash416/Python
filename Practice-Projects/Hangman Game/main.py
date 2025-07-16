import random

def hangman_game():
    word_list = ["python", "developer","hangman","programming","challange","omprakash","bhola"]
    word_to_guess = random.choice(word_list).lower()
    
    guessed_word = ["_"] * len(word_to_guess)
    
    attempts_left = 5
    
    guessed_letters = []
    
    print("Welcome to Hangman")
    print(f"The word has {len(word_to_guess)} letters.")
    print(" ".join(word_to_guess))
    
    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'No letters guessed yet.'}")
        print("word to guess: " + " ".join(guessed_word))
        
        guess = input("Enter a letter: ").lower()
        
        if not guess.isalpha() or guess.isdigit() != 1:
            print("Plese enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.append(guess)
        
        
        if guess in word_to_guess:
            print(f"Good Guess! '{guess}' is in the word.")
            
            for index,letter in enumerate(word_to_guess):
                if letter == guess:
                    
                     guessed_word[index] = guess
               
        else:
            print(f"Wrong guess. '{guess}' is not in the word.")
            attempts_left -= 1
        
        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:")
            print(" ".join(guessed_word))
            break    
        
    
    if attempts_left == 0:
        print("\nGame over! You've run out of attempts.")
        print(f"The word was: {word_to_guess}")

hangman_game()