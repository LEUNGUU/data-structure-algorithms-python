#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


class AdapterQueue:
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def first(self):
        return self._queue[0]

    def enqueue(self, e):
        self._queue.append(e)

    def dequeue(self):
        self._queue.popleft()


if __name__ == "__main__":
    pass
