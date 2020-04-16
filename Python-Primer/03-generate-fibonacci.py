#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future

def fibonacci2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a +b

if __name__ == '__main__':
    for elem in fibonacci():
        print(elem)
