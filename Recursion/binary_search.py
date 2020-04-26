#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if (
        low > high
    ):  # Because low is asymptotically close to high. After low=high, then low+1 > high
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    print(binary_search(list(range(0, 100)), 999, 0, 99))
