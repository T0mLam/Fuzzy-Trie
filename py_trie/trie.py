from __future__ import annotations
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
        delete: Delete a word in the Trie and return True if successful.
        complete: Complete a word based on the input of the user and
                  return the list of words ordered by their length.

    Static Methods:
        from_list: Create a Trie object from a python list.
        from_txt: Create a Trie object from a txt file.

    To instantiate:
        >>> trie = Trie()
    """
    
    def __init__(self) -> None:
        """Construct the root of the trie."""
        self._root: TrieNode = TrieNode()
        self._size: int = 0

    def __contains__(self, item: str) -> bool:
        """Enable the use of membership test operator 'in' for the class."""
        try:
            return self.find(item)
        except TypeError as exc:
            raise TypeError(
                "The 'in' operator only support non-empty string comparisons."
            ) from exc

    def __len__(self) -> int:
        """Enable the use of 'len' operator for retrieving the total number of words."""
        return self._size

    @property
    def root(self) -> TrieNode:
        """Declare 'root' as a read-only attribute."""
        return self._root
    
    @property
    def size(self) -> int:
        """Declare 'size' as a read-only attribute."""
        return self._size
    
    @staticmethod
    def from_list(words: List[str]) -> Trie:
        """Create a Trie object from a python list.
        
        Args:
            words (List[str]): A list of words to be inserted.
    
        Returns:
            Trie: A Trie object with inserted words from the list.

        Raises:
            TypeError: The input parameter 'words' is not a list of strings.
        
        To instantiate:
            >>> trie = Trie.from_list([...])
        """
        if not (
            isinstance(words, list) or 
            all([isinstance(w, str) for w in words])
        ):
            raise TypeError("The input parameter 'words' must be a list of strings.")

        trie = Trie()

        for w in words:
            trie.insert(w)

        return trie

    @staticmethod
    def from_txt(path: str) -> Trie:
        """Create a Trie object from a txt file.
        
        Args:
            path (str): The path of the txt file.
    
        Returns:
            Trie: A Trie object with inserted words from the file.

        Raises:
            TypeError: The input parameter 'path' is not a string.
            FileNotFoundError: The file with the input path does not exist.
        
        To instantiate:
            >>> trie = Trie.from_txt('...')
        """
        if not isinstance(path, str):
            raise TypeError("The input parameter 'path' must be a string.")
        
        words = []

        try:
            with open(path, 'r') as f:
                for line in f:
                    words.extend(line.strip().split())
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file with the path '{path}' is not found"
            ) from exc
        
        return Trie.from_list(words)

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
    
    def delete(self, word: str) -> bool:
        """Delete a word in the trie.

        Args:
            word (str): A word to be deleted in the trie.

        Returns:
            bool: Return true if the word is successfully deleted, false if not present.

        Raises:
            TypeError: Errors caused by non-string or empty input of 'word'.
        """
        if not isinstance(word, str) or not word:
            raise TypeError("The input parameter 'word' must be a non-empty string")
        
        # Return False if the word to be deleted is not present in the trie.
        if not self.find(word):
            return False

        def dfs(i: int, node: TrieNode) -> None:
            # Stop the recusion whether after reaching the last character.
            # Set the end of word attribute to be False
            # and return True to indicate the node is deletable if it is a leaf.
            if i == len(word) - 1:
                node.end_of_word = False
                return not node.children
            
            # The variable 'removable' indicates whether
            # the subtree of the node could be deleted. 
            removable = dfs(i + 1, node.children[word[i + 1]])

            # If the subtree is removable and the current node 
            # and only has 1 child, remove its child.
            if removable and len(node.children) == 1:
                del node.children[word[i + 1]]
            
            # Return current node to be deletable if it is the not 
            # the end of a word, has no children and has a removable subtree.
            return (
                not node.end_of_word and 
                not node.children and
                removable
            )

        # Start the dfs at the first character of the word
        node = self._root
        dfs(0, node.children[word[0]])

        # Decrement the number of words in the trie by 1
        self._size -= 1

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

        # Use backtracking to find all the combinations of words starting
        # at the last character of the input string
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
                # Remove the char from the cache once a combination have been added
                cache.pop()

        dfs(node)
        # Return the list sorted by the length of each word
        return sorted(res, key=len)