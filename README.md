# Collin
Collin is a template/skeleton for creating interactive/stateful command-line applications.

### Why Collin?

`clint` was already taken

### Why not Click or Argh?

AFAIK, the regular CLI-building libraries do not provide interactive/stateful options,
without implementing some type of extra storage-mechanism

### Interactive/Stateful

Collin can hold data within the programming data-structures (variables, etc.) for the duration of the
program. You no longer need a database or other storage-mechanism

### Extendable/Skeleton/Template/Your-lang

Collin is very much a template/skeleton. The code is relatively simple for all types of programmers
(novice included) and can be extended to just about any other language that has some command-line
support

### Support

Collin currently supports:

 - Python3
 - Python2 (with a few adjustments to the Python3 code)
 - [add your language to this document]
 
### Usage

1. Save `menu.py` and `functions.py` in any folder
2. Open folder in the CLI of your choosing
3. Run:
```
python menu.py
```

### Contributing

#### General:

1. Fork the repo
2. Make your changes/additions
3. Open a Pull Request

#### Adding another language

1. Create a folder specifying your desired language eg. `Ruby`, `Haskell`
2. Use the basic structure of `menu.[lang]` and `functions.[lang]` within
newly created folder
3. If your language has multiple versions eg. `Python2` and `Python3` then
specify the version in the folder-name

### Licensing

This project is licensed under the `Unlicense`, as it is just a template. You can therefore
re-license any projects that use Collin under their own licenses (MIT/Apache/BSD/GPL3/etc.)
