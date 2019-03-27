import math
debug_print = print


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


def transpose_matrix(m):
	return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def get_matrix_minor(m,i,j):
	return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_matrix_deternminant(m):
	# Base case for 2x2 matrix
	if len(m) == 2:
		return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])

	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c)*m[0][c]*get_matrix_deternminant(get_matrix_minor(m,0,c))
	return determinant


def get_adjoint_matrix(m):
	determinant = get_matrix_deternminant(m)

	#special case for 2x2 matrix:
	if len(m) == 2:
		m = [[m[1][1], -1*m[0][1]], [-1*m[1][0], m[0][0]]]
		return m

	#find matrix of cofactors
	cofactors = []
	for r in range(len(m)):
		cofactorRow = []
		for c in range(len(m)):
			minor = get_matrix_minor(m,r,c)
			cofactorRow.append(((-1)**(r+c)) * get_matrix_deternminant(minor))
		cofactors.append(cofactorRow)
	cofactors = transpose_matrix(cofactors)
	return cofactors


def print_matrix(matrix):
	'''
	Prints the matrix in a tabular format
	'''
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))


def multiply_matrices(m1, m2):
	result = [[0 for col in range(len(m2[0]))] for row in range(len(m1))]
	
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m2)):
				result[i][j] += m1[i][k] * m2[k][j]
	
	return result


def is_perfect_square(x): 
	'''
	Find floating point value of  
	square root of x. 
	'''
	sr = math.sqrt(x) 
   
	# If square root is an integer 
	return ((sr - math.floor(sr)) == 0) 


def next_perfect_square(n):
	'''
	Finds the next perfect sqaure for the given number
	'''
	nextN = math.floor(math.sqrt(n)) + 1
  
	return nextN **2


def encryption(m):
	'''
	Encrypting the plain text matrix
	'''
	return [[chr(col + 65) for col in row] for row in m]


def decryption(m):
	'''
	Decrypting the plain text matrix
	'''
	return [[chr(col%26 + 65) for col in row] for row in m]

def matrix_mod(m):
	return [[col%26 for col in row] for row in m]


def hill_cipher(text, key):

	n = int(math.sqrt(len(key)))
	'''
	Consider Text: ZXCVB
	Key : H  I  L
	      Z  M  N
	      V  C  X
	Therefore text matrix will be: Z X C
	                               V B X
	                               (here extra dummy character 'X' is added since it does not fit the matrix)
	'''
	num_X = 0 if len(text)%n == 0 else n-len(text)%n
	text += 'X' * num_X

	# convert key and plain text into its ord
	key = [ord(k) - ord('A') for k in key]
	text = [ord(k) - ord('A') for k in text]

	# initialize the key matrix
	key_matrix = []

	# create key matrix
	for i in range(0, len(key), n):
		key_matrix.append(list(key[i : i+n]))

	debug_print('Key Matrix: ')
	print_matrix(key_matrix)

	# initialize the plain_text matrix
	text_matrix = []

	# creating plain_text matrix
	for i in range(0, len(text), n):
		text_matrix.append(list(text[i : i+n]))

	#debug_print('Plain Text Matrix: ')
	#print_matrix(text_matrix)

	# Encryption
	result = matrix_mod(multiply_matrices(text_matrix, key_matrix))

	#debug_print('Cipher Text Matrix: ')
	cipher = encryption(result)
	#print_matrix(cipher)

	flattened_cipher_text = [item for sublist in cipher for item in sublist]
	print('Cipher Text: {}'.format(''.join(flattened_cipher_text)))

	# Decryption
	mat_adj = matrix_mod(get_adjoint_matrix(key_matrix))

	inverse_factor = modinv(get_matrix_deternminant(key_matrix) % 26, 26)

	# multiplying the adjoint matrix by the inverse factor to get the matrix inverse
	mat_inv = [[inverse_factor*col for col in row] for row in mat_adj]
	
	result = multiply_matrices(result, mat_inv)
	plain_text = decryption(result)

	#debug_print('Plain Text Matrix after Decryption: ')
	#print_matrix(plain_text)

	flattened_plain_text = [item for sublist in plain_text for item in sublist]
	plain_text = ''.join(flattened_plain_text[ : len(flattened_plain_text) - num_X])
	print('Plain Text after Decryption: {}'.format(plain_text))


if __name__ == '__main__':
    plain_text = 'SIDDHESH'
    key = 'HILL'
    print('Plain Text: {}'.format(plain_text))
    print('Key: {}'.format(key))

    # make the key matrix a perfect nxn matrix
    if not is_perfect_square( len(key) ):
        key = key + 'X'*( next_perfect_square(len(key)) - len(key) )        

    hill_cipher(plain_text, key)
