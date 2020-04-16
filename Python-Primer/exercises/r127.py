#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def factors(n):  # generator that computes factors
    k = 1
    temp = []
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:  # special case if n is perfect square
        yield k
    for item in reversed(temp):
        yield item


if __name__ == "__main__":
    for item in factors(10):
        print(item)
