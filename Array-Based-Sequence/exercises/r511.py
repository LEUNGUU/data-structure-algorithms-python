#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_matrix(matrix):
    total = 0
    for itemA in matrix:
        for itemB in itemA:
            total += itemB
    return total


def recursive_sum_no_tail(matrix):
    if len(matrix) == 0:
        return 0
    return sum(matrix[0]) + recursive_sum_no_tail(matrix[1:])


def recursive_sum_tail(matrix, total=0):
    if len(matrix) == 0:
        return total
    return recursive_sum_tail(matrix[1:], total + sum(matrix[0]))


if __name__ == "__main__":
    print(sum_matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(recursive_sum_no_tail([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(recursive_sum_tail([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
