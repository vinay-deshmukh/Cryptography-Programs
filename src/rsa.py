
def get_ned(p, q):
    # Assume p, q are primes
    n = p * q
    totient = (p-1) * (q-1)
    e = totient - 1 # e and totient are co prime
    
    # congruence relation
    d = modinv(e, totient)
    assert d is not None, 'Mod. inverse doesn\'t exist'
    
    # n is modulus, e is public, d is private
    return n, e, d

def rsa_encrypt(msg, e, n):
    return _pow_str(msg, e, n)
    
def rsa_decrypt(msg, d, n):
    return _pow_str(msg, d, n)

def _pow_str(msg, exp, mod):
    return ''.join( chr( pow(ord(c), exp, mod) ) for c in msg)


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

if __name__ == '__main__':
    inp = 'Hide the gold in the tree stump'
    
    n, e, d = get_ned(17, 31)
    enc = rsa_encrypt(inp, e=e, n=n)
    dec = rsa_decrypt(enc, d=d, n=n)
    
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    print('Input == Decrypted ?', inp == dec)
    assert inp == dec, 'Input != Decrypted'