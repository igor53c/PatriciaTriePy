from PatriciaTrie import PatriciaTrie


def test_insert_and_search():
    trie = PatriciaTrie()

    words_to_insert = ["hello", "world", "hi", "her", "hero", "heron"]
    for word in words_to_insert:
        trie.insert(word)

    for word in words_to_insert:
        assert trie.search(word), f"Word {word} should be found in the trie."

    not_inserted_words = ["hell", "wor", "heroes", "heroic"]
    for word in not_inserted_words:
        assert not trie.search(word), f"Word {word} should not be found in the trie."


def test_delete():
    trie = PatriciaTrie()

    words_to_insert = ["hello", "world", "hi", "her", "hero", "heron"]
    for word in words_to_insert:
        trie.insert(word)

    words_to_delete = ["hello", "hero", "heron"]
    for word in words_to_delete:
        trie.delete(word)
        assert not trie.search(word), f"Word {word} should not be found in the trie after deletion."

    remaining_words = ["world", "hi", "her"]
    for word in remaining_words:
        assert trie.search(word), f"Word {word} should still be found in the trie."


if __name__ == "__main__":
    test_insert_and_search()
    test_delete()
    print("All tests passed.")
