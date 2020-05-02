#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


# because the list is in increasing order, so we can do like this.
def find_pair_sum_to_k(num: List[int], k: int, start: int, end: int) -> tuple:
    assert len(num) > 2
    if start == end:
        return ()
    if num[start] + num[end] > k:
        return find_pair_sum_to_k(num, k, start, end - 1)
    elif num[start] + num[end] < k:
        return find_pair_sum_to_k(num, k, start + 1, end)
    else:
        return (num[start], num[end])


if __name__ == "__main__":
    print(find_pair_sum_to_k([1, 2, 3, 4, 5, 6], 9, 0, 5))
