from trie import Trie


class FuzzyTrie(Trie):
    """A prefix tree data structure which stores an alphabet as value in each node.
    
    Attributes:
        root: A pointer to the root of the Trie.

    Methods:
        insert: Insert a string into the Trie.
        find: Return True if the word is in the Trie else False.
        complete: Complete a word based on the input of the user and return the list of words ordered by their length.
        fizzy_search: 
    """

    def __init__(self) -> None:
        """Inherit the attributes and methods from the base Tri.e"""
        super().__init__()