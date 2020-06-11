#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S"""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())


def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm"""
    n = len(S)
    if n < 2:
        return
    S1 = LineQueue()
    S2 = LinkQueue()
    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


if __name__ == "__main__":
    pass
