#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]


if __name__ == "__main__":
    print(linear_sum([1, 2, 3, 4], 3))
