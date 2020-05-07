#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CaeserCipher:
    """Class for doing encryption and decryption using caeset cipher"""

    def __init__(self, shift):
        """Construct a caeser cipher using a given integer shift for rotation"""
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord("A"))
            decoder[i] = chr((i - shift) % 26 + ord("A"))
        self._forward = "".join(encoder)
        self._backard = "".join(decoder)

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
