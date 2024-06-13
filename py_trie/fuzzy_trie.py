from typing import List

from .trie import Trie


class FuzzyTrie(Trie):
    """A prefix tree data structure with approximate string matching function.
    
    Attributes:
        root: A pointer to the root of the Trie.

    Methods:
        insert: Insert a string into the Trie.
        find: Return True if the word is in the Trie else False.
        complete: Complete a word based on the input of the user and return the list of words ordered by their length.
        fizzy_search: Search a list of words within a Levenshtein distance to the target string in the trie.
    """
    
    def __init__(self) -> None:
        """Inherit the attributes and methods from the base Trie."""
        super().__init__()

    def fuzzy_search(target: str, threshold: int) -> List[str]:
        if not isinstance(target, str):
            raise TypeError("The input parameter 'target' must be a string.")
        pass