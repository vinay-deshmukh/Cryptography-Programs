import itertools
from utils import modinv


class Ciphers:
    def __init__(self, text, key=3):
        self.text = text.upper().replace(' ', '')
        self.key = key

    def _encode(self, msg, a=1, b=0):
        '''
        common encode function
        '''
        return ''.join([ chr((( (a*(ord(t) - ord('A')) + b)) % 26) + ord('A')) for t in msg ])

    def _decode(self, cipher, a=1, b=0):
        '''
        common decode function
        '''
        return ''.join([ chr((( modinv(a, 26)*(ord(c) - ord('A') - b) ) % 26) + ord('A')) for c in cipher ])

    def shift_encrypt(self):
        '''
        C = (P + K) % 26
        '''
        return self._encode(self.text, b=self.key)

    def shift_decrypt(self, cipher):
        '''
        P = (C - K) % 26
        '''
        return self._decode(cipher, b=self.key)

    def multiplicative_encrypt(self):
        '''
        C = (P * K) % 26
        '''
        return self._encode(self.text, a=self.key)

    def multiplicative_decrypt(self, cipher):
        '''
        P = (C * K^-1) % 26
        '''
        return self._decode(cipher, a=self.key)

    def affine_encrypt(self):
        '''
        C = (a*P + b) % 26
        '''
        return self._encode(self.text, a=self.key[0], b=self.key[1])

    def affine_decrypt(self, cipher):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        return self._decode(cipher, a=self.key[0], b=self.key[1])

    def encrypt_vignere(self):
        '''
        Ci = (Pi + Ki) mod 26
        '''
        return ''.join([chr(((ord(a)-ord('A')) + (ord(b)-ord('A'))) % 26 + ord('A')) for a,b in zip(self.text, itertools.cycle(self.key))])

    def decrypt_vignere(self, cipher):
        '''
        Pi = (Ci - Ki + 26) mod 26
        '''
        return ''.join([chr(((ord(a)-ord('A')) - (ord(b)-ord('A')) + 26) % 26 + ord('A')) for a,b in zip(cipher, itertools.cycle(self.key))])


def main():
    text = 'twenty fifteen'
    ciphers = Ciphers(text, 5)

    #------------ Additive or Shift Cipher -------------#

    shift_encrypt_text = ciphers.shift_encrypt()
    print('Additive Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(shift_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.shift_decrypt(shift_encrypt_text) ))

    #---------- Additive or Shift Cipher Ends ----------#


    #------------ Multiplicative Cipher -------------#

    multiplicative_encrypt_text = ciphers.multiplicative_encrypt()
    print('Multiplicative Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(multiplicative_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.multiplicative_decrypt(multiplicative_encrypt_text) ))

    #---------- Multiplicative Cipher Ends ----------#

    #------------ Affine Cipher -----------#

    affine_cipher = Ciphers(text, [17, 20])
    affine_encrypted_text = affine_cipher.affine_encrypt()
    print('Affine Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print('Decrypted Text: {}\n'.format( affine_cipher.affine_decrypt(affine_encrypted_text) ))

    #--------- Affine Cipher Ends ---------#

    #----------- Vignere Cipher ------------#
    vignere = Ciphers(text, 'apex')
    vignere_encrypted_text = vignere.encrypt_vignere()
    print('Vignere Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(vignere_encrypted_text))
    print('Decrypted Text: {}'.format( vignere.decrypt_vignere(vignere_encrypted_text) ))
    #---------- Vignere Cipher Ends --------#


if __name__ == '__main__':
    main()