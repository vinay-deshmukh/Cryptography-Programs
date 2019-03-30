from utils import shift_char, modinv


class Ciphers:
    def __init__(self, key=3):  # 3 is for vignere's i think.
        self.key = key

    def affine_encrypt(self, msg, m=1, c=0):
        '''
        C = (m*P + c) % 26
        '''
        return ''.join([ chr((( (m*(ord(t) - ord('A')) + c)) % 26) + ord('A')) for t in msg ])

    def affine_decrypt(self, cipher, m=1, c=0):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        return ''.join([ chr((( modinv(m, 26)*(ord(_) - ord('A') - c) ) % 26) + ord('A')) for _ in cipher ])

    def shift_encrypt(self, text):
        '''
        C = (P + K) % 26
        '''
        return self.affine_encrypt(text, c=self.key)

    def shift_decrypt(self, cipher):
        '''
        P = (C - K) % 26
        '''
        return self.affine_decrypt(cipher, c=self.key)

    def multiplicative_encrypt(self, text):
        '''
        C = (P * K) % 26
        '''
        return self.affine_encrypt(text, m=self.key)

    def multiplicative_decrypt(self, cipher):
        '''
        P = (C * K^-1) % 26
        '''
        return self.affine_decrypt(cipher, m=self.key)


    def encrypt_vignere(self, text):
        '''
        Ci = (Pi + Ki) mod 26
        '''
        if len(self.key) != len(text):
            self.key += ''.join([ self.key[i % len(self.key)] for i in range(len(text) - len(self.key)) ])

        elif len(self.key) > len(text):
            self.key = text[:len(self.key)]

        return ''.join([chr(((ord(a)-ord('A')) + (ord(b)-ord('A'))) % 26 + ord('A')) for a,b in zip(text, self.key)])

    def decrypt_vignere(self, cipher):
        '''
        Pi = (Ci - Ki + 26) mod 26
        '''
        return ''.join([chr(((ord(a)-ord('A')) - (ord(b)-ord('A')) + 26) % 26 + ord('A')) for a,b in zip(cipher, self.key)])


def main():
    text = 'twenty fifteen'
    ciphers = Ciphers(5)

    #------------ Additive or Shift Cipher -------------#

    shift_encrypt_text = ciphers.shift_encrypt(text)
    print('Additive Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(shift_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.shift_decrypt(shift_encrypt_text) ))

    #---------- Additive or Shift Cipher Ends ----------#


    #------------ Multiplicative Cipher -------------#

    multiplicative_encrypt_text = ciphers.multiplicative_encrypt(text)
    print('Multiplicative Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(multiplicative_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.multiplicative_decrypt(multiplicative_encrypt_text) ))

    #---------- Multiplicative Cipher Ends ----------#

    #------------ Affine Cipher -----------#

    affine_cipher = Ciphers([17, 20])
    affine_encrypted_text = affine_cipher.affine_encrypt(text)
    print('Affine Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print('Decrypted Text: {}\n'.format( affine_cipher.affine_decrypt(affine_encrypted_text) ))

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
