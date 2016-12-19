import pytest
from rsa_encryption_gui.rsa_encryption import *


class TestEncryption:

    def test_keygen(self):
        self.private_class = PrivateKeyGen()
        while not self.private_class.public_exponent():
            self.private_class = PrivateKeyGen()
            self.private_class.public_exponent()

        assert self.private_class.public_exponent()

        self.private_class.private_exponent()
        assert self.private_class.d

    def test_public(self):
        self.public_class = PublicKey(e=1, n=1)
        public_exponent, public_power = self.public_class.print_key()
        assert public_exponent and public_power
