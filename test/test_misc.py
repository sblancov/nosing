import unittest

from misc import StringSet

STRING = 'abc'
STRING_LIST = ['abc', 'abc', 'cba']


class StringSetTest(unittest.TestCase):

    def setUp(self):
        self.collection = set()
        self.string_set = StringSet(self.collection)

    def tearDown(self):
        del self.string_set


class StringSetConstructorTest(unittest.TestCase):

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


class StringSetAddTest(StringSetTest):

    def test_add_no_parameter(self):
        ''' Add method should raise TypeError when no parameters are passed '''
        with self.assertRaises(TypeError):
            self.string_set.add()

    def test_add_an_element(self):
        ''' Add method should add an element to collection '''
        expected_data = set([STRING])
        self.string_set.add(STRING)
        self.assertEqual(self.collection, expected_data)

    def test_add_no_repeated_element(self):
        ''' Add method should not add reapeted elements '''
        expected_data = set(['abc', 'cba'])
        for item in STRING_LIST:
            self.string_set.add(item)
        self.assertEqual(self.collection, expected_data)

    def test_add_nonstrip_element(self):
        ''' Add method should remove whitespaces from the beginning and the''' \
            ''' end of string '''
        expected_data = set([STRING])
        self.string_set.add(' {} '.format(STRING))
        self.assertEqual(self.collection, expected_data)


class StringSetRemoveTest(StringSetTest):

    def setUp(self):
        super(StringSetRemoveTest, self).setUp()
        for item in STRING_LIST:
            self.string_set.add(item)

    def test_remove_no_parameter(self):
        ''' Remove method should raise TypeError when no parameter is passed'''
        with self.assertRaises(TypeError):
            self.string_set.remove()

    def test_remove_existent_element(self):
        ''' Remove method should remove an added element '''
        self.string_set.remove(STRING)
        expected_data = set(['cba'])
        self.assertEqual(self.collection, expected_data)

    def test_remove_nonexistent_element(self):
        ''' Remove method should not remove a nonexistent element '''
        self.string_set.remove('nonexistent')
        expected_data = set(['abc', 'cba'])
        self.assertEqual(self.collection, expected_data)

    def test_remove_strip_element(self):
        ''' Remove method should remove item stripping whitespaces from the''' \
            '''beggining and the end of string'''
        self.string_set.remove(' abc ')
        expected_data = set(['cba'])
        self.assertEqual(self.collection, expected_data)


class StringSetParseTest(StringSetTest):

    def test_parse_elements(self):
        ''' Parse method should parse a list of strings separated by commas '''
        self.string_set.parse('abc, cba, abc')
        expected_data = set(['abc', 'cba'])
        self.assertEqual(self.collection, expected_data)


class StringSetCleanTest(StringSetTest):

    def test_clean_elements(self):
        ''' Clean method should empty StringSet instance '''
        for item in STRING_LIST:
            self.string_set.add(item)
        self.string_set.clean()
        expected_data = set()
        self.assertEqual(self.collection, expected_data)

    def test_clean_void(self):
        ''' Clean method should do nothing when StringSet is empty '''
        self.string_set.clean()
        expected_data = set()
        self.assertEqual(self.collection, expected_data)


class StringSetContainsTest(StringSetTest):

    def test_contains_true(self):
        ''' __contains__ method should return True when a string is present '''
        expected_data = 'abc'
        self.assertFalse(expected_data in self.string_set)
        for item in STRING_LIST:
            self.string_set.add(item)
        self.assertTrue(expected_data in self.string_set)

    def test_contains_false(self):
        ''' __contains__ method should return False when a string is not ''' \
            '''present '''
        self.assertFalse('def' in self.string_set)

    def test_contains_whitespaces_string(self):
        ''' __contains__ method should return True when a strip string is ''' \
            '''present '''
        expected_data = ' abc '
        self.assertFalse(expected_data in self.string_set)
        for item in STRING_LIST:
            self.string_set.add(item)
        self.assertTrue(expected_data in self.string_set)


class StringSetUnicode(StringSetTest):

    def test_str(self):
        ''' __str__ method should return a list of comma separated ''' \
            '''string '''
        for item in STRING_LIST:
            self.string_set.add(item)
        expected_data = 'abc, cba'
        self.assertEqual(expected_data, str(self.string_set))


class StringSetIter(StringSetTest):

    def test_iter(self):
        ''' __iter__ method should return an item when loop '''

        for item in STRING_LIST:
            self.string_set.add(item)
        expected_data = 'cba'
        for i in self.string_set:
            result = i
        self.assertEqual(expected_data, result)
