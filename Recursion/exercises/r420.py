#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List


def sortby_k(num: List[int], k: int) -> List[int]:
    if not num:
        return []
    if num[0] <= k:
        return [num[0]] + sortby_k(num[1:], k)
    else:
        return sortby_k(num[1:], k) + [num[0]]


if __name__ == "__main__":
    print(sortby_k([1, 2, 3, 1, 2, 768, 46], 1))
