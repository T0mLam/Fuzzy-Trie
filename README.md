# Fuzzy-Trie (unfinished)

## Project Description
Prefix-tree data structure with an approximate string matching algorithm modified from Shang and Merrettal's implementation [1].

## What is a Trie (Prefix-Tree)?

## Import Data Structures
The `py_trie/` module contains the 2 implementations of the trie.

To import and use the data structure independently, add the following code in your program:
```python
from py_trie.{module} import {data structure}
```
Replace `{module}` with the name of the module, `{data structure}` with the name of the class, <br>
e.g.
```python
# Import the fuzzy trie data structure
from py_trie.fuzzy_trie import FuzzyTrie
```

## Run Unit Tests
The `tests/` folder contains unit tests for the modules in `py_trie/`.

To run the tests, execute the following command from the project's root directory:
```bash
python -m unittest tests.{test module}
```
Replace `{test module}` with the name of the test module, e.g. `test_trie` to run the tests.

## Get Help
Use the python `help` function to print the docstrings and type hints for the trie classes, <br>
e.g. 
```python
# Import the trie data structure
from py_trie.trie import Trie

# Call the built-in 'help' function in Python
help(Trie)
```
Output:
```
Help on class Trie in module py_trie.trie:

class Trie(builtins.object)
 |  Trie() -> None
 |  
 |  A prefix tree data structure which stores an alphabet as value in each node.
 |  
 |  Attributes:
 |      ...
 |  
 |  Methods:
 |      ...
 |  
 |  __init__(self) -> None
 |      ...
 |  
 |  complete(self, word: str) -> List[str]
 |      ...
 |      
 |  ... 
```

## References
[1] H. Shang and T. H. Merrettal, "Tries for approximate string matching," in IEEE Transactions on Knowledge and Data Engineering, vol. 8, no. 4, pp. 540-547, Aug. 1996, doi: 10.1109/69.536247.
