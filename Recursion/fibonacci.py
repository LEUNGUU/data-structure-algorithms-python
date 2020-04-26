#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Running time is exponential in n.
def bad_fibonacci(n):
    """Return the nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


# Running time is linear time
def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)


if __name__ == "__main__":
    print(good_fibonacci(3))
