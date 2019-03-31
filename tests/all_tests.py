import sys
sys.path.append('.')    # if user is outside tests dir.
sys.path.append("..")   # if user is inside  tests dir

import unittest
from src import utils, other_ciphers


logger = utils.Logger(print)


def _test_cipher(self, encryptor, decryptor, _121=True):
    """
    Tests single cipher text algorithm for correctness.
    _121: whether algo gives one text op for one text ip.
    """
    strings = [utils.get_rand_ascii_str() for i in range(20)]
    strings += ['']
    for string in strings:
        ct = encryptor(string)
        pt = decryptor(ct)
        if _121:
            self.assertEqual( len(ct), len(string) )
        self.assertEqual( pt, string.upper() )


class Tests(unittest.TestCase):
    def test_shift_chars(self):
        # shift char gets the element after displacing elements with dx.
        ip_op = {
            ('a', 2): 'c',
            ('b', -1): 'a',
            ('z', 3): 'c',
            ('c', -4): 'y'
        }

        for ip, op in ip_op.items():
            self.assertEqual( utils.shift_char(*ip), op, "should be "+op )
            self.assertEqual( utils.shift_char(ip[0].upper(), ip[1]), op.upper(), "should be "+op )

        illegal_ips = ["rb", 1, None, 1.0, True]
        for ip in illegal_ips:
            self.assertRaises( ValueError, utils.shift_char, ip, 2)
    
    def test_other_ciphers(self):
        cipher_keys_pairs = {
            'vignere': ("encrypting text"*10, ' ', '@^&*#%$'),
            'shift': (0, 1, -1, 29), 
            'affine': ((17, -1), (7, 19), (15, -99)), 
            'multiplicative': (5, 17, 3, 7)
        }

        for cipher, keys in cipher_keys_pairs.items():
            logger.log(cipher)
            for key in keys:
                # if isinstance(key, tuple):
                #    encryptor = eval('other_ciphers.Ciphers(*key).encrypt_'+cipher)
                #else:
                encryptor = eval('other_ciphers.Ciphers(key).encrypt_'+cipher)
                decryptor =  eval('other_ciphers.Ciphers(key).decrypt_'+cipher)
                _test_cipher(
                    self,
                    encryptor,
                    decryptor
                )
if __name__ == '__main__':
    unittest.main()
