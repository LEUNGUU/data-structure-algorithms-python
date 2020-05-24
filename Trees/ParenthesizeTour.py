#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from EulerTour import EulerTour


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(", ", end="")
        print(p)
        print(p.element(), end="")
        if not self.tree().is_leaf(p):
            print(" (", end="")

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(")", end="")


if __name__ == "__main__":
    pass
