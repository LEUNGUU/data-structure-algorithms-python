#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minmax(data:list) -> tuple:
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest, largest


if __name__ == '__main__':
    print(minmax([-1,2,-3,4,5]))
