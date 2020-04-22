#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Hints: Use bit opertions
def is_even(k:int) -> bool:
    return not k & 1

if __name__ == '__main__':
    print(is_even(9))
