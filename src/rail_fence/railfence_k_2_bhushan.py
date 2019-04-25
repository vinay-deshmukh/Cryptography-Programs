text = "ABCD"
n = len(text)

# encrypting
enc = ''.join(text[i::2] for i in range(2))
print("Encrypted: ", enc)

# this is the index after which the second row will start
id1 = -(-n//2)        # taking ceil of number.

l1, l2 = enc[:id1], enc[id1:]

print("".join( sum( zip(l1, l2), () ) ))
print(l1[-1] if n & 1 else "")
