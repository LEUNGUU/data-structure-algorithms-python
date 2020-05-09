#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import time


def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed"""
    data = []
    start = time()
    for i in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


if __name__ == "__main__":
    print("10 append operations: ", compute_average(10))
    print("100 append operations: ", compute_average(100))
    print("1000 append operations: ", compute_average(1000))
    print("10000 append operations: ", compute_average(10000))
