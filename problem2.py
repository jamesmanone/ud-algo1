#!/usr/bin/env python3


# O(log(n))
def find_min(arr):
    s = 0
    e = len(arr) - 1
    while e > s:
        c = ((e - s) // 2) + s
        if arr[s] > arr[c]:
            e = c
        elif arr[e] < arr[c]:
            s = c + 1
        else:
            return s
    return s


def binary_search(arr, t):
    s = 0
    e = len(arr)
    while s < e:
        c = ((e - s) // 2) + s
        if arr[c] < t:
            s = c + 1
        elif arr[c] > t:
            e = c
        else:
            return c
    return -1


def rotated_search(arr, t):
    if len(arr) == 0:
        return -1
    offset = find_min(arr)
    if t > arr[-1]:
        return binary_search(arr[:offset], t)
    else:
        index = binary_search(arr[offset:], t)
        return index + offset if index is not -1 else -1


def test(input, expected, tst):
    actual = tst(input[0], input[1])
    try:
        assert(actual == expected)
        print(f"\u2705 Expected {expected}, got {actual}")
    except AssertionError:
        print(f'\u274C Expected {expected}, got {actual} for {input}')
        return True


def main():
    test_list = [
        ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1], 5),
        ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6], 0),
        ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 2], 6),
        ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11], -1),
        ([[6, 7, 8, 1, 2, 3, 4], 3], 5),
        ([[6, 7, 8, 1, 2, 3, 4], 8], 2),
        ([[], 2], -1)
    ]
    for q, a in test_list:
        test(q, a, rotated_search)


if __name__ == '__main__':
    main()
