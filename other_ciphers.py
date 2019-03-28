class Ciphers:
    def __init__(self, text, key=3):
        self.text = text
        self.key = key

    def _egcd(self, a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y

    def _modinv(self, a, m):
        gcd, x, y = self._egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def shift_encrypt(self):
        '''
        C = (P + K) % 26
        '''
        return ''.join([ chr(((ord(t) - ord('A') + self.key) % 26) + ord('A')) for t in self.text.upper().replace(' ', '') ])

    def shift_decrypt(self, cipher):
        '''
        P = (C - K) % 26
        '''
        return ''.join([ chr(((ord(c) - ord('A') - self.key) % 26) + ord('A')) for c in cipher ])

    def multiplicative_encrypt(self):
        '''
        C = (P * K) % 26
        '''
        return ''.join([ chr((((ord(t) - ord('A')) * self.key) % 26) + ord('A')) for t in self.text.upper().replace(' ', '') ])

    def multiplicative_decrypt(self, cipher):
        '''
        P = (C * K^-1) % 26
        '''
        return ''.join([ chr((((ord(c) - ord('A')) * self._modinv(self.key, 26)) % 26) + ord('A')) for c in cipher ])

    def affine_encrypt(self):
        '''
        C = (a*P + b) % 26
        '''
        return ''.join([ chr((( self.key[0]*(ord(t) - ord('A')) + self.key[1] ) % 26) + ord('A')) for t in self.text.upper().replace(' ', '') ])

    def affine_decrypt(self, cipher):
        '''
        P = (a^-1 * (C - b)) % 26
        '''
        return ''.join([ chr((( self._modinv(self.key[0], 26)*(ord(c) - ord('A') - self.key[1]) ) % 26) + ord('A')) for c in cipher ])


def main():
    text = 'twenty fifteen'
    ciphers = Ciphers(text, 5)

    #------------ Additive or Shift Cipher -------------#

    shift_encrypt_text = ciphers.shift_encrypt()
    print('Additive Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(shift_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.shift_decrypt(shift_encrypt_text )))

    #---------- Additive or Shift Cipher Ends ----------#


    #------------ Multiplicative Cipher -------------#

    multiplicative_encrypt_text = ciphers.multiplicative_encrypt()
    print('Multiplicative Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format(multiplicative_encrypt_text))
    print('Decrypted Text: {}\n'.format( ciphers.multiplicative_decrypt(multiplicative_encrypt_text )))

    #---------- Multiplicative Cipher Ends ----------#

    #------------ Affine Cipher -----------#

    affine_cipher = Ciphers('twenty fifteen', [17, 20])
    affine_encrypted_text = affine_cipher.affine_encrypt()
    print('Affine Cipher: ')
    print('Original Text: {}'.format(text))
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
    print('Decrypted Text: {}'.format( affine_cipher.affine_decrypt(affine_encrypted_text) ))

    #--------- Affine Cipher Ends ---------#


if __name__ == '__main__':
    main()