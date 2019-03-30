import sys
sys.path.append('.')    # if user is outside tests dir.
sys.path.append("..")   # if user is inside  tests dir

from src import utils
import unittest


class TestUtils(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
