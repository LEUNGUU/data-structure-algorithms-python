#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def distinctFromEachOther(a:list) -> bool:
    temp = {item for item in a}
    if len(temp) == len(a):
        return True
    else:
        return False
        

if __name__ == '__main__':
    print(distinctFromEachOther([1,2,3,1]))
