DEBUG = True
debug_print = print if DEBUG else lambda *x: None
DOT = '.' # denotes blank cell
NULL = 'X'
def print_mat(msg, mat):
    debug_print(msg)
    for row in mat:
        debug_print(' '.join(row))

def _preprocess(inp, k):
    # this function will make sure len(inp) is proper
    # proper = no of elements in top row == no of elements in bottom row

    # to find correct len(inp)
    # if f(n) == len(inp), it is perfect fit, no modifications needed
    # if f(n) >  len(inp), stop iteration, add remaining chars to inp
    def f(n): return n*k + (n-1)*(k-2)
    perfect = False
    n = 0
    for ni in range(1, 10000):
        an = f(ni)
        debug_print('len(inp)', len(inp), 'an', an)
        if an == len(inp):
            perfect = True
            break
        if an > len(inp):
            n = an
            break
    if not perfect:
        inp += NULL * (n - len(inp))

    return inp

def enc_rail(inp, k):

    inp = _preprocess(inp, k)

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

    # region second row
    first_row_indices = list(range(0, len(inp), 2*(k-1)))
    second_row_indices = []
    for findex in first_row_indices:
        if findex != first_row_indices[0]:
            second_row_indices.append( findex - 1 )
        if findex != len(inp) - 1:
            second_row_indices.append( findex + 1 )
    
    # Remove duplicates
    second_row_indices = list(sorted(set(second_row_indices)))

    for si in second_row_indices:
        mat[1][si] = inp[ii]
        ii += 1
        # print_mat('First row, ii=' + str(ii), mat)
    print_mat('Second row', mat)
    # endregion

    # third row onwards
    for ki in range(2, k):
        cur_indices = _get_next_indices(mat, ki-1)
        for ci in cur_indices:
            mat[ki][ci] = inp[ii]
            ii += 1
        print_mat('Row ' + str(ki) + ' done', mat)

    #zigzag begin
    dec = ''
    vi = 0
    vinc = +1 # vertical increment
    for hi, c in enumerate(inp):
        # move right and down
        # then right and up
        dec += mat[vi][hi]
        if vi == k - 1: #last row
            vinc = -1
        if vi == 0: #first row
            vinc = +1
        vi += vinc
    #zigzag end
    return dec.replace(NULL, '')

def _get_next_indices(mat, row_no):
    # returns list of indices of positions to be filled in 
    # next row, based on currently filled positions
    # call only with row_no=1 onwards,
    # ie call with index of second row, get indices of third row

    # region Get current row indices
    non_empty_indices_cur_row = []
    row = mat[row_no]
    ri = 0
    while ri < len(row):
        if row[ri] != DOT: # if non empty
            non_empty_indices_cur_row.append(ri)
        ri += 1
    # endregion

    # Gen next row indices as
    # immediately next index for all even position index
    # and
    # immediately prev index for all odd  position index
    # eg
    # aa = [2, 5, 6]
    # so 2 is even position, ie aa.index(2) == 0, so add next index
    #    5 is odd  position, ie aa.index(5) == 1, so add prev index
    next_row_indices = []
    for ni, nindex in enumerate(non_empty_indices_cur_row):
        if ni % 2 == 0:
            next_row_indices.append(nindex + 1)
        else:
            next_row_indices.append(nindex - 1)

    # Remove duplicates
    next_row_indices = sorted(set(next_row_indices))

    debug_print('CurrentRowNo   :', row_no)
    debug_print('CurrentIndices :', non_empty_indices_cur_row)
    debug_print('NextIndices    :', next_row_indices)

    return next_row_indices
    

if __name__ == '__main__':
    inp = 'ABCDEFGHI' * 4
    k = 2
    assert k > 1
    enc = enc_rail(inp, k)
    dec = dec_rail(enc, k)
    print('Input:', inp)
    print('Enc  :', enc)
    print('Dec  :', dec)
    print('Input == Dec ?', inp == dec)
    assert inp == dec, 'Input != dec'