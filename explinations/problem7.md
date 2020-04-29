# Problem 7: Trie based HTTPRouter

Also uses `RouteTrie.py` and `Router.py`

On initializing a `Router` it initializes a `RouterTrie`. The Nodes hold the path handlers. Inserting and accessing are O(h) time complexity. Accessing takes O(1) space. The trie takes at least O(n) space. If there are a lot of "folders" (intermediate nodes without handlers) the space complexity could be much worse.