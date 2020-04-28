#!/usr/bin/env python3


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr, n, i):
    left = (i * 2) + 1
    right = left + 1
    if left > n:
        return
    if right > n:
        if arr[left] > arr[i]:
            swap(arr, left, i)
        return

    max_child = left if arr[left] > arr[right] else right
    if arr[max_child] > arr[i]:
        swap(arr, max_child, i)
        heapify(arr, n, max_child)


def build_max_heap(arr):
    n = len(arr) - 1
    i = n//2
    while i >= 0:
        heapify(arr, n, i)
        i -= 1


def rearange_digits(arr):
    build_max_heap(arr)
    n = len(arr)-1

    out = [0, 0]
    while n >= 0:
        largest = arr[0]
        swap(arr, n, 0)
        n -= 1
        heapify(arr, n, 0)

        out[n % 2] *= 10
        out[n % 2] += largest
    return out if out[0] > out[1] else [out[1], out[0]]


def test(input, expected, tst):
    actual = tst(input)
    try:
        assert(expected == actual)
        print(f"\u2705 Expected {expected}, got {actual}")
    except AssertionError:
        print(f'\u274C Expected {expected}, got {actual} for {input}')
        return True


def main():
    test_list = [
        ([1, 2, 3, 4, 5], [531, 42]),
        ([6, 5, 9, 6, 8, 3, 4, 9], [9864, 9653]),
        ([4, 6, 2, 5, 9, 8], [964, 852])
    ]
    for q, a in test_list:
        test(q, a, rearange_digits)

    print("passed \U0001F60E")


if __name__ == '__main__':
    main()
