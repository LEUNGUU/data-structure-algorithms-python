#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Empty(Exception):
    """Error attempting to access an element from an empty container"""

    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)

    def top(self):
        """
        Return(but do not remove) the element at the top of the stack
        Raise empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise"""
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise"""
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1 : k]
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return S.is_empty()


if __name__ == "__main__":
    AS = ArrayStack()
    print("push 1,2 into stack")
    AS.push(1)
    AS.push(2)
    print(AS.pop())
    reverse_file("test")
    print(is_matched("[5+x)]"))
    print(is_matched_html("<body>hello</body>"))
