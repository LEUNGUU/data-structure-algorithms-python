#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def scale(data, factor):
    """ Multiply all entries of numeric data list by the given factor.

    data    an intance of any mutable sequence type (such as a list)
            containing numeric elements

    factor  a number that serves as the multiplicative factor for scaling
    """

    for j in range(len(data)):
        data[j] *= factor


if __name__ == "__main__":
    pass
