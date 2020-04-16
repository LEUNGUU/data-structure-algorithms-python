#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lessThan2(a:int) -> int:
    if a <= 2:
        print("input must be greater that 2!")
    else:
        count = 1
        while a / 2 >= 2:
            count += 1
            a = a / 2
        return count



if __name__ == '__main__':
    print("10: ", lessThan2(10))
    print("2: ", lessThan2(2))
    print("100: ", lessThan2(100))
