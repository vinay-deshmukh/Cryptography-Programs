def encode(string):
    return string[0::2] + string[1::2]

def decode(string):
    mid = len(string) // 2
    return string[:mid] + string[mid:]

msg = "something"

e = encode(msg)
d = decode(msg)

print("encoded:", e)
print("decoded:", d)
