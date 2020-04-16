#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


def countwords(s:str) -> int:
    word_list = s.split(' ')
    return Counter(word_list)

if __name__ == '__main__':
    print(countwords("I am a good boy No other boy like me "))
