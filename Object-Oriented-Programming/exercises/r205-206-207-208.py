#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CreditCard:
    """ A consumer credit card."""

    __slots__ = "_customer", "_bank", "_account", "_limit", "_balance"

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.
        The initial balance is zero

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    # def _set_balance(self, change):
    #     """For the subclass to affect a change to the balance"""
    #     return change(self._balance)

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifing number(typically stored as string)."""
        return self._account

    def get_limit(self):
        """Return current card limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        try:
            if price + self._balance > self._limit:  # if charge would exceed limit.
                return False  # cannot accept charge
            else:
                self._balance += price
                return True
        except TypeError:
            print("Number is required!")

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        try:
            if amount < 0:
                raise ValueError("Amount must be POSITIVE!")
            self._balance -= amount
        except TypeError:
            print("Number is required!")


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    OVERLIMIT_FEE = 5
    __slots__ = "_apr"

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit catd instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate(e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """

        success = super().charge(price)
        if not success:
            self._balance -= PredatoryCreditCard.OVERLIMIT_FEE
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if super().get_balance() > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor


if __name__ == "__main__":
    wallet = []
    wallet.append(
        CreditCard("John Bowman", "California Savings", "5309 2302 9302 3203", 2500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Federal", "2343 2333 2333 3332", 3500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Finance", "2234 4322 3443 3434", 5000)
    )

    for val in range(1, 1):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    # wallet[0].charge("candy")
    # wallet[0].make_payment("candy")
    # wallet[0].make_payment(-12)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()

    prd = PredatoryCreditCard(
        "John Bowman", "California Finance", "2234 4322 3443 3434", 5000, 0.00825
    )
    print(prd.charge(5001))
    print(prd.get_balance())
