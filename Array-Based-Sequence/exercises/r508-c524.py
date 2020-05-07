#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from time import time


def benchmark(test_func):
    insert_df = pd.DataFrame(
        index=["start", "middle", "end"], columns=["100", "1000", "10000", "100000"]
    )
    insert_df.index.name = "Time(microseconds)"
    for n in list(insert_df.columns):
        insert_df[n] = [test_func(int(n), mode) for mode in insert_df.index]
    return insert_df


def insert_average(n, mode="start"):
    data = []
    start = time()
    if mode == "start":
        for _ in range(n):
            data.insert(0, None)
    elif mode == "middle":
        for _ in range(n):
            data.insert(n // 2, None)
    elif mode == "end":
        for _ in range(n):
            data.insert(n, None)
    end = time()
    return (end - start) * 1000000 / n


def pop_average(n, mode="start"):
    data = [None] * n
    start = time()
    if mode == "start":
        for _ in range(n):
            data.pop(0)
    elif mode == "middle":
        count = n
        while count > 0:
            data.pop(count // 2)
            count -= 1
    elif mode == "end":
        for _ in range(n):
            data.pop(-1)
    end = time()
    return (end - start) * 1000000 / n

def remove_average(n, mode="start"):
    data = [None] * n
    start = time()
    if mode == "start":
        for _ in range(n):
            data.remove(data[0])
    elif mode == "middle":
        count = n
        while count > 0:
            data.remove(data[count//2])
            count -= 1
    elif mode == "end":
        for _ in range(n):
            data.remove(data[-1])
    end = time()
    return (end - start) * 1000000 / n




if __name__ == "__main__":
    print(benchmark(insert_average))
    print(benchmark(pop_average))
    print(benchmark(remove_average))
