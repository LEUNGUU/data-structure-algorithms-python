#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_even(k:int) -> bool:
    return True if (-1)**k == 1 else False


if __name__ == '__main__':
    print(is_even(9))
