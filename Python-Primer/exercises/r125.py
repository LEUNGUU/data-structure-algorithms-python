#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import ascii_letters


def removePunctuation(a:str) -> str:
    checklist = list(ascii_letters)
    checklist.extend(['\n','\t',' '])
    res = []
    for item in a:
        if item in checklist:
            res.append(item)
    return ''.join(res)


if __name__ == '__main__':
    print("Let's try, \n Mike.")
    print(removePunctuation("Let's try, \n Mike."))
