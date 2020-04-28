#!/usr/bin/env python3


def quicksort(arr, s, e):
    if e - s < 1:
        return
    p = arr[-1]
    if len(arr) > 5:
        p = (arr[-1] + arr[-2] + arr[-3] + arr[-4] + arr[-5]) / 5
    s1, e1 = s, e

    while s1 < e1:
        if arr[s1] > p:
            arr[s1], arr[e1] = arr[e1], arr[s1]
            e1 -= 1
        else:
            s1 += 1

    quicksort(arr, s, s1)
    quicksort(arr, e1+1, e)


def rearange_digits(input):
    input = quicksort(input[:], 0, len(input)-1)
    out = [0, 0]
    i = len(input) - 1

    while i >= 0:
        if i % 2 == 0:
            out[0] *= 10
            out[0] += input[i]
        else:
            out[1] *= 10
            out[1] += input[i]

    return out


def test(input, expected, tst):
    actual = tst(input)
    try:
        assert(expected == actual)
        print(f"\u2705 Expected {expected}, got {actual}")
    except AssertionError:
        print(f'\u274C Expected {expected}, got {actual} for {input}')
        return True

# [3 4 5 6 6 8 9 9]
def main():
    test_list = [
        ([1, 2, 3, 4, 5], [531, 42]),
        ([6, 5, 9, 6, 8, 3, 4, 9], [9653, 9864]),
        ([4, 6, 2, 5, 9, 8], [852, 964])
    ]
    for q, a in test_list:
        test(q, a, rearange_digits)


if __name__ == '__main__':
    main()
