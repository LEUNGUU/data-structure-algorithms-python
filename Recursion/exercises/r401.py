#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# find the largest element in a list
def find_maximum(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], find_maximum(nums[1:]))


if __name__ == "__main__":
    print(find_maximum([1, 2, 3, 6, 4, 3, 7]))
