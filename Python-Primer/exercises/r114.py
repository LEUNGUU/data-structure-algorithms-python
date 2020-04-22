#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# hints: Note that both numbers in the pair must be odd
def pairsOdd(a: list) -> list:
    temp = []
    for i in a:
        for j in a:
            if i != j and (i * j) % 2 != 0:
                temp.append(tuple(sorted((i, j))))
    res = {item for item in temp}
    return res


def pairsOdd2(a: list) -> list:
    res = []
    for index in range(0, len(a)):
        if (index + 1) < len(a):
            res.append(
                [
                    (a[index], item)
                    for item in a[index + 1 :]
                    if a[index] * item % 2 != 0
                ]
            )
    return res


def is_product_odd_in(a: list) -> bool:
    odd = [item for item in a if item & 1]
    return True if len(odd) >= 2 else False


if __name__ == "__main__":
    print(pairsOdd([1, 2, 3, 5, 6, 7]))
    print(pairsOdd2([1, 2, 3, 5, 6, 7]))
    print(is_product_odd_in([1, 2, 3, 5, 6, 7]))
