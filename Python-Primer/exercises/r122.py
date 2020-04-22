#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dotProduct(a: list, b: list) -> list:
    assert len(a) == len(b)
    return [a[index] * b[index] for index in range(len(a))]


if __name__ == "__main__":
    print(dotProduct([1, 2, 3], [1, 2, 3]))
