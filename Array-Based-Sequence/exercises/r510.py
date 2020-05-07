#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CaeserCipher:
    """Class for doing encryption and decryption using caeset cipher"""

    def __init__(self, shift):
        """Construct a caeser cipher using a given integer shift for rotation"""
        self._forward = "".join([chr((i + shift) % 26 + ord("A")) for i in range(26)])
        self._backard = "".join([chr((i - shift) % 26 + ord("A")) for i in range(26)])

    def encrypt(self, message):
        """Return string representing encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message by a given secret"""
        return self._transform(secret, self._backard)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = code[j]
        return "".join(msg)


if __name__ == "__main__":
    cipher = CaeserCipher(3)
    msg = "THE EAGLE IS IN PLAY"
    coded = cipher.encrypt(msg)
    print("secret: ", coded)
    decoded = cipher.decrypt(coded)
    print("message: ", decoded)
