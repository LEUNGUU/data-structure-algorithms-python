#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def even_before_odd(nums: List[int]) -> List[int]:
    if not nums:
        return []
    if nums[0] % 2 == 0:
        return [nums[0]] + even_before_odd(nums[1:])
    else:
        return even_before_odd(nums[1:]) + [nums[0]]


if __name__ == "__main__":
    print(even_before_odd([2, 3, 4, 2, 8, 7]))
