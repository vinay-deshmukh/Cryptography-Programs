q = 29 # large prime
a = 3  # primitive root

alice_x = 7
darth_xa = 11

print(f'Alice\'s private key             : {alice_x}')
print(f'Darths\'s private key (for Alice):{darth_xa}')
print()

bob_x = 5
darth_xb = 9
print(f'Bob\'s private key            : {bob_x}')
print(f'Darth\'s private key (for Bob): {darth_xb}')
print()


alice_y = pow(a, alice_x, q)
darth_ya = pow(a, darth_xa, q)
print(f'Alice\'s public key            : {alice_y}')
print(f'Darth\'s public key (for Alice): {darth_ya}')
print()

bob_y = pow(a, bob_x, q)
darth_yb = pow(a, darth_xb, q)
print(f'Bob\'s public key            : {bob_y}')
print(f'Darth\'s public key (for Bob): {darth_yb}')
print()



alice_k = pow(darth_ya, alice_x, q)
darth_ka = pow(alice_y, darth_xa, q)
print(f'Alice calculates key from Darth\'s public key for Bob: {alice_k}')
print(f'Darth calculates his key for Alice                  : {darth_ka}')
print()

bob_k = pow(darth_yb, bob_x, q)
darth_kb = pow(bob_y, darth_xb, q)
print(f'Bob calculates key from Darth\'s public key for Alice: {bob_k}')
print(f'Darth calculates his key for Bob                    : {darth_kb}')
print()

'''
Output:
Alice's private key             : 7
Darths's private key (for Alice):11

Bob's private key            : 5
Darth's private key (for Bob): 9

Alice's public key            : 12
Darth's public key (for Alice): 15

Bob's public key            : 11
Darth's public key (for Bob): 21

Alice calculates key from Darth's public key for Bob: 17
Darth calculates his key for Alice                  : 17

Bob calculates key from Darth's public key for Alice: 2
Darth calculates his key for Bob                    : 2
'''