#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def asymptotic_cal_not_tail(n: int) -> int:
    if n < 2:
        return 0
    return 1 + asymptotic_cal_not_tail(n // 2)


def asymptotic_cal_tail(n: int, count=0) -> int:
    if n < 2:
        return count
    return asymptotic_cal_tail(n // 2, 1 + count)


if __name__ == "__main__":
    print(asymptotic_cal_not_tail(9))
    print(asymptotic_cal_tail(9))
