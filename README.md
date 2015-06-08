# Prose-Tools

This is a small collection of Python-based tools generated to aid in dealing with prose documents.

All of them accept the ```-h``` flag to help understand what they can do.

e.g.
```
$ python common-words.py -h

>> usage: common-words.py [-h] [-i INPUT] [-o OUTPUT] [-wl WORD_LIST]
                       [-cl CHARACTER_LIST]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input file. Normally a prose document.
  -o OUTPUT, --output OUTPUT
                        The output file name, without file extension.
  -wl WORD_LIST, --word-list WORD_LIST
                        Define your own list of words to ignore. Seperate with
                        spaces.
  -cl CHARACTER_LIST, --character-list CHARACTER_LIST
                        Define your own list of formatting characters to
                        ignore. Seperate with spaces.
```

## Documentation

Some automated documentation (via [Docbuilder](http://github.com/shakna-israel/docbuilder)) is available in the [docs](docs) folder.
