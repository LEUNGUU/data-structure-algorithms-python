#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def matrix_sum(matrix):
    return sum(num for raw in matrix for num in raw)


if __name__ == "__main__":
    print(matrix_sum([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
