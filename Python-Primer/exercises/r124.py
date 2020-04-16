#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def vowels(a:str) -> int:
    vowels = ['a','e','i','o','u']
    count = 0
    for item in a:
        if item in vowels:
            count += 1
    return count


if __name__ == '__main__':
    print(vowels("hello"))
