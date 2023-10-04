from random import choice
import string


WORDLIST_FILENAME = "words.txt"


def display_hangman(tries):
    """
    Display the hangman's current state based on the number of tries.

    Args:
    tries (int): The number of incorrect guesses made by the player.

    Returns:
    None
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[tries]) 


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings 
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    Args:
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    Check if all the letters in the secret word have been guessed.

    Args:
    secret_word (str): The word the user is trying to guess.
    letters_guessed (list): List of letters that have been guessed.

    Returns:
    bool: True if all the letters of the secret word are in letters_guessed, False otherwise.
    '''
    guessed = True
    for letter in secret_word:
      if letter not in letters_guessed:
        guessed = False
        break   
    return guessed
            

def get_guessed_word(secret_word, letters_guessed):
    '''
    Create a string representing the guessed and unguessed letters in the secret word.

    Args:
    secret_word (str): The word the user is trying to guess.
    letters_guessed (list): List of letters that have been guessed.

    Returns:
    str: A string with letters, underscores (_), and spaces representing which letters in secret_word have been guessed.
    '''
    guessed_word = ''
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word += letter
      else:
        guessed_word += '_ '
    return guessed_word            

  
def get_available_letters(letters_guessed):
    '''
    Get a string of available letters that have not been guessed yet.

    Args:
    letters_guessed (list): List of letters that have been guessed.

    Returns:
    str: A string comprised of letters that represents which letters have not yet been guessed.
    '''
    available_letters = set(string.ascii_lowercase) - set(letters_guessed)
    return ''.join(sorted(available_letters))


def print_game_status(game_state):
    print(f"You have {game_state['num_of_guesses']} guesses left. ")
    print(f"Available letters: {get_available_letters(game_state['letters_guessed'])}")


def get_valid_input(game_state):
    '''
    Get a valid letter input from the player.

    Args:
    game_state (dict): The current state of the game.

    Returns:
    str: The valid letter input from the player.
    '''
    while True:
        if game_state['num_of_guesses'] == 0:
            break
        letter = input("Please guess a letter: ").lower()
        if letter == '*':
            return letter
        elif not letter.isalpha() or len(letter) != 1:
            game_state['warnings'] -= 1
            print(f"Oops! That is not a valid letter. You have {game_state['warnings']} warning left:")
            check_warnings(game_state)
        elif letter in game_state['letters_guessed']:
            game_state['warnings'] -= 1
            print(f"Oops! You've already guessed that letter. You have {game_state['warnings']} warning left:")
            check_warnings(game_state)
        else:
            return letter
        

def check_warnings(game_state):
    '''
    Check the remaining warnings and decrement them if needed.

    Args:
    game_state (dict): The current state of the game.

    Returns:
    dict: The updated game state with decremented warnings.
    '''
    if game_state['warnings'] == 0:
        print("You ran out of warnings. You lose one guess!")
        game_state['num_of_guesses'] -= 1
        print(f"Total number of guesses left: {game_state['num_of_guesses']}")
        display_hangman(game_state['num_of_guesses'])
        game_state['warnings'] = 3
    return game_state       

        
def check_guess(letter, secret_word, game_state):
    '''
    Check if the guessed letter is in the secret word and update the game state accordingly.

    Args:
    letter (str): The letter guessed by the player.
    secret_word (str): The word the user is trying to guess.
    game_state (dict): The current state of the game.

    Returns:
    None
    '''
    if letter in secret_word:
        game_state['letters_guessed'].append(letter)
        print(f"Good guess: {get_guessed_word(secret_word, game_state['letters_guessed'])}")
        display_hangman(game_state['num_of_guesses'])
    elif letter in 'aeiou':
        game_state['num_of_guesses'] -= 2
        game_state['letters_guessed'].append(letter)
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, game_state['letters_guessed'])}")
        display_hangman(game_state['num_of_guesses'])
    else:
        game_state['num_of_guesses'] -= 1
        game_state['letters_guessed'].append(letter)
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, game_state['letters_guessed'])}")
        display_hangman(game_state['num_of_guesses'])


def calculate_score(game_state):
    '''
    Calculate the player's score based on the number of guesses and unique letters guessed.

    Args:
    game_state (dict): The current state of the game.

    Returns:
    int: The player's score.
    '''
    return game_state['num_of_guesses'] * len(set(game_state['letters_guessed']))


def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'. ")


def initialize_game_state():
    '''
    Initialize the game state with default values.

    Returns:
    dict: The initial game state.
    '''
    return {'num_of_guesses': 6, 'letters_guessed': [], 'warnings': 3}

       
def match_with_gaps(my_word, other_word):
    '''
    Check if my_word matches other_word when considering gaps (underscores).

    Args:
    my_word (str): A string with _ characters, the current guess of the secret word.
    other_word (str): A regular English word.

    Returns:
    bool: True if all the actual letters of my_word match the corresponding letters of other_word,
          or the letter is the special symbol _, and my_word and other_word are of the same length; False otherwise.
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False

    for i in range(len(my_word)):
        if my_word[i] == '_':
            continue
        elif my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    '''
    Show possible matches in the wordlist for the given my_word.

    Args:
    my_word (str): A string with _ characters, the current guess of the secret word.

    Returns:
    None
    '''
    matching_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matching_words.append(word)
    if matching_words:
        print("Possible word matches:")
        print(", ".join(matching_words))
    else:
        print("No matches found.")


def hangman_with_hints(secret_word):
    '''
    Play the Hangman game with hints.

    Args:
    secret_word (str): The secret word to guess.

    Returns:
    None
    '''
    game_state = initialize_game_state()

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long. ")

    while game_state['num_of_guesses'] > 0:
        print("---------------------------")
        print_game_status(game_state)

        letter = get_valid_input(game_state)
        if game_state['num_of_guesses'] == 0:
            break
        if letter == '*':
            show_possible_matches(get_guessed_word(secret_word, game_state['letters_guessed']))
        else:
            check_guess(letter, secret_word, game_state)


        if is_word_guessed(secret_word, game_state['letters_guessed']):
            print("Congratulations! You won!")
            total_score = calculate_score(game_state)
            print(f"Your total score for this game is: {total_score}")
            if play_again():
                secret_word = choose_word(wordlist)
                game_state = initialize_game_state()
            else:
                print("Goodbye!")
                break

    if game_state['num_of_guesses'] <= 0:
        print(f"Sorry, you ran out of guesses, The word was {secret_word}.")
        if play_again():
            secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)
        else:
            print("Goodbye!")


if __name__ == "__main__":
    # Game initialization and execution
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
