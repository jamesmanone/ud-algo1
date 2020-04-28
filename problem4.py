#!/usr/bin/env python3
from random import randint


def sort_012(arr):
    s = 0
    e = len(arr) - 1

    while s < len(arr) and arr[s] == 0:
        s += 1

    while e > s and arr[e] == 2:
        e -= 1

    i = s
    while i <= e:
        if arr[i] == 2:
            arr[i], arr[e] = arr[e], arr[i]
            e -= 1
        elif arr[i] == 0:
            arr[i], arr[s] = arr[s], arr[i]
            s += 1
            if s > i:
                i = s
        else:
            i += 1

    return arr


def test():
    test_list = [
        [randint(0, 2) for _ in range(randint(1, 25))] for _ in range(20)
    ]

    for l in test_list:
        expected = sorted(l)
        actual = sort_012(l)
        try:
            assert(actual == expected)
            print(f"\u2705 Expected {expected}, got {actual}")
        except AssertionError:
            print(f'\u274C Expected {expected}, got {actual} for {l}')


if __name__ == "__main__":
    test()
