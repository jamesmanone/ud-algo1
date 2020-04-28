#!/usr/bin/env python3
from random import randint


def get_min_max(arr):
    min = float("inf")
    max = float("-inf")

    if len(arr) == 0:
        return (None, None)

    for i in arr:
        min = i if i < min else min
        max = i if i > max else max

    return (min, max)


def test():
    test_list = [
        [randint(0, 100) for _ in range(randint(1, 25))] for _ in range(10)
    ]
    for l in test_list:
        sort = sorted(l)
        expected = (sort[0], sort[-1])
        actual = get_min_max(l)
        try:
            assert(actual == expected)
            print(f"\u2705 Expected {expected}, got {actual}")
        except AssertionError:
            print(f'\u274C Expected {expected}, got {actual} for {l}')


if __name__ == '__main__':
    test()
