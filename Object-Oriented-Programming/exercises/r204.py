#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Flower:
    """This is a flower class"""

    def __init__(self, name: str, petals: int, price: float):
        """Create a new float instance.

        name   the name of the flower
        petals the number of the petals
        price  the price of the flower
        """
        self._name = name
        self._petals = petals
        self._price = price

    @property
    def name(self):
        """Return name of the flower"""
        return self._name

    @property
    def petals(self):
        """Return the number of petals of the flower"""
        return self._petals

    @property
    def price(self):
        """Return the price of the flower"""
        return self._price

    def set_name(self, name: str):
        """Set the name of the flower"""
        self._name = name

    def set_petals(self, petals: int):
        """Set the number of petals of the flower"""
        self._petals = petals

    def set_price(self, price: float):
        """Set the price of the flower"""
        self._price = price


if __name__ == "__main__":
    # test my flower class
    f = Flower("rose", 9, 10.08)
    print("name: {}, petals: {}, price: {}".format(f.name, f.petals, f.price))
    print("set new name and petals and price")
    f.set_name("lily")
    f.set_petals(10)
    f.set_price(9.234)
    print("name: {}, petals: {}, price: {}".format(f.name, f.petals, f.price))
