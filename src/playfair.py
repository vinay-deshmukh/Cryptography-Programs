import string
DEBUG = False
debug_print = print if DEBUG else lambda *x: None

class PlayFair():
    NULL = 'X'
    def __init__(self, key):
        # key is list of strings
        self.key = key
        oneline = []

        list_alphas = self.key + string.ascii_uppercase.replace('J', '')

        for a in list_alphas:
            if not a in oneline:
                oneline.append(a)

        # use 1d list to implement matrix
        self.line = oneline

    def __repr__(self):
        ans = []
        for i in range(0, 26, 5):
            ans.append( self.line[i:i+5] )
        mat = '\n'.join( ' '.join(row) for row in ans )
        return f'Key={repr(self.key)}, \n' + mat

    def _rc(self, i):
        # get r,c tuple from index i
        r, c = i//5, i % 5
        return r, c
    def _i(self, rc):
        # get index i from r,c tuple
        r, c = rc
        i = (r % 5) * 5 + c % 5
        return i
        
    def _mapper(self, a, b, encrypt=True):
        # a = first letter in pair
        # b = second letter in pair
        # encrypt = bool which decides if we are encrypting or decrypting
        # returns pair of letters (2-tuple)

        ai, bi = self.line.index(a), self.line.index(b)
        
        # arc, brc is 2-tuple with (row, col)
        arc, brc = self._rc(ai), self._rc(bi)
        
        # make list so we can modify inplace
        arc, brc = list(arc), list(brc)

        # after this if else, arc, brc will contain output indexes
        if arc[0] == brc[0]:
            # if same row
            if encrypt:
                arc[1] = (arc[1] + 1) % 5 # move right once
                brc[1] = (brc[1] + 1) % 5 # and wrap around
            else:
                arc[1] = (arc[1] - 1) % 5 # move left once
                brc[1] = (brc[1] - 1) % 5 # and wrap around
            
        elif arc[1] == brc[1]:
            # if same column
            if encrypt:
                arc[0] = (arc[0] + 1) % 5 # move down once
                brc[0] = (brc[0] + 1) % 5 # and wrap around
            else:
                arc[0] = (arc[0] - 1) % 5 # move up once
                brc[0] = (brc[0] - 1) % 5 # and wrap around
        else:
            # third case
            arc[1], brc[1] = brc[1], arc[1]
        
        ci, di = self._i(arc), self._i(brc)
        c, d = self.line[ci], self.line[di]
        return c, d

    def _preprocess(self, pt):
        debug_print('Before preprocess:', pt)
        pi = 0
        pairs = [] # contains 2 chars

        while pi < len(pt):
            a = pt[pi]
            try:
                b = pt[pi+1]
            except IndexError:
                # if str is odd length, pt[pi+1] triggers this
                # so add NULL, and end preprocessing here
                pairs.append( a + self.NULL )
                break

            if a == b:
                pairs.append( a + self.NULL ) 
                pi += 1
            else:
                pairs.append( a + b )
                pi += 2
        
        str_pair = ''.join(p for p in pairs)
        debug_print('After  preprocess:', str_pair)
        return str_pair

    def _playfair(self, inp, encrypt=True):
        # inp = input string
        # encrypt = bool for encrypting/decrypting
        # returns output string after applying _mapper

        ans = [] # contains 2char
        for ii in range(0, len(inp), 2):
            a, b = inp[ii], inp[ii+1]
            c, d = self._mapper(a, b, encrypt=encrypt)
            ans.append( c + d )
        return ''.join(ans)

    def encrypt(self, pt):
        pt = self._preprocess(pt)
        out = self._playfair(inp=pt, encrypt=True)
        return out

    def decrypt(self, ct):
        assert len(ct) % 2 == 0, 'Enc string should be even in length'

        out = self._playfair(inp=ct, encrypt=False)
        return out.replace(self.NULL, '')

def get_2char(s):
    # return string as 2char pairs separated by space
    ans = []
    for i in range(0, len(s), 2):
        try: x = s[i+1]
        except IndexError: x = ''
        ans.append( s[i] + x )
    return ' '.join(ans)

if __name__ == '__main__':
    p = PlayFair(key='PLAYFAIREXAMPLE')
    print(p)
    inp = 'Hide the gold in the tree stump'.replace(' ', '').upper()
    print('Input:', get_2char(inp))
    enc = p.encrypt(inp)
    print('Enc  :', get_2char(enc))
    dec = p.decrypt(enc)
    print('Dec  :', get_2char(dec))
    print('Input == Decrypted ?', inp == dec)
    assert inp == dec, 'Input != Decrypted'

    
