#!/usr/bin/env python

import unittest

# These three lines allow me to run this from within Sublime Text
import os
import sys
sys.path.append(os.path.abspath('..'))

# From folder.filename import *
# from spicerack.spicerack import *
# OR:
# import folder.filename as filename
import spicerack as srack

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'

class test_spicerack(unittest.TestCase):
    """ Tests """

    def test_launch_response(self):
        pass

    def test_get_spice_location(self):
        pass

    def test_set_spice_location(self):
        pass

if __name__ == '__main__':
    unittest.main()
