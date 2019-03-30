import string

# Restrict ord(), chr() to only ascii_uppercase
# Allows us to directly get  ord('A') = 0, chr(0) = 'A', etc
ord = string.ascii_uppercase.index
chr = string.ascii_uppercase.__getitem__

def _add(msg, add=0):
    # Add `add` to each char of string and mod 26
    # Return modified string
    return ''.join( chr( (ord(c) + add) % 26 ) for c in msg )

def _mul(msg, mul=1):
    # Multiply `mul` with each char of string and mod 26
    # Return modified string
    return ''.join( chr( (ord(c) * mul) % 26 ) for c in msg )

def shift_encrypt(msg, key):
    # C = P + key
    return _add(msg, add=key)

def shift_decrypt(msg, key):
    # P = C - key
    return _add(msg, add=-key)

def mul_encrypt(msg, key):
    # C = P * key
    return _mul(msg, mul=key)

def mul_decrypt(msg, key):
    # P = C * key^-1
    return _mul(msg, mul=modinv(key, 26))

def affine_encrypt(msg, mul, add):
    # C = (mul * P) + add
    return _add( _mul(msg, mul), add )

def affine_decrypt(msg, mul, add):
    # P = (C - add) * (mul)^-1
    return _mul( _add(msg, -add), modinv(mul, 26))

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
    inp = 'ABCD' * 5

    print('\nAffine cipher:')
    enc = affine_encrypt(inp, 5, 8)
    dec = affine_decrypt(enc, 5, 8)
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    assert inp == dec

    print('\nMultiplicative cipher')
    enc = mul_encrypt(inp, 5)
    dec = mul_decrypt(enc, 5)
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    assert inp == dec

    print('\nAdditive cipher / Shift Cipher / Caesar cipher')
    enc = shift_encrypt(inp, 3)
    dec = shift_decrypt(enc, 3)
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    assert inp == dec

    
