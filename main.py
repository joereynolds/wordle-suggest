import sys


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

def suggest(parsed_board):
    board_word_limit = 5 + 1
    invalid_letters = get_invalid_letters(parsed_board)
    correct_letters = get_correctly_positioned_letters(parsed_board)

    suggestions = []

    for word in open('popular.txt'):

        if len(word) != board_word_limit:
            continue

        if is_invalid_letter_in_word(invalid_letters, word):
            continue

        if is_correctly_positioned_letter_in_word(correct_letters, word):
            suggestions.append(word)


    return suggestions



try:
    wordle_file = sys.argv[1]
except IndexError:
    sys.exit("Please specify a txt file containing your wordle board so far")

# print(parse_board(sys.argv[1]))
# print(get_invalid_letters(parse_board(sys.argv[1])))

suggestions = suggest(parse_board(sys.argv[1]))

print(suggestions)
print(str(len(suggestions)), 'suggestions')
