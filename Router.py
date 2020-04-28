from RouteTrie import RouteTrie


class Router:
    class Response:
        __errors = {
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            418: 'I\'m a teapot',
            500: 'Internal Server Error',
            502: 'Bad Gateway',
            503: 'Service Unavailable'
        }

        def __init__(self):
            self.write = print

        def error(self, code):
            self.write(f"{code} {self.__errors[code]}")

    class Request:
        def __init__(self, path, **kwargs):
            self.path = path
            for kw in kwargs:
                setattr(self, kw, kwargs[kw])

    # begin Router
    def __init__(self, port):
        self.__listen_on = port
        self.__trie = RouteTrie()

    def add_handler(self, path, handler):
        node = self.__trie.lookup(path, force=True)
        node.handler = handler

    def __not_found(self, path):
        node = self.__trie.lookup('404')
        if node is not None:
            return node.get(
                request=Router.Request(path),
                response=Router.Response()
            )
        return self.Response().error(404)

    def get(self, path):
        node = self.__trie.lookup(path)
        if node is None or not node.handler:
            return self.__not_found(path)
        node.get(
            request=Router.Request(path),
            response=Router.Response()
        )
