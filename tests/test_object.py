#!/usr/bin/env python

import unittest

import mlbgame


class TestObject(unittest.TestCase):
    
    def test_object(self):
        data = {
            'string': 'string',
            'int': '10',
            'float': '10.1',
            'unicode': u'\xe7\x8c\xab'
        }
        obj = mlbgame.object.Object(data)
        self.assertIsInstance(obj.string, str)
        self.assertIsInstance(obj.int, int)
        self.assertIsInstance(obj.float, float)
        try:
            self.assertIsInstance(obj.unicode, unicode)
        except NameError:
            self.assertIsInstance(obj.unicode, str)
        self.assertEqual(obj.string, 'string')
        self.assertEqual(obj.int, 10)
        self.assertEqual(obj.float, 10.1)
        self.assertEqual(obj.unicode, u'\xe7\x8c\xab')
