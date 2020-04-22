#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# hints:Keep track of the smallest and largest value while looping
def minmax(data: list) -> tuple:
    smallest = largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item
    return smallest, largest


if __name__ == "__main__":
    print(minmax([-1, 2, -3, 4, 5]))
