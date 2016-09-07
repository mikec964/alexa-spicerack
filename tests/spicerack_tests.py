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
import spicerack.spicerack as srack

import json

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'

class test_spicerack(unittest.TestCase):
    """ Tests """

    def test_launch_response(self):
        response = srack.launch_response()
        pass

    def test_get_spice_location(self):
        json_data = open('intent-getSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.get_spice_location(intent)
        pass

    def test_set_spice_location(self):
        json_data = open('intent-setSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.set_spice_location(intent)
        pass

if __name__ == '__main__':
    unittest.main()
