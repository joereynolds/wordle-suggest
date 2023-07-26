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


try:
    wordle_file = sys.argv[1]
except IndexError:
    sys.exit("Please specify a txt file containing your wordle board so far")

# print(parse_board(sys.argv[1]))

print(get_invalid_letters(parse_board(sys.argv[1])))
