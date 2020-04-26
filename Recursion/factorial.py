#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        # debug the recursive step
        print(n)
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(9))
