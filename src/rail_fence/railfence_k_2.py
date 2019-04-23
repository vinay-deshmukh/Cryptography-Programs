import math

text = "ABCD"
len_input = len(text)

# encrypting
l = [text[i::2] for i in range(2)]
enc = ''.join(l)
print("Encrypted: ", enc)

# this is the index after which the second row will start
id1 = math.ceil(len(text)/2)

l1, l2 = enc[:id1], enc[id1:]

for i, m in zip(l1, l2):
    print(i + m, end='')

if len_input % 2 != 0:
	print(l1[-1])