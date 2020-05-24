#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from EulerTour import EulerTour


class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = ".".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


if __name__ == "__main__":
    pass
