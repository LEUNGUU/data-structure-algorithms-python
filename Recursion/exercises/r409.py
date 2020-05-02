#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# find the largest and smallest element in a list
def min_max(nums: list) -> tuple:
    if len(nums) == 1:
        return (nums[0], nums[0])
    return (min(nums[0], min_max(nums[1:])[0]), max(nums[0], min_max(nums[1:])[1]))


if __name__ == "__main__":
    print(min_max([1, 2, 3, 6, 4, 3, 7]))
