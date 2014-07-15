#!/usr/bin/env python

import sys
import unittest
import rot13

class TestDES(unittest.TestCase):
    def test_clean(self):
        string1 = 'test string'
        string2 = 'Hello World!'
        string3 = 'THE QUICK BROWN FOX'
        string4 = 'L3Pt 0V3R tH3 L4Zy D0G'
        string5 = '23140951230991320459-'
        assert(rot13.clean(string1) == 'teststring')
        assert(rot13.clean(string2) == 'helloworld')
        assert(rot13.clean(string3) == 'thequickbrownfox')
        assert(rot13.clean(string4) == 'lptvrthlzydg')
        assert(rot13.clean(string5) == '')

    def test_shift_byte(self):
        ib1 = 'a'
        ib2 = 'g'
        ib3 = 'r'
        ib4 = 'z'
        assert(rot13.shift_byte(ib1, 5, False) == 'f')
        assert(rot13.shift_byte(ib2, 10, True) == 'w')
        assert(rot13.shift_byte(ib3, 13, False) == 'e')
        assert(rot13.shift_byte(ib4, 50, True) == 'b')

if __name__ == "__main__":
    unittest.main()
