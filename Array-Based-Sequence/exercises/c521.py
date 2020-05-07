#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time

DOCUMENT = "Hello, Python!" * 1000


def a1_concatenation():
    letters = ""
    for c in DOCUMENT:
        if c.isalpha():
            letters += c
    return letters


def a2_appending():
    temp = []
    for c in DOCUMENT:
        if c.isalpha():
            temp.append(c)
    return "".join(temp)


def a3_list_comp():
    letters = "".join([c for c in DOCUMENT if c.isalpha()])
    return letters


def a4_generator():
    letters = "".join(c for c in DOCUMENT if c.isalpha())
    return letters


def time_report(func):
    start = time()
    func()
    end = time()
    return (end - start) * 1000000


if __name__ == "__main__":
    print("a1_concatenation: ", time_report(a1_concatenation))
    print("a2_appending: ", time_report(a2_appending))
    print("a3_list_comp: ", time_report(a3_list_comp))
    print("a4_generator: ", time_report(a4_generator))
