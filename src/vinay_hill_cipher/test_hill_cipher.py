from my_hill_cipher import *
DEBUG = True
debug_print = print if DEBUG else lambda *x,**y: None


# @staticmethod
def test_identity():
    mat1 = Matrix(range(9), 3, 3)
    mat2 = Matrix([1,0,0,0,1,0,0,0,1], 3, 3)
    ans = mat1 * mat2
    assert mat1 == ans, 'Identity property failed!'
    debug_print('Matrix.test_identity passed!')

# @staticmethod
def test_multiply():
    # https://en.wikipedia.org/wiki/Hill_cipher
    m1 = Matrix([6,24,1,  13,16,10,  20,17,15], 3, 3)
    m2 = Matrix([0,2,19], 3,1)
    ans = Matrix([67,222,319], 3, 1)
    assert ans == m1*m2, 'test_multiply not working'
    debug_print('Matrix.test_multiply passed')

# @staticmethod
def test_determinant():
    a = SquareMatrix([2, 3, 4, 5], 2)
    assert a.determinant() == -2, 'determinant m=2 doesn\'t work'

    # https://www.mathsisfun.com/algebra/matrix-determinant.html
    a = SquareMatrix([6,1,1, 4,-2,5, 2,8,7], 3)
    assert a.determinant() == -306, 'determinant m=3 doesn\'t work'
    debug_print('SquareMatrix.test_determinant passed')

# @staticmethod
def test_slicing():
    a3 = SquareMatrix([1,0,0, 0,1,0, 0,0,1], 3)
    a2 = SquareMatrix([1,0, 0,1], 2)
    b = a3._get_slice(2, 2)
    assert b == a2, 'slicing 1 not working'

    a2 = SquareMatrix([1,0, 0,0], 2)
    b = a3._get_slice(2, 1)
    assert b == a2, 'slicing 2 not working'
    debug_print('SquareMatrix.test_slicing passed!')

# @staticmethod
def test_minors():
    # https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
    a = SquareMatrix([3,0,2, 2,0,-2, 0,1,1], 3)
    ans = SquareMatrix([2,2,2, -2,3,3, 0,-10,0], 3)
    assert ans == a._minor_matrix(), 'minors not working'
    debug_print('SquareMatrix.test_minors passed')

# @staticmethod
def test_cofactors():
    # https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
    minors = SquareMatrix([2,2,2, -2,3,3, 0,-10,0], 3)
    cofactors = SquareMatrix([2,-2,2, +2,3,-3, 0,+10,0], 3)
    assert cofactors == minors._cofactor_matrix(minor_matrix=minors), 'cofactors not working'
    debug_print('SquareMatrix.test_cofactors passed')

# @staticmethod
def test_transpose():
    a = SquareMatrix([2,-2,2, +2,3,-3, 0,+10,0], 3)
    ans = SquareMatrix([2,2,0, -2,3,+10, 2,-3,0], 3)
    assert ans == a.transpose(), 'test_transpose not working'
    debug_print('SquareMatrix.test_transpose passed')

# @staticmethod
def test_mul_number():
    a = SquareMatrix([1,2, 3,4], 2)
    num = 2
    ans = SquareMatrix([2,4, 6,8], 2)
    assert ans == a.mul_number(2), 'test_mul_number not working'
    debug_print('SquareMatrix.test_mul_number passed')

# @staticmethod
def test_inverse():
    # https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
    # a = SquareMatrix([3,0,2, 2,0,-2, 0,1,1], 3)
    # inverse = SquareMatrix([ 2/10,  2/10, 0/10,
    #                         -2/10,  3/10, 10/10,
    #                          2/10, -3/10,  0/10
    #                     ], 3)
    # assert inverse == a.inverse(), 'test_inverse not working'
    # debug_print('SquareMatrix.test_inverse passed')

    # CANT USE THIS TEST SINCE WE ARE NOT FINDING TRUE determinant^-1
    # we are finding modinv(det, 26)
    

    # test for actual multiplicative inverse matrix
    key = SquareMatrix([17,17,5,  21,18,21,  2,2,19], 3)
    key_1 = SquareMatrix([4,9,15,  15,17,6,  24,0,17], 3)

    assert key.inverse().mod_number(26) == key_1, 'test_inverse not working'
    debug_print('SquareMatrix.test_inverse passed')


# @staticmethod
def test_mod_number():
    a = SquareMatrix([50,51, 52,53], 2)
    ans = SquareMatrix([0,1, 2,3], 2)
    # print('a', a, sep='\n')
    # print('sqr', make_square(a), sep='\n')
    assert ans == a.mod_number(50), 'test_mod_number not working'
    debug_print('SquareMatrix.test_mod_number passed')
def run_tests():
    test_identity()
    test_multiply()
    test_determinant()
    test_slicing()
    test_minors()
    test_cofactors()
    test_transpose()
    test_mul_number()
    test_inverse()
    test_mod_number()

if __name__ == '__main__':
    run_tests()
