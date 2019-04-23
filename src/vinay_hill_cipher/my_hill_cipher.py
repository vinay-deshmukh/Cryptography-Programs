from math import sqrt
DEBUG = False
debug_print = print if DEBUG else lambda *x,**y: None

import string
ord = string.ascii_uppercase.index
chr = string.ascii_uppercase.__getitem__

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
        return None # modular inverse does not exist
    else:
        return x % m

class Matrix:
    def __init__(self, contents, r, c):
        contents = list(contents)
        assert len(contents) == r * c

        # underlying 2d list which contains the elements
        self._mat = [[0 for ci in range(c)] for ri in range(r)]
        self.r, self.c = r, c
        for ri in range(r):
            for ci in range(c):
                self._mat[ri][ci] = contents[ri * c + ci]

    def __repr__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self._mat)

    def __mul__(self, mat2):
        # override multiply operator
        mat1 = self
        mat2 = mat2

        assert mat1.c == mat2.r, 'Matrices can\'t be multiplied'
        result = Matrix(range(mat1.r * mat2.c), mat1.r, mat2.c)

        m1, m2 = mat1._mat, mat2._mat
        for r1 in range(mat1.r):
            for c2 in range(mat2.c):
                result._mat[r1][c2] = sum(m1[r1][k] * m2[k][c2]  for k in range(mat2.r))
        return result

    def __eq__(self, mat2):
        return ( self._mat == mat2._mat and self.r == mat2.r and self.c == mat2.c)

    def same_shape(self):
        # return a new Matrix object with same shape
        # this matrix's contents are not same as `self`
        return Matrix(range(self.r * self.c), self.r, self.c)

    def mod_number(self, num):
        # Return new Matrix object
        # which is obtained by modding `self` with `num`
        ans = self.same_shape()
        for ri in range(ans.r):
            for ci in range(ans.c):
                ans._mat[ri][ci] = self._mat[ri][ci] % num
        return ans

class SquareMatrix(Matrix):
    def __init__(self, d1_list, m):
        d1_list = list(d1_list)
        assert len(d1_list) == m * m
        super().__init__(d1_list, m, m)
        self.m = m # m is the `r` or `c` value of current square matrix

    def same_shape(self):
        # return a new SquareMatrix object with same shape
        # this matrix's contents are not same as `self`
        return SquareMatrix(range(self.m * self.m), self.m)

    def mul_number(self, num):
        # return new SquaredMatrix object
        # which is obtained by multiplying `self` with `num`
        ans = self.same_shape()
        for ri in range(ans.r):
            for ci in range(ans.c):
                ans._mat[ri][ci] = round(num * self._mat[ri][ci], 3)
        return ans

    def inverse(self):
        # Returns the inverse of this matrix
        # Reference: https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
        
        # Get determinant
        det = self.determinant()
        if det == 0: raise ValueError('Inverse of singular matrix doesn\'t exist!')

        # Get minor matrix
        minor_matrix = self._minor_matrix()

        # Get cofactor matrix
        cofactor_matrix = self._cofactor_matrix(minor_matrix=minor_matrix)

        # Get adjugate matrix
        adjugate_matrix = cofactor_matrix.transpose()

        # Get inverse
        det = modinv(det%26, 26)
        if det is None: raise ValueError('det is None')
        inverse = adjugate_matrix.mul_number(det)

        return inverse

    def transpose(self):
        # Return transpose SquaredMatrix of self
        ans = self.same_shape()
        for ri in range(ans.r):
            for ci in range(ans.c):
                ans._mat[ci][ri] = self._mat[ri][ci]
        return ans

    def determinant(self):
        # return the determinant of matrix
        # returns a number
        if self.m == 1: return self._mat[0][0]
        if self.m == 2: 
            return (  self._mat[0][0] * self._mat[1][1]
                    - self._mat[0][1] * self._mat[1][0] )
        else:
            # generic case
            ans = 0
            sign = +1
            for ci in range(self.c):
                # for each element in first row, calculate determinant of sliced matrix
                ans += sign * self._mat[0][ci] * self._get_slice(0, ci).determinant()
                sign = -sign
            return ans

    def _minor_matrix(self):
        # return the minor matrix
        minors = self.same_shape()
        for ri in range(minors.r):
            for ci in range(minors.c):
                minors._mat[ri][ci] = self._get_slice(ri, ci).determinant()
        return minors

    def _cofactor_matrix(self, minor_matrix):
        # Apply + - to minor matrix, inplace
        for ri in range(minor_matrix.r):
            for ci in range(minor_matrix.c):
                minor_matrix._mat[ri][ci] *= (-1) ** (ri+ci)
        return minor_matrix

    def _get_slice(self, r_, c_):
        # Get slice of matrix without the `r_` row, and `c_` column
        # where r_ can be from 0 to (self.r-1)
        # where c_ can be from 0 to (self.c-1)

        # Slice of matrix will be (r_ - 1) X (c_ - 1)
        # Create SquareMatrix object of that size
        m_1 = self.m - 1 # m - 1
        ans = SquareMatrix(range(m_1*m_1), m_1)

        for ri in range(self.m):
            for ci in range(self.m):
                if ri == r_ or ci == c_:
                    # skip the specified row and column
                    continue

                # When inserting the elements from current matrix 
                # to sliced matrix
                # if index is less than `r_`, we can directly insert
                # if index is greater than `r_`,
                # we have to shift it to one place left ie `r1_1`
                if ri < r_: r_insert = ri
                else      : r_insert = ri - 1
                if ci < c_: c_insert = ci
                else      : c_insert = ci - 1

                ans._mat[r_insert][c_insert] = self._mat[ri][ci]
        return ans


class HillCipher:
    BLANK = 'X'
    def __init__(self, key):
        self.key = key

        sqr, si = 1 , 1
        while len(self.key) > sqr:
            si += 1
            sqr = si * si

        # m is order of matrix
        self.m = int(sqrt(sqr))
        debug_print(f'Key Matrix: {self.m}x{self.m}')

        # Pad key string
        while len(self.key) != self.m * self.m:
            self.key += self.BLANK
        
        self.keym = SquareMatrix(
            d1_list=map(ord, self.key), # send the ord values to matrix
            m=self.m
            )
        debug_print('Key Matrix', self.keym, sep='\n')
        debug_print('Key Matrix Determinant', self.keym.determinant(), sep='\n')
        debug_print('Key Matrix Inverse', self.keym.inverse(), sep='\n')

    def _create_nxm_matrix(self, ins):
        '''
        Takes input string `ins` converts it to a 
        n x `m` matrix, where m is order of key matrix
        '''
        while len(ins) % self.m != 0:
            ins += self.BLANK
        n = len(ins) // self.m
        mat = Matrix(map(ord, ins), r=n, c=self.m)
        return mat

    def encrypt(self, pt):
        pt_mat = self._create_nxm_matrix(pt)
        debug_print('Pt matrix:')
        debug_print(repr(pt_mat))

        encrypted_mat = (pt_mat * self.keym)
        debug_print('After multiply:')
        debug_print(encrypted_mat)

        encrypted_mat = encrypted_mat.mod_number(26)
        debug_print('after mod')
        debug_print(encrypted_mat)
        
        debug_print('Enc matrix:')
        debug_print(repr(encrypted_mat))

        # Get 1d string from matrix
        enc_str = ''.join(''.join(map(chr, row)) for row in encrypted_mat._mat)
        return enc_str


    def decrypt(self, ct):
        ct_mat = self._create_nxm_matrix(ct)
        debug_print('Ct matrix:')
        debug_print(repr(ct_mat))

        decrypted_mat = (ct_mat * self.keym.inverse())
        debug_print('After inverse multiply')
        debug_print(decrypted_mat)
        decrypted_mat = decrypted_mat.mod_number(26)
        debug_print('After mod')
        debug_print(decrypted_mat)

        debug_print('Dec matrix:')
        debug_print(repr(decrypted_mat))

        # Get 1d string from matrix
        dec_str = ''.join(''.join(map(chr, row)) for row in decrypted_mat._mat)
        return dec_str

if __name__ == '__main__':

    inp = 'PAYMOREMONEY'
    key = ''.join(map(chr, [17,17,5,  21,18,21,  2,2,19]))

    h = HillCipher(key=key)
    enc = h.encrypt(inp)
    dec = h.decrypt(enc)

    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    print('Input == Decrypted ?', inp == dec)
    assert inp == dec, 'Input != Decrypted'