#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def recursive_product_tail(n: int, m: int, total=0) -> int:
    if n < 1:
        return total
    return recursive_product_tail(n - 1, m, m + total)


def recursive_product_no_tail(n: int, m: int) -> int:
    if n < 1:
        return 0
    return m + recursive_product_no_tail(n - 1, m)


if __name__ == "__main__":
    # print(recursive_product(9,0))
    # print(recursive_product(1,9))
    # print(recursive_product(8,9))
    print(recursive_product_tail(997, 999))
    print(recursive_product_no_tail(997, 999))
