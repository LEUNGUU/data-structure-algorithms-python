#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Any


def get_subsets(s: List[Any]) -> List[Any]:
    if len(s) == 0:
        return [[]]
    return [[s[0]] + i for i in get_subsets(s[1:])] + get_subsets(s[1:])


if __name__ == "__main__":
    print(get_subsets([4, 3, 2]))
