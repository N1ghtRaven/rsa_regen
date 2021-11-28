from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA


class Regenerator:
    def __init__(self, salt):
        self.i = 0
        self.salt = salt.encode()
        self.master = None

    def not_rand(self, n):
        self.i += 1
        return PBKDF2(self.master, str(self.i).encode(), dkLen=n, count=1)

    def regenerate_key(self, key):
        self.i = 0
        self.master = PBKDF2(key, self.salt, count=10000)
        return RSA.generate(4096, randfunc=self.not_rand)
