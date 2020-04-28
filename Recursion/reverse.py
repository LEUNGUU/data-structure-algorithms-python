#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 1, 2, 3]
    reverse(S, 0, 8)
    print(S)
