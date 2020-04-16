#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factors(n:int) -> list:
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
        if k * k == n:
            yield k

# comprehension
# factors = [k for k in rnge(1, n+1) if n % k == 0]

if __name__ == '__main__':
    for factor in factors(100):
        print(factor)
