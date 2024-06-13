# Fuzzy-Trie

## Project Description
Prefix-tree data structure with an approximate string matching algorithm based on Shang and Merrettal's paper [1].

## Import Data Structures
The `py_trie` module contains the 2 implementations of the trie.

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

## References
[1] H. Shang and T. H. Merrettal, "Tries for approximate string matching," in IEEE Transactions on Knowledge and Data Engineering, vol. 8, no. 4, pp. 540-547, Aug. 1996, doi: 10.1109/69.536247.
