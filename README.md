# Usage

```
python3 main.py wordle.txt
```

Where `wordle.txt` is a file containing your current board. The following is the syntax for the board

`!` - Correct letter, correct place

`?` - Correct letter, wrong place

`-` - Invalid letter

For example:

```
A? U- D- I- O-
R? E! A! L- M-
```

Would yield

```
11 suggestions:
bears
fears
gears
hears
heart
sears
tears
teary
wears
weary
years
```

## Troubleshooting

### Word isn't showing up as a suggestion but it's definitely correct

In that case, the wordlist I'm using (popular.txt) does not contain that word. Raise a PR/Issue and I'll add it in.

## Extras

### Live refresh of your suggestions

Use `entr`. I.e.

```
ls your-wordle-board | entr python3 main.py your-wordle-board
```

### Column output

Pipe it to `column`

```
python3 main.py your-wordle-board | column
```

## Tests

Run in a venv
Do this to install pytest:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt 
```

And then you can

`pytest test.py`
