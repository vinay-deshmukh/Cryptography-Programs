import string


def get_pairs_of_text(text):
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        try:
            b = text[i+1]
        except Exception as e:
            pairs.append((a, 'X'))
            break

        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs


def get_index(k, key):
    for i in range(5):
        for j in range(5):
            if key[i][j] == k:
                return i, j


def find_new_pairs(pair, key, encrypt):
    a, b = pair
    ai, aj = get_index(a, key)
    bi, bj = get_index(b, key)

    if ai == bi:
        if encrypt: # move right
            aj = (aj + 1) % 5
            bj = (bj + 1) % 5
        else: # move left
            aj = (aj - 1) % 5
            bj = (bj - 1) % 5
    elif aj == bj:
        if encrypt: # move down
            ai = (ai + 1) % 5
            bi = (bi + 1) % 5
        else: # move up
            ai = (ai - 1) % 5
            bi = (bi - 1) % 5
    else:
        aj, bj = bj, aj

    return (key[ai][aj], key[bi][bj])


def encrypt(text, key):
    pairs = get_pairs_of_text(text)
    new_pairs = []
    for pair in pairs:
        new_pairs.append(find_new_pairs(pair, key, encrypt=True))
    return ''.join(a+b for a, b in new_pairs)


def decrypt(text, key):
    pairs = get_pairs_of_text(text)
    new_pairs = []
    for pair in pairs:
        new_pairs.append(find_new_pairs(pair, key, encrypt=False))
    return ''.join(a+b for a, b in new_pairs).replace('X', '')


def create_key(key):
    all_elements = []
    elements = list(key + string.ascii_uppercase.replace('J', ''))
    for el in elements:
        if not el in all_elements:
            all_elements.append(el)

    KEY = []
    for i in range(0, 25, 5):
        KEY.append(all_elements[i:i+5])

    return KEY


def playfair(text, key):
    print('Original Text: ', text)
    enc = encrypt(text, key=key)
    print('Encrypted Text: ', enc)
    dec = decrypt(enc, key=key)
    print('Decrypted Text: ', dec)


if __name__ == '__main__':
    text = 'BALLOON'
    key = 'BALLOON'
    playfair(text, key=create_key(key))
