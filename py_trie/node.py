class TrieNode:
    """An individual trie node.
    
    Attributes:
        children (dict): A dictionary mapping the character to its TrieNode object.
        end_of_word (bool): A boolean value indicating whether the current character is the end of the word.
    """
    
    def __init__(self) -> None:
        """Consturct the children and end_of_word attributes."""
        self.children: dict = {}
        self.end_of_word: bool = False