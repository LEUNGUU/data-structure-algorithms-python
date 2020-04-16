#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint, choice


def punishment():
    sentence = []
    for _ in range(0, 100):
        sentence.append("I will never spam my friends again.")

    miss = 0
    while miss < 8:
        index = randint(0,99)
        print(index)
        while True:
            pos = randint(0, len(sentence[index])-1)
            if sentence[index][pos] not in [' ', '.']:
                sentence[index] = sentence[index][0:pos]+chr(choice(range(97,123)))+sentence[index][pos+1:] 
                break
        miss += 1
    return sentence


if __name__ == '__main__':
    print(punishment())
