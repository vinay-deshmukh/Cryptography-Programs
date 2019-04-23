
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

'''
Output:
Large Prime     : 29
Primitive Root  : 4
Private Key of A: 7
Private Key of B: 11
Public key of A : 28
Public key of B : 5
Key created by A: 28
Key created by B: 28
'''