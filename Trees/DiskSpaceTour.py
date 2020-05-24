#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from EulerTour import EulerTour


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)


if __name__ == "__main__":
    pass
