# Fuzzy-Trie

## Project Description
Prefix-tree data structure with an approximate string matching algorithm modified from Shang and Merrettal's implementation [1].

## What is a Trie (Prefix-Tree)?
A trie is a tree data structure with each node storing a character of the key. A complete key is formed by a path from the root to the node marked with the end of word. Keys with the same prefixes share the same node in the trie. This compressed nature of the key representation enables <b>more efficient key lookups and prefix matching</b> than other primitive data structures, e.g. arrays or python lists, and <b>time complexity independent to the number of keys</b> in the trie..

Time complexity:
[]()            |   Trie     |  Array
--------------- | :--------: | :-------------:
Insertion / Deletion       |   $O(l)$   |   $O(1)$    
Searching       |   $O(k)$   |   $O(n)$  
Prefix Matching |   $O(l)$   |   $O(l * n)$  
Word Completion | $O(l + a\^{k - l})$* |   $O(l * n)$   
Fuzzy Search    |       $O(m * a\^{m})$*     |   $O(k * m * n)$  

$a =$ Number of characters in each level <br/>
$m =$ Number of mismatches in the key <br/>
$n =$ Number of elements in the array <br/>
$k =$ Length of the longest key in the trie <br/>
$l =$ Length of the input key <br/>

\* Runtime heavily depends on the number of characters in each level

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
