#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a=[1]
    try:
        a[12]=5
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
