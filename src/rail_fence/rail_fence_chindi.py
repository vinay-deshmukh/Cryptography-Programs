def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]   # memory inefficient.
    rails = [*range(0, numrails - 1), *range(numrails - 1, 0, -1)]  # sawtooth.
    for n, x in enumerate(lst): fence[rails[n % len(rails)]][n] = x
    return [j for i in fence for j in i if j is not None]
    return [c for c in sum(fence, []) if c is not None]

def encode(text, n):
    return ''.join(fence(text, n))

def decode(text, n):
    pos = fence(range(len(text)), n)
    return ''.join(text[pos.index(n)] for n in range(len(text)))
