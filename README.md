# keyboard-path-finder

finds words that contain paths across neighboring keyboard keys.

the program searches through a word list and finds the longest sequence of letters where every letter is directly next to the previous one on a keyboard layout.

## features

* supports qwerty and qwertz keyboard layouts
* searches inside complete words
* finds the longest keyboard path in each word
* supports large word lists
* simple command line interface

## usage examples

### qwerty keyboard & english wordlist

```bash
python3 main.py english.txt --qwerty
```

### qwertz keyboard & german wordlist

```bash
python3 main.py german.txt --qwertz
```

## word lists

the program requires a text file containing one word per line.

two are included: german and english

large word lists work best because longer words have more possible paths.

## rules

a valid path must:

* move only between neighboring keys
* use horizontal, vertical, and diagonal neighbors
* not reuse the same key inside one path
* contain at least 3 characters

