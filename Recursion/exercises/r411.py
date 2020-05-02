#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Any


def one_comp_all(element: Any, s: List[Any]) -> bool:
    for i in range(len(s)):
        if element == s[i]:
            return False
    return True


def is_unique(s: List[Any]) -> bool:
    if len(s) == 1:
        return True
    return is_unique(s[1:]) and one_comp_all(s[0], s[1:])


if __name__ == "__main__":
    print(is_unique([1, 2, 3, 1, 2, 3]))
    print(is_unique([1, 2, 3, 4]))
    print(is_unique([1, 2]))
