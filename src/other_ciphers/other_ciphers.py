import sys
sys.path.append('.')
sys.path.append("..")
sys.path.append('./src/')
sys.path.append('../src/')

import itertools
from utils import modinv, shift_char


def all_caps_trim_ws(func):
    # removes all the spaces and convert all text args to uppercase.
    def wrapper(*args, **kwargs):
        args = list(args)    # so that it can be modified.
        for idx, arg in enumerate(args):
            if isinstance(arg, str):
                args[idx] = arg.upper().replace(" ", "")
        return func(*args, **kwargs)
    return wrapper

class Ciphers:
    def __init__(self, key=3):
        self.key = key

    @all_caps_trim_ws
    def encrypt_affine(self, msg, a=None, b=None):
        '''
        C = (a*P + b) % 26
        '''
        if a is None and b is None:
            a, b = self.key
        return ''.join([ chr((( (a*(ord(t) - ord('A')) + b)) % 26) + ord('A')) for t in msg ])

    def decrypt_affine(self, cipher, a=None, b=None):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        if a is None and b is None:
            a, b = self.key
        return ''.join([ chr((( modinv(a, 26)*(ord(c) - ord('A') - b) ) % 26) + ord('A')) for c in cipher ])

    @all_caps_trim_ws
    def encrypt_shift(self, text, key=None):
        '''
        C = (P + K) % 26
        '''
        key = self.key if key is None else key
        return "".join(shift_char(char, key) for char in text)

    def decrypt_shift(self, cipher):
        '''
        P = (C - K) % 26
        '''
        return self.encrypt_shift(cipher, -self.key)

    @all_caps_trim_ws
    def encrypt_multiplicative(self, text):
        '''
        C = (P * K) % 26
        '''
        return self.encrypt_affine(text, a=self.key, b=0)

    def decrypt_multiplicative(self, cipher):
        '''
        P = (C * K^-1) % 26
        '''
        return self.decrypt_affine(cipher, a=self.key, b=0)

    @all_caps_trim_ws
    def encrypt_vignere(self, text):
        '''
        Ci = (Pi + Ki) mod 26
        '''
        return ''.join([chr(((ord(a)-ord('A')) + (ord(b)-ord('A'))) % 26 + ord('A')) for a,b in zip(text, itertools.cycle(self.key))])

    def decrypt_vignere(self, cipher):
        '''
        Pi = (Ci - Ki + 26) mod 26
        '''
        return ''.join([chr(((ord(a)-ord('A')) - (ord(b)-ord('A')) + 26) % 26 + ord('A')) for a,b in zip(cipher, itertools.cycle(self.key))])


def main():
    text = 'twentyfifteen'
    ciphers = Ciphers(5)

    #------------ Additive or Shift Cipher -------------#

    shift_encrypt_text = ciphers.encrypt_shift(text)
    print('Additive Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(shift_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.decrypt_shift(shift_encrypt_text) ))

    #---------- Additive or Shift Cipher Ends ----------#


    #------------ Multiplicative Cipher -------------#

    multiplicative_encrypt_text = ciphers.encrypt_multiplicative(text)
    print('Multiplicative Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(multiplicative_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.decrypt_multiplicative(multiplicative_encrypt_text) ))

    #---------- Multiplicative Cipher Ends ----------#

    #------------ Affine Cipher -----------#

    affine_cipher = Ciphers((17, 20))
    affine_encrypted_text = affine_cipher.encrypt_affine(text)
    print('Affine Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print('Decrypted Text: {}\n'.format( affine_cipher.decrypt_affine( affine_encrypted_text ) ))

    #--------- Affine Cipher Ends ---------#

    #----------- Vignere Cipher ------------#
    vignere = Ciphers('apex')
    vignere_encrypted_text = vignere.encrypt_vignere(text)
    print('Vignere Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(vignere_encrypted_text))
    print('Decrypted Text: {}'.format( vignere.decrypt_vignere(vignere_encrypted_text) ))
    #---------- Vignere Cipher Ends --------#


if __name__ == '__main__':
    main()
