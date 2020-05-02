#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_sum(n: int) -> float:
    if n == 1:
        return 1
    return 1 / n + harmonic_sum(n - 1)


if __name__ == "__main__":
    print(harmonic_sum(1))
    print(harmonic_sum(2))
    print(harmonic_sum(3))
    print(harmonic_sum(4))
