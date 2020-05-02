#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def char_to_int(ch: str) -> int:
    """Convert a char to int"""
    return ord(ch) - ord("0")


def convert_string(s: str) -> int:
    if len(s) == 1:
        return char_to_int(s)
    return char_to_int(s[0]) * (10 ** (len(s) - 1)) + convert_string(s[1:])


if __name__ == "__main__":
    print(convert_string("12321"))
    print(convert_string("12521"))
