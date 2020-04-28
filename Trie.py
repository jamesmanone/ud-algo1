class Trie:
    class Node:
        def __init__(self, letter):
            self.__children = {}
            self.__letter = letter
            self.is_word = False

        # forward 'in' to self.__children
        def __contains__(self, key):
            return key in self.__children

        # Trie.Node &operator[]() to act more like defaultdict. upserting in
        # __children can be done with out fear of NoneType
        def __getitem__(self, key):
            if key not in self.__children:
                self.__children[key] = Trie.Node(key)
            return self.__children[key]

        # void operator[](bool)
        def __setitem__(self, key, val):
            if key not in self.__children:
                self.__children[key] = Trie.Node(key)
            self.__children[key].is_word = val

        def insert(self, char):
            self[char] = False

        # Recursive helper for .suffixes
        def __suffixes(self):
            out = []
            if self.is_word:
                out.append("")
            for char in self.__children.values():
                out += char.__suffixes()
            return [self.__letter + x for x in out]

        # Works the same as __suffixes but doesn't prepend self.__letter
        def suffixes(self):
            out = []
            for char in self.__children.values():
                out += char.__suffixes()
            return out

    # end Trie.Node
    def __init__(self):
        self.__root = Trie.Node(None)

    def insert(self, word):
        root = self.__root
        for char in word:
            root = root[char]  # override operator[] to upsert on __children
        root.is_word = True

    # Return type is Trie.Node
    def find(self, substr):
        root = self.__root
        for char in substr:
            if char not in root:  # override in to return in node.__children
                return Trie.Node(None)
            root = root[char]
        return root
