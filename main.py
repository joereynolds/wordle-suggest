import wordle
import sys


if __name__ == '__main__':
    try:
        wordle_file = sys.argv[1]
    except IndexError:
        sys.exit("Please pass a file containing your wordle board so far")

    suggestions = wordle.suggest(
        wordle.parse_board(wordle_file),
        open('popular.txt', 'r')
    )

    wordle.print_suggestions(suggestions)
