from string import ascii_lowercase, ascii_uppercase
from random import randint
import inspect


class Logger(object):   # this is a standard logger.
    def __init__(self, logger=print):
        self.logger = logger
    def log(self, *args):
        print(inspect.getmodule(inspect.stack()[1][0]), end=": ")
        self.logger(*args)


def _egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = _egcd(a, m)
    if gcd == 1:
        return x % m
    # mod inv doesn't exist.


def shift_char(char, dx):
    """
    This function returns the char obtained after displacement of dx from char.
    """
    if not isinstance(char, str) or len(char) != 1 :
        raise ValueError("Char is a one length string.")
    
    if char.isupper():
        charset = ascii_uppercase
    else:
        charset = ascii_lowercase
    base_idx = charset.index(char)
    return charset[ (base_idx + dx) % 26 ]


def get_rand_ascii_str(max_len_string=20):
    string = "".join(chr(97+randint(0, 25)) for i in range(randint(0, max_len_string)))
    upper_case = randint(0, 1)
    return string.upper() if upper_case else string
