#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def distinctFromEachOther(a:list) -> bool:
    return True if len(a) == len(set(a)) else False
        

if __name__ == '__main__':
    print(distinctFromEachOther([1,2,3,1]))
