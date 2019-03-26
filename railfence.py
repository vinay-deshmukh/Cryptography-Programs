DEBUG = True
debug_print = print if DEBUG else lambda *x: None
DOT = '.' # denotes blank cell
def print_mat(msg, mat):
    print(msg)
    for row in mat:
        print(' '.join(row))

def zigzag_traversal(mat, func):
    # mat = matrix
    # func = function to execute for element
    pass

def enc_rail(inp, k):
    mat = [ [ DOT for i in inp ]  for _ in range(k)]
    print_mat('Encode Init:', mat)

    vi = 0
    vinc = +1 # vertical increment
    for hi, c in enumerate(inp):
        # move right and down
        # then right and up
        mat[vi][hi] = c
        if vi == k - 1: #last row
            vinc = -1
        if vi == 0: #first row
            vinc = +1
        vi += vinc
    print_mat('After insert:', mat)

    enc = ''.join(c for row in mat for c in row)
    return enc.replace(DOT, '')

def dec_rail(inp, k):
    mat = [ [ DOT for i in inp ]  for _ in range(k)]
    print_mat('Decode Init:', mat)

    # fill first row, in 2*(k-1) increments
    ii = 0
    hi = 0
    while hi < len(inp):
        mat[0][hi] = inp[ii]
        ii += 1
        hi += 2 * (k-1)
    print_mat('First row', mat)

    # second row
    first_row_indices = list(range(0, len(inp), 2*(k-1)))
    second_row_indices = []
    for findex in first_row_indices:
        if findex != first_row_indices[0]:
            second_row_indices.append( findex - 1 )
        if findex != first_row_indices[-1]:
            second_row_indices.append( findex + 1 )
    for si in second_row_indices:
        mat[1][si] = inp[ii]
        ii += 1
    print_mat('Second row', mat)

    # third row onwards
    for ki in range(2, k):
        cur_indices = _get_next_indices(mat, ki-1)
        for ci in cur_indices:
            mat[ki][ci] = inp[ii]
            ii += 1
        print_mat('Row ' + str(ki) + ' done', mat)


    return ''

def _get_next_indices(mat, row_no):
    non_empty_indices_cur_row = []
    row = mat[row_no]
    ri = 0
    while ri < len(row):
        if row[ri] != DOT: # if non empty
            non_empty_indices_cur_row.append(ri)
        ri += 1

    # Gen next row indices as
    # immediately next index of first index,
    # then for each following index, 
    #     take index from one before and one after
    next_row_indices = []
    #next_row_indices.append( non_empty_indices_cur_row[0] + 1 )
    for ni, nindex in enumerate(non_empty_indices_cur_row):
        # next_row_indices.append( nindex - 1 )

        # if nindex != non_empty_indices_cur_row[-1]:
        #     # find right index, only if ni is not last element
        #     next_row_indices.append( nindex + 1 )
        if ni % 2 == 0:
            next_row_indices.append( nindex + 1)
        else:
            next_row_indices.append( nindex - 1)

    # Remove duplicates
    next_row_indices = sorted(set(next_row_indices))
    debug_print('Row :', row_no)
    debug_print('Cur :', non_empty_indices_cur_row)
    debug_print('Next:', next_row_indices)

    return next_row_indices
    

if __name__ == '__main__':
    inp = 'ABCDEFGHI'
    k = 3
    assert k >= 3
    enc = enc_rail(inp, k)
    dec = dec_rail(enc, k)
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    print('Input == Dec ?', inp == dec)
    assert inp == dec, 'Input != dec'