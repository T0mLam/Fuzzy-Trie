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

    def fuzzy_search(
        target: str, 
        threshold: int,
        sort_by_distance: bool = False,
        num_return: int | None = None
    ) -> List[str]:
        """An approximate string matching method that return a list of word within a Levenshtein distance threshold.
        
        Args:
            target (str): The target word.
            threshold (int): The maximum Levenshtein distance difference.
            sort_by_distance (bool): Return the words in ascending order of LD difference. (Default=False)
            num_return (int): The maximum number of return words. (Default=None)

        Returns:
            List[str]:  A list of words that are within the Levenshtein distance threshold in the trie.

        Raises:
            TypeError: Invalid data type of input parameter 'word'.
            ValueError: Invalid data type and range of input parameters 'threshold' or 'num_return'.

        Notes:
            Additional time complexity is introduced if 'sort_by_distance' is set to True.
        """
        if not isinstance(target, str):
            raise TypeError("The input parameter 'target' must be a string.")
        
        if not isinstance(sort_by_distance, bool):
            raise TypeError("The input parameter 'sort_by_distance' must be a boolean.")
        
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("The input parameter 'threshold' must be a non-negative integer")
        
        if (not isinstance(num_return, None) and
            (not isinstance(num_return, int) or num_return < 1)):
            raise ValueError("The input parameter 'num_return' must be a positive integer")
        