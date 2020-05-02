#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def is_palindrome(s: str) -> bool:
#    def judge(s: str, start: int, end: int) -> bool:
#        n = end - start + 1
#        if n <= 1:
#            return True
#        return (s[start] == s[end]) and judge(s, start+1, end-1)
#    return judge(s, 0, len(s)-1)


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    return (s[0] == s[len(s) - 1]) and is_palindrome(s[1 : len(s) - 1])


if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome("gohangasalamiimalasagnahog"))
