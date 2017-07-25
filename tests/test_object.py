#!/usr/bin/env python

import unittest

class TestObject(unittest.TestCase):
    
    def test_object(self):
        import mlbgame
        data = {
            'string': 'string',
            'int': '10',
            'float': '10.1'
        }
        obj = mlbgame.object.Object(data)
        self.assertIsInstance(obj.string, str)
        self.assertIsInstance(obj.int, int)
        self.assertIsInstance(obj.float, float)
        self.assertEqual(obj.string, 'string')
        self.assertEqual(obj.int, 10)
        self.assertEqual(obj.float, 10.1)
