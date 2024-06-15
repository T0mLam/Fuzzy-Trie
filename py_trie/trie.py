from typing import List

from .node import TrieNode


class Trie:
    """A prefix tree data structure which stores an alphabet as value in each node.
    
    Attributes:
        root: A pointer to the root of the Trie.
        size: The total number of words in the Trie.

    Methods:
        insert: Insert a string into the Trie.
        find: Return True if the word is in the Trie else False.
        complete: Complete a word based on the input of the user and return the list of words ordered by their length.
    """
    
    def __init__(self) -> None:
        """Construct the root of the trie."""
        self._root: TrieNode = TrieNode()
        self._size: int = 0

    @property
    def root(self) -> TrieNode:
        return self._root
    
    @property
    def size(self) -> int:
        return self._size

    def insert(self, word: str) -> bool:
        """Insert the word into the trie.

        Args:
            word (str): A word to be inserted into the trie.

        Returns:
            bool: Return true if the word is successfully added to the trie.

        Raises:
            TypeError: Errors caused by non-string or empty input of 'word'.
        """
        if not isinstance(word, str) or not word:
            raise TypeError("The input parameter 'word' must be a non-empty string")

        # Create a pointer to the root
        node = self._root

        # Check if the character is a child of the root
        for char in word:
            # Create a new branch if the character is not found
            if char not in node.children:
                node.children[char] = TrieNode()
            # Traverse to the node storing the character 
            node = node.children[char]
            
        # Set the node storing the last character of the word to be the end_of_word
        node.end_of_word = True

        # Increment the number of words in the trie by 1
        self._size += 1

        return True

    def find(self, word: str) -> bool:
        """Search whether the word is stored in the trie.

        Args:
            word (str): A word to be searched for in the trie.
        
        Returns:
            bool: True if the word is found else false.

        Raises:
            TypeError: Errors caused by non-string or empty input of 'word'.
        """
        if not isinstance(word, str) or not word:
            raise TypeError("The input parameter 'word' must be a non-empty string")

        node = self._root
        # Check every character in the word
        for char in word:
            # Return false if any char is not found
            if char not in node.children:
                return False
            # Traverse to the next char
            node = node.children[char]
        
        # Return true if the last char is marked as the end of word
        return node.end_of_word

    def complete(self, word: str) -> List[str]:
        """Complete the given word by searching words in the trie with the same prefix.

        Args:
            word (str): A word to be completed.
        
        Returns:
            List[str]: A list of possible words in the trie.

        Raises:
            TypeError: Errors caused by non-string input of 'word'.
        """
        if not isinstance(word, str):
            raise TypeError("The input parameter 'word' must be a string")

        node = self._root
        res = []

        # Find the node storing the last character of the input string
        for char in word:
            # Return an empty list if the input string is not found
            if char not in node.children:
                return []
            node = node.children[char]

        # Use backtracking to find all the combinations of words starting at the last char of the input str
        cache = []
        def dfs(node: TrieNode) -> None:
            # Append the word to res if it is marked as the end of word
            if node.end_of_word and cache:
                res.append(word + ''.join(cache)) 

            for child in node.children:
                # Backtracking 
                # Use a cache variable to store the combinations of the word
                cache.append(child)
                # Continue recursion on each child of the subtree
                dfs(node.children[child])
                # Remove the char from the cache once a combination have been added to res
                cache.pop()

        dfs(node)
        # Return the list sorted by the length of each word
        return sorted(res, key=len)
    
    def __contains__(self, item: str) -> bool:
        """Enable the use of membership test operator 'in' for the class."""
        return self.find(item)

    def __len__(self) -> int:
        """Enable the use of 'len' operator for retrieving the total number of words in the trie."""
        return self._size