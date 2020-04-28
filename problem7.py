#!/usr/bin/env python3
from Router import Router


def make_handler(path, name):
    def handler(request=None, response=None):
        if response is None:
            raise TypeError
        if request is None:
            return response.error(500)

        if request.path is None or type(request.path) != str:
            return response.error(500)

        return response.write(f"{name}")
    return handler


routes = [
    ('/', 'index'),
    ('/about', 'about'),
    ('404', 'These aren\'t the bytes you\'re looking for'),
    ('/home/page', 'Homepage')
]

router = Router(8000)
for route in routes:
    router.add_handler(route[0], make_handler(*route))

router.get('/')  # prints 'index'
router.get('/about')  # prints 'about'
router.get('/home')  # 404
router.get('/home/page')  # Homepage
