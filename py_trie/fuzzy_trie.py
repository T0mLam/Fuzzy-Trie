from typing import List

from .node import TrieNode
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
        self,
        target: str, 
        threshold: int,
        num_return: int | None = None,
        sort_by_distance: bool = False
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
        
        if (not isinstance(num_return, type(None)) and
            (not isinstance(num_return, int) or num_return < 1)):
            raise ValueError("The input parameter 'num_return' must be a positive integer")
        
        cols = len(target) + 1
        res = []
        
        def dfs(
            node: TrieNode, 
            curr_str: str,
            prev_row: List[int]
        ) -> None:
            # Get the latest added character from the string
            letter = curr_str[-1]

            # Get the new row using the edit distance algorithm
            curr_row = edit_dist(letter, prev_row)

            # If the last value of the row is less than the threshold
            # and it is a word stored in the trie, push the word to the result.
            if curr_row[-1] <= threshold and node.end_of_word:
                word = (curr_str, curr_row[-1]) if sort_by_distance else curr_str
                res.append(word)
            
            # Stop the recursion once the number of element in result 
            # meet the num_return parameter 
            if (isinstance(num_return, int) and
                len(res) == num_return):
                return 

            # If the minimum value of the row has not exceeded the threshold, 
            # it is possible that adding additional characters 
            # to the end of the word will still be valid
            if min(curr_row) <= threshold:
                for child in node.children:
                    dfs(node.children[child], curr_str + child, curr_row)

        def edit_dist(
            letter: str,
            prev_row: List[int]
        ) -> int:
            # Create the first value of the new row
            curr_row = [prev_row[0] + 1]

            for col in range(1, cols):
                # Add the value of the top left grid to curr_row 
                # if the combination and target share the same letter 
                if target[col - 1] == letter:
                    curr_row.append(prev_row[col - 1])
                    continue

                # Otherwise calculate each cost of the 3 grids at the 3 directions
                # according to the edit distance algorithm
                replace_cost = prev_row[col - 1] + 1
                insert_cost = curr_row[col - 1] + 1
                delete_cost = prev_row[col] + 1

                # Append the minimum cost to the curr_row
                curr_row.append(min(replace_cost, insert_cost, delete_cost))

            return curr_row
    
        node = self.root
        # Create the first row of the 2d matrix
        first_row = range(len(target) + 1)

        # Start the recursion from every child of the trie root
        for child in node.children:
            dfs(node.children[child], child, first_row)

        # Sort the words by their Levenshtein distances
        # if sort_by_distance is set to True
        if sort_by_distance:
            res = [tup[0] for tup in sorted(res, key=lambda x: x[1])]

        return res