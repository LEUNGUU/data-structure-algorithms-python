#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse_str(s: str) -> str:
    if len(s) == 1:
        return s[0]
    return s[-1] + reverse_str(s[:-1])


if __name__ == "__main__":
    print(reverse_str("pots&pans"))
    print(reverse_str("snap&stop"))
