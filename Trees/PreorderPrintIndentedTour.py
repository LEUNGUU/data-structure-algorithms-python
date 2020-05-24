#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from EulerTour import EulerTour
from LinkedBinaryTree import LinkedBinaryTree


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * " " + str(p, element()))


if __name__ == "__main__":
    LBT = LinkedBinaryTree()
