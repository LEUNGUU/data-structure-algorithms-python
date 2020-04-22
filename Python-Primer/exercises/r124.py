#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# hints:You can use the condition ch in 'aeiou' to test if a character is a vowel.
def vowels(a: str) -> int:
    count = 0
    for item in a:
        if item in "aeiouAEIOU":
            count += 1
    return count


if __name__ == "__main__":
    print(vowels("hello"))
