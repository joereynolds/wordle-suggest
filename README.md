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
actin
again
anvil
attic
await
```
