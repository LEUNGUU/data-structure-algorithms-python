#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    content = []
    while True:
        try:
            line = input()
            content.append(line)
        except EOFError:
            content.reverse()
            print('\n'.join(content))
            break

