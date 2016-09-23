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

class test_database(unittest.TestCase):
    """Test database functions"""

    def setUp(self):
        """Create table if none exists"""
        srack.get_table()

    # @unittest.skip("not yet")
    def test_recall_spice(self):
        user_id = "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMKTLFMOJEWRISWHRVJWUUHGIHTYPR3M6EHBVGX2INBCHNKSRAZ5JBR3DO6QRPM6IIF33T73QA2P3F2I7LGRGZHOITL4UJUJES7PNYC5EFZPVMZGH3FHY5PUTFSKBZCLS6XX5YTDKMU7TJEW6RHXWDSR7LZ4HAT7PF6FJ7CA5N54OMEZUYY2MQ"
        spiceName = "Tumeric"
        spiceLocation = "None"
        spiceRow = "1"
        spiceColumn = "6"
        srack.store_spice(user_id, spiceName, spiceLocation, spiceRow, spiceColumn)
        result = srack.recall_spice(user_id, spiceName)
        # print(result)
        # print(result['spiceLocation'])
        self.assertEqual(result['spiceName'], spiceName)
        self.assertEqual(result['spiceLocation'], spiceLocation)
        self.assertEqual(result['spiceRow'], spiceRow)
        self.assertEqual(result['spiceColumn'], spiceColumn)


class test_lambda(unittest.TestCase):
    """Test lamda handler and basic overhead"""

    def test_lambda_handler(self):
        json_data = open('launch.json').read()
        event = json.loads(json_data)
        response = srack.lambda_handler(event, "")
        pass

    #def test_on_session_started(self):
    #def test_on_session_ended(self):
    #def test_on_launch(self):
    #def test_on_intent(self):

# @unittest.skip("skip spicerack")
class test_spicerack(unittest.TestCase):
    """Test functions specific to spicerack"""

    def test_launch_response(self):
        response = srack.launch_response()
        pass

    def test_get_spice_location(self):
        user_id = "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMKTLFMOJEWRISWHRVJWUUHGIHTYPR3M6EHBVGX2INBCHNKSRAZ5JBR3DO6QRPM6IIF33T73QA2P3F2I7LGRGZHOITL4UJUJES7PNYC5EFZPVMZGH3FHY5PUTFSKBZCLS6XX5YTDKMU7TJEW6RHXWDSR7LZ4HAT7PF6FJ7CA5N54OMEZUYY2MQ"
        json_data = open('intent-getSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.get_spice_location(user_id, intent)
        pass

    def test_set_spice_location(self):
        user_id = "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMKTLFMOJEWRISWHRVJWUUHGIHTYPR3M6EHBVGX2INBCHNKSRAZ5JBR3DO6QRPM6IIF33T73QA2P3F2I7LGRGZHOITL4UJUJES7PNYC5EFZPVMZGH3FHY5PUTFSKBZCLS6XX5YTDKMU7TJEW6RHXWDSR7LZ4HAT7PF6FJ7CA5N54OMEZUYY2MQ"
        json_data = open('intent-setSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.set_spice_location(user_id, intent)
        pass


if __name__ == '__main__':
    unittest.main()
