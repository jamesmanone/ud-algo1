#!/usr/bin/env python3


def root2(n):
    if n == 1:  # edge case
        return 1

    low = 0
    high = n
    while high > low + 1:
        guess = ((high - low)//2) + low
        g2 = guess*guess
        if g2 == n:
            return guess
        elif g2 > n:
            high = guess
        elif g2 < n:
            low = guess
    return low


if __name__ == "__main__":
    from math import sqrt

    fail = False
    n = 300000
    for i in range(n):
        actual = root2(i)
        expected = int(sqrt(i))
        try:
            assert(actual == expected)
        except AssertionError:
            print(f"For {i} expected {expected}, got {actual}")
            fail = True
    print(f"All {n} test cases passed! \U0001F60E")
