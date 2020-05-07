#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(A):
    """sort list of comparable elements into nondecreasing order"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur


if __name__ == "__main__":
    A = [1, 2, 6, 9, 1, 8, 3]
    insertion_sort(A)
    print(A)
