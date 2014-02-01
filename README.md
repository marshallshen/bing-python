# BingPython
----------------------
A light-weight relevance feedback application using Bing search API

## Usage
----------------------
Run via Shell script:

- Assuming "precision @ 10", the program always return top 10 results per search.
- You can pass you own [account key](http://datamarket.azure.com/dataset/bing/search). If you don't pass one, the application runs using a default account key.

The runner format:
$ <project-dir>/bin/run.sh <query> <precision> <optional account key>

## Example
search with default account key: [snow leopard], [gates], [columbia]
```shell
bin/run.sh DEFAULT_KEY 0.8 "gates"
bin/run.sh DEFAULT_KEY 0.8 "snow leopard"
bin/run.sh DEFAULT_KEY 0.8 "columbia"
```

Run via Python:
```shell
$ python bing/relevance.py
```

## Install
---------------------
To install dependent packages:

$ python setup.py install


## Development
-----------------------
To run the test suite:
$ nosetests
