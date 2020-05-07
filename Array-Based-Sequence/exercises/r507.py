#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_dup(nums):
    n = len(nums)
    return sum(nums) - n * (n - 1) // 2


if __name__ == "__main__":
    print(find_dup([1, 2, 3, 2]))
