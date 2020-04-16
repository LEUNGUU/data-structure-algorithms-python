#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def words(letters, word=''):
    print("before print: ", letters)
    print("before print: ", word)
    letters or print(word)
    for letter in letters:
        print('while loop, letter: ', letter)
        print('while loop, letters: ', letters)
        words(letters - {letter}, word + letter)

if __name__ == '__main__':
    print(words(set('catdog')))
