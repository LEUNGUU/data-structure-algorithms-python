#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Linked-List")
from _SinglyLinkedList import SinglyLinkedList


# r7.1
def second_to_last(linkedlist):
    return linkedlist.index(-2)


# r7.2
def contactentate_list(linkedlist1, linkedlist2):
    answer = SinglyLinkedList()
    answer.add_first(linkedlist1.head)
    linkedlist1.add_last(linkedlist2.head)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    for i in range(5):
        sll.add_first(i)
    print(second_to_last(sll))
