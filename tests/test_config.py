from redesigned_barnacle.config import convert_value, parse_file, parse_str
from unittest import TestCase
from unittest.mock import mock_open, patch


class ConvertValueTest(TestCase):
    def test_bool(self):
        self.assertEqual(convert_value('TRUE'), True)
        self.assertTrue(type(convert_value('TRUE')) is bool, True)

        self.assertEqual(convert_value('False'), False)
        self.assertTrue(type(convert_value('False')) is bool, True)

    def test_float(self):
        self.assertEqual(convert_value('1.23'), 1.23)
        self.assertTrue(type(convert_value('1.23')) is float)

        self.assertEqual(convert_value('.456'), 0.456)
        self.assertTrue(type(convert_value('.456')) is float)

    def test_int(self):
        self.assertEqual(convert_value('123'), 123)
        self.assertTrue(type(convert_value('123')) is int)

        self.assertEqual(convert_value('009'), 9)
        self.assertTrue(type(convert_value('009')) is int)

    def test_quote(self):
        self.assertEqual(convert_value('"foo"'), 'foo')


class ParseStrTest(TestCase):
    def test_simple(self):
        data = parse_str([
            'foo: 1',
            'bar: str',
        ])
        self.assertDictEqual(data, {
            'bar': 'str',
            'foo': 1,
        })

    def test_blanks(self):
        data = parse_str([
            '',
            'foo: 1',
        ])
        self.assertDictEqual(data, {
            'foo': 1,
        })

    def test_comments(self):
        data = parse_str([
            '# ignore: me',
            'foo: 1',
        ])
        self.assertDictEqual(data, {
            'foo': 1,
        })

    def test_invalid(self):
        data = parse_str([
            'foo:',
            'bar: 3',
            'fin',
        ])
        self.assertDictEqual(data, {
            'bar': 3,
        })


class ParseFileTest(TestCase):
    def test_simple(self):
        mock = mock_open(read_data='''
    foo: 1
    ''')

        data = parse_file('foo', open=mock)
        self.assertDictEqual(data, {
            'foo': 1,
        })
