import pytest

import wordle

@pytest.mark.parametrize("words, board, expected", [
    (
        # It filters out words that aren't the correct length
        ['smileeeeee', 'smile', 'smil'],
        [['S!', 'M!', 'I!', 'L!', 'E!']],
        ['smile']
    ),
    (
        #'words with an invalid letter are never present in a suggestion'
        ['taath', 'tooth', 'teeth'],
        [['E-']],
        ['taath', 'tooth']
    ),
    (
        # If a letter starts correct but in the wrong position,
        # then it shouldn't suggest words starting with that letter
        ['heart', 'meart', 'cehrt'],
        [['H?', 'X-', 'X-', 'X-', 'X-']],
        ['cehrt']
    ),
    (
        # It brings back results containing a definite match on a letter
        ['cease', 'beard', 'tools', 'screw', 'lemon'],
        [
            ['X', 'E!', 'X', 'X', 'X'],
            ['X', 'X', 'A!', 'X', 'X'],
        ],
        ['cease', 'beard']
    ),
    (
        # If an element has an "almost" correct letter. It only brings back
        # words with that letter somewhere in the word
        ['ebony', 'eigth', 'ethic', 'ethos', 'evils', 'excel'],
        [
            ['E!', 'T!', 'H!', 'X', 'X']
        ],
        ['ethic', 'ethos']
    ),
    (
        # Test we don't class a letter as invalid if it's valid
        # somewhere else on the board
        ['vigil'],
        [
            ['V!', 'I!', 'G!', 'I-', 'L!']
        ],
        ['vigil']
    )
])
def test_suggestions(words, board, expected):
    actual = wordle.suggest(board, words)
    assert actual == expected
