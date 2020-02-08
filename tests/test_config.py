from jubilant_train.config import parse_file, parse_str
from unittest import TestCase
from unittest.mock import mock_open, patch


class ParseStrTest(TestCase):
    def test_simple(self):
        data = parse_str([
            'foo: 1',
            'bar: str',
        ])
        self.assertDictEqual(data, {
            'bar': 'str',
            'foo': '1',
        })

    def test_blanks(self):
        data = parse_str([
            '',
            'foo: 1',
        ])
        self.assertDictEqual(data, {
            'foo': '1',
        })

    def test_comments(self):
        data = parse_str([
            '# ignore: me',
            'foo: 1',
        ])
        self.assertDictEqual(data, {
            'foo': '1',
        })

    def test_invalid(self):
        data = parse_str([
            'foo:',
            'bar: 3',
            'fin',
        ])
        self.assertDictEqual(data, {
            'bar': '3',
        })


class ParseFileTest(TestCase):
    def test_simple(self):
        mock = mock_open(read_data='''
    foo: 1
    ''')

        data = parse_file('foo', open=mock)
        self.assertDictEqual(data, {
            'foo': '1',
        })
