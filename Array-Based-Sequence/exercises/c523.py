#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time


def list_comprehension(n):
    return ["a" for _ in range(n)]


def list_append(n):
    res = []
    for _ in range(n):
        res.append("a")
    return res


def time_report(func):
    start = time()
    func(100)
    end = time()
    return (end - start) * 1000000


if __name__ == "__main__":
    print("list_comprehension: ", time_report(list_comprehension))
    print("list_append: ", time_report(list_append))
