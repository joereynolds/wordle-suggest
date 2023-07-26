import sys

"""
Gives you suggestions for the current state of a wordle board
Pass a file to it and it'll spit out suggestions

Notation is:
    ! = Correct letter, correct place
    ? = Correct letter, wrong place
    - = Invalid letter

i.e.

A! U- D- I! O-

would yield:
    actin
    again
    anvil
    attic
    await
"""


def parse_board(wordle_file):
    return [line.split() for line in open(wordle_file)]

def get_invalid_letters(parsed_board):
    invalid_letters = []
    for line in parsed_board:
        for letter in line:
            if '-' in letter:
                invalid_letters.append(letter[0])

    return invalid_letters

def get_correctly_positioned_letters(parsed_board):
    letters = {}
    for line in parsed_board:
        for i, letter in enumerate(line):
            if '!' in letter:
                letters[letter[0]] = i

    return letters

def get_incorrectly_positioned_correct_letters(parsed_board):
    letters = {}
    for line in parsed_board:
        for i, letter in enumerate(line):
            if '?' in letter:
                letters[letter[0]] = i

    return letters


def is_invalid_letter_in_word(invalid_letters, word):
    for invalid_letter in invalid_letters:
        if invalid_letter.lower() in word:
            return True

    return False

def is_correctly_positioned_letter_in_word(correctly_positioned_letters, word):
    letter_count = len(correctly_positioned_letters)

    count = 0
    for letter, index in correctly_positioned_letters.items():
        if word[index] == letter.lower():
            count += 1

        if count == letter_count:
            return True


    return False

def is_correct_letter_in_wrong_position(almost_correct_letters, word):
    for i in range(len(word)):
        for letter, index in almost_correct_letters.items():
            if word[i] == letter.lower() and i == index:
                return True

def suggest(parsed_board):
    board_word_limit = 5 + 1
    invalid_letters = get_invalid_letters(parsed_board)
    correct_letters = get_correctly_positioned_letters(parsed_board)
    almost_correct_letters = get_incorrectly_positioned_correct_letters(parsed_board)

    suggestions = []

    for word in open('popular.txt'):

        # Weed out anything not of valid length
        if len(word) != board_word_limit:
            continue

        # Weed out stuff which has invalid letters in it
        if is_invalid_letter_in_word(invalid_letters, word):
            continue

        # Weed out words if valid letters in the wrong place
        if is_correct_letter_in_wrong_position(almost_correct_letters, word):
            continue

        if is_correctly_positioned_letter_in_word(correct_letters, word):
            suggestions.append(word)


    return suggestions

try:
    wordle_file = sys.argv[1]
except IndexError:
    sys.exit("Please specify a txt file containing your wordle board so far")

suggestions = suggest(parse_board(sys.argv[1]))

print(suggestions)
print(str(len(suggestions)), 'suggestions')
