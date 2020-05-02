#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_vowels(s: int, count=0) -> int:
    vowels = "aeiouAEIOU"
    if len(s) == 0:
        return count
    elif s[0] in vowels:
        return count_vowels(s[1:], count + 1)
    else:
        return count_vowels(s[1:], count)


def is_more_vowels(s: str) -> bool:
    num_vowels = count_vowels(s)
    num_consonants = len(s) - num_vowels
    if num_vowels > num_consonants:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_more_vowels("heo"))
