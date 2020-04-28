class RouteTrie:
    class Node:
        def __init__(self):
            self.__handler = None
            self.__children = {}

        @property
        def handler(self):
            return self.__handler is not None

        @handler.setter
        def handler(self, func):
            self.__handler = func

        def get(self, *args, **kwargs):
            if not self.handler:
                raise KeyError("handler not found")
            self.__handler(*args, **kwargs)

        # forward 'in' to self.__children
        def __contains__(self, key):
            return key in self.__children

        # RouteTrie.Node &operator[]() to act more like defaultdict. upserting
        # in __children can be done with out fear of NoneType
        def __getitem__(self, key):
            if key not in self:
                self.__children[key] = RouteTrie.Node()
            return self.__children[key]

        # void operator[](func)
        def __setitem__(self, key, handler):
            if key not in self:
                self.__children[key] = RouteTrie.Node()
            self.__children[key].__handler = handler

        def insert(self, path, handler=None):
            self[path] = handler if handler is not None else RouteTrie.Node()

    # end RouteTrie.Node
    def __init__(self):
        self.__root = RouteTrie.Node()

    def lookup(self, path, force=False):
        root = self.__root
        for part in self.str_to_path(path):
            if not force and part not in root:
                return None
            root = root[part]
        return root

    @classmethod
    def str_to_path(cls, string):
        # eliminates leading and trailing /
        return [x for x in string.split('/') if x != '']
