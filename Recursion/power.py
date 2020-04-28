#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# running time is O(n)
def power1(x, n):
    """Compute the x**n for integer n"""
    if n == 0:
        return 1
    else:
        return x * power1(x, n - 1)


# running time is O(logn)
def power2(x, n):
    """Compute the x**n for integer n"""
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


if __name__ == "__main__":
    print(power1(10, 3))
    print(power2(10, 3))
