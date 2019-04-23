
q = 29 # large prime
a = 4 # primitive root of prime number, q

xa, xb = 7, 11 # private keys of A,B
ya, yb = pow(a, xa, q), pow(a, xb, q)
ka, kb = pow(yb, xa, q), pow(ya, xb, q)

print(f'Large Prime     : {q}')
print(f'Primitive Root  : {a}')
print(f'Private Key of A: {xa}')
print(f'Private Key of B: {xb}')
print(f'Public key of A : {ya}')
print(f'Public key of B : {yb}')
print(f'Key created by A: {ka}')
print(f'Key created by B: {kb}')
assert ka == kb, 'Diffie Hellman failed!'
