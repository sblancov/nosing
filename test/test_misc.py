import unittest

from misc import StringSet


class MiscTest(unittest.TestCase):

    def setUp(self):
        self.collection = set()
        self.string_set = StringSet(self.collection)

    def tearDown(self):
        del self.string_set


class MiscConstructorTest(unittest.TestCase):

    def test_constructor_fail(self):
        ''' Constructor should raise an exception when no parameters '''
        with self.assertRaises(TypeError):
            StringSet()

    def test_constructor_ok(self):
        ''' Constructor should success with set object as parameter'''
        collection = set()
        string_set = StringSet(collection)
        self.assertIsInstance(string_set, StringSet)

    def test_constructor_param_is_set(self):
        ''' Constructor should receive a set object as parameter '''
        collection = []
        with self.assertRaises(TypeError):
            StringSet(collection)


class MiscAddTest(MiscTest):

    def test_add_no_parameter(self):
        ''' Add method should raise TypeError when no parameters are passed '''
        with self.assertRaises(TypeError):
            self.string_set.add()

    def test_add_an_element(self):
        ''' Add method should add an element to collection '''
        input_data = 'abc'
        expected_data = set(['abc'])
        self.string_set.add(input_data)
        self.assertEqual(self.collection, expected_data)

    def test_add_no_repeated_element(self):
        ''' Add method should not add reapeted elements '''
        input_data = ['abc', 'abc', 'cba']
        expected_data = set(['abc', 'cba'])
        for item in input_data:
            self.string_set.add(item)
        self.assertEqual(self.collection, expected_data)
