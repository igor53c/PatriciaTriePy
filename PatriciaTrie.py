from TrieNode import TrieNode


class PatriciaTrie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Delete a word from the trie
    def delete(self, word):
        def _delete(node, current_word, depth):
            if depth == len(current_word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = current_word[depth]
            if char not in node.children:
                return False
            should_delete_child = _delete(node.children[char], current_word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            return False

        _delete(self.root, word, 0)
